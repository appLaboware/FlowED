#!/usr/bin/env python3
import json, time, urllib.request, urllib.error

A="http://127.0.0.1:18081"
B="http://127.0.0.1:18082"

def wait(url):
    for _ in range(60):
        try:
            if urllib.request.urlopen(url+"/healthz",timeout=2).status == 200: return
        except Exception: time.sleep(1)
    raise RuntimeError(url)

def call(method,url,payload=None):
    data=None if payload is None else json.dumps(payload).encode()
    req=urllib.request.Request(url,data=data,method=method,headers={"Content-Type":"application/json"})
    with urllib.request.urlopen(req,timeout=5) as r:
        return r.status, dict(r.headers), json.load(r)

for u in (A,B): wait(u)

dns={
 "protocol":"mytrues.decision/v1","requestId":"dns-1",
 "subject":{"kind":"failure","code":"dns.requested_provider_credentials_missing"},
 "context":{
  "azure_provider_fqdn_available":True,
  "azure_provider_fqdn":"site.example.brazilsouth.azurecontainer.io",
  "azure_public_ip_available":True,
  "azure_public_ip":"203.0.113.42"
 }
}
sa,_,da=call("POST",A+"/v1/decisions/resolve.failure",dns)
sb,_,db=call("POST",B+"/v1/decisions/resolve.failure",dns)
assert sa==sb==200
assert da["provider"]["id"]=="senior-a" and da["selected"]["result"]["endpoint"]["type"]=="hostname"
assert db["provider"]["id"]=="senior-b" and db["selected"]["result"]["endpoint"]["type"]=="ip"

unknown={
 "protocol":"mytrues.decision/v1","requestId":"php-unknown-1",
 "subject":{"kind":"failure","code":"runtime.php.extension_missing"},
 "context":{
  "runtime":"php","database":"mysql","missing_extension":"pdo_mysql",
  "customer_domain":"private.customer.example",
  "AZURE_CLIENT_ID":"real-client-id-must-not-leak",
  "public_ip":"198.51.100.77"
 }
}
pa,ha,pba=call("POST",A+"/v1/decisions/resolve.failure",unknown)
pb,hb,pbb=call("POST",B+"/v1/decisions/resolve.failure",unknown)
assert pa==pb==202
serialized=json.dumps(pba)
for forbidden in ("private.customer.example","real-client-id-must-not-leak","198.51.100.77"):
    assert forbidden not in serialized
assert pba["casePacket"]["abstractContext"]["runtime"]=="php"
assert pba["casePacket"]["abstractContext"]["missing_extension"]=="pdo_mysql"

resolution={
 "decision":{
  "id":"decision.php.install_pdo_mysql",
  "action":"runtime.install_missing_extension",
  "result":{"extension":"pdo_mysql","strategy":"install-and-retry"},
  "guards":[{"key":"runtime_is_php"}],
  "notice":"Provider senior-a approved installation of the missing PHP extension and retry."
 }
}
drid=pba["decisionRequestId"]
sr,_,resolved=call("POST",A+f"/v1/provider/decision-requests/{drid}/resolution",resolution)
assert sr==200 and resolved["status"]=="decided"

gr,_,after=call("GET",A+f"/v1/decision-requests/{drid}")
assert gr==200 and after["decision"]["id"]=="decision.php.install_pdo_mysql"

repeat,_,learned=call("POST",A+"/v1/decisions/resolve.failure",{**unknown,"requestId":"php-unknown-2"})
assert repeat==200 and learned["decision"]["id"]=="decision.php.install_pdo_mysql"

br,_,still=call("GET",B+pbb["statusUrl"])
assert br==202 and still["status"]=="awaiting-provider-decision"

print(json.dumps({
 "protocol":"PASS",
 "provider_choice_changes_dns_outcome":{
   "senior-a":da["selected"]["result"],
   "senior-b":db["selected"]["result"]
 },
 "unknown_case":{
   "senior-a_initial":"awaiting-provider-decision",
   "senior-a_after_human":"decided",
   "senior-a_future_same_case":"decided-immediately",
   "senior-b":"still-awaiting-provider-decision"
 },
 "anonymization":"PASS"
},indent=2))
