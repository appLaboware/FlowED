CREATE CONSTRAINT failure_code IF NOT EXISTS
FOR (f:Failure) REQUIRE f.code IS UNIQUE;

CREATE CONSTRAINT decision_id IF NOT EXISTS
FOR (d:Decision) REQUIRE d.id IS UNIQUE;

CREATE CONSTRAINT action_id IF NOT EXISTS
FOR (a:Action) REQUIRE a.id IS UNIQUE;

CREATE VECTOR INDEX failure_embeddings IF NOT EXISTS
FOR (f:Failure)
ON f.embedding
OPTIONS { indexConfig: {
  `vector.dimensions`: 8,
  `vector.similarity_function`: 'cosine'
}};

MERGE (s1:Evidence {id:'cbr-4r-2005'})
SET s1.kind='research',
    s1.title='Retrieval, reuse, revision and retention in case-based reasoning',
    s1.url='https://doi.org/10.1017/S0269888906000646';

MERGE (s2:Evidence {id:'ms-decision-theoretic-cbr-1996'})
SET s2.kind='research',
    s2.title='Decision-Theoretic Case-Based Reasoning',
    s2.url='https://www.microsoft.com/en-us/research/publication/decision-theoretic-case-based-reasoning/';

MERGE (s3:Evidence {id:'ms-graphrag'})
SET s3.kind='research-implementation',
    s3.title='Microsoft GraphRAG',
    s3.url='https://github.com/microsoft/graphrag',
    s3.note='Knowledge graph retrieval inspiration only - not execution authority';

MERGE (f1:Failure {code:'azure.credentials.separate_missing'})
SET f1.description='Preferred split Azure repository secrets are absent while a legacy aggregate AZURE secret may exist',
    f1.embedding=[1.0,1.0,0.0,1.0,0.0,0.0,1.0,1.0];

MERGE (d1:Decision {id:'decision.azure.parse_legacy_bundle'})
SET d1.status='approved',
    d1.automation='automatic',
    d1.risk='low',
    d1.priority=100,
    d1.userNotice='Azure split secrets were not available; using the compatible legacy AZURE key-value bundle for this run.',
    d1.successCount=coalesce(d1.successCount,0),
    d1.failureCount=coalesce(d1.failureCount,0);

MERGE (a1:Action {id:'azure.credentials.parse_legacy_bundle'})
SET a1.kind='adapter',
    a1.effect='Parse AZURE_CLIENT_ID, AZURE_TENANT_ID and AZURE_SUBSCRIPTION_ID from legacy AZURE text';

MERGE (g1:Guard {id:'guard.legacy_azure_bundle_present'})
SET g1.key='legacy_azure_bundle_present', g1.value='true';

MATCH (f1:Failure {code:'azure.credentials.separate_missing'}),
      (d1:Decision {id:'decision.azure.parse_legacy_bundle'}),
      (a1:Action {id:'azure.credentials.parse_legacy_bundle'}),
      (g1:Guard {id:'guard.legacy_azure_bundle_present'}),
      (s1:Evidence {id:'cbr-4r-2005'}),
      (s2:Evidence {id:'ms-decision-theoretic-cbr-1996'})
MERGE (f1)-[:RESOLVED_BY]->(d1)
MERGE (d1)-[:EXECUTES]->(a1)
MERGE (d1)-[:REQUIRES]->(g1)
MERGE (d1)-[:SUPPORTED_BY]->(s1)
MERGE (d1)-[:SUPPORTED_BY]->(s2);

MERGE (f2:Failure {code:'dns.requested_provider_credentials_missing'})
SET f2.description='A custom DNS name was requested but DNS provider credentials are unavailable',
    f2.embedding=[0.0,0.0,1.0,0.0,1.0,1.0,1.0,1.0];

MERGE (d2:Decision {id:'decision.dns.use_azure_provider_fqdn'})
SET d2.status='approved',
    d2.automation='automatic',
    d2.risk='low',
    d2.priority=100,
    d2.userNotice='The requested custom DNS could not be configured; deployment continued using the Azure-provided hostname.',
    d2.successCount=coalesce(d2.successCount,0),
    d2.failureCount=coalesce(d2.failureCount,0);

MERGE (a2:Action {id:'delivery.use_azure_provider_fqdn'})
SET a2.kind='fallback',
    a2.effect='Continue deployment and expose the Azure-provided FQDN instead of failing the cycle';

MERGE (g2:Guard {id:'guard.azure_provider_fqdn_available'})
SET g2.key='azure_provider_fqdn_available', g2.value='true';

MATCH (f2:Failure {code:'dns.requested_provider_credentials_missing'}),
      (d2:Decision {id:'decision.dns.use_azure_provider_fqdn'}),
      (a2:Action {id:'delivery.use_azure_provider_fqdn'}),
      (g2:Guard {id:'guard.azure_provider_fqdn_available'}),
      (s1:Evidence {id:'cbr-4r-2005'}),
      (s2:Evidence {id:'ms-decision-theoretic-cbr-1996'}),
      (s3:Evidence {id:'ms-graphrag'})
MERGE (f2)-[:RESOLVED_BY]->(d2)
MERGE (d2)-[:EXECUTES]->(a2)
MERGE (d2)-[:REQUIRES]->(g2)
MERGE (d2)-[:SUPPORTED_BY]->(s1)
MERGE (d2)-[:SUPPORTED_BY]->(s2)
MERGE (d2)-[:SUPPORTED_BY]->(s3);
