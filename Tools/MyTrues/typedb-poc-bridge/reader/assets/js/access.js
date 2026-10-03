document.addEventListener('DOMContentLoaded',async()=>{
 let d={unavailable:'Acesso temporariamente indisponível.'};
 try{const loaded=await MyTruesI18n.load('access');d=loaded.d;MyTruesI18n.apply(d);document.documentElement.lang=loaded.locale}catch(e){}
 const p=new URLSearchParams(location.search),status=document.getElementById('access-status');
 if(status&&p.get('status')){status.textContent=d.unavailable||'Acesso temporariamente indisponível.';status.classList.add('has-error');status.setAttribute('title',status.textContent)}
});
