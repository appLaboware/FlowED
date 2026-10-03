const {createApp}=Vue;
createApp({
 data:()=>({
  me:null,section:'home',query:'',events:[],people:[],loading:false,saving:false,
  truthDialog:false,personDialog:false,snackbar:false,message:'',claimCode:'',lastInvite:'',
  adminTab:'people',admin:{people:[],interests:[],admins:[],counts:{people:0,interests:0,admins:0}},
  i18n:{},locale:'pt-BR',
  suggestions:['npm','pnpm','OAuth','schema','package manager'],
  form:{subject:'',statement:'',kind:'truth',relation:'none',related_occurrence:null},
  personForm:{display_name:'',email:'',role:'member'}
 }),
 computed:{
  nav(){
   const x=[
    {id:'home',label:this.t('nav_home'),icon:'mdi-home-outline'},
    {id:'memory',label:this.t('nav_memory'),icon:'mdi-timeline-text-outline'}
   ];
   if(this.me?.role==='admin')x.push({id:'people',label:this.t('nav_people'),icon:'mdi-account-multiple-outline'});
   return x
  },
  mobileNav(){return [...this.nav,{id:'new',label:this.t('new_truth'),icon:'mdi-plus-circle-outline'}].slice(0,4)},
  kindItems(){return[
   {title:this.t('type_truth'),value:'truth'},{title:this.t('type_observation'),value:'observation'},
   {title:this.t('type_decision'),value:'decision'},{title:this.t('type_preference'),value:'preference'},
   {title:this.t('type_correction'),value:'correction'}]},
  relationItems(){return[
   {title:this.t('relation_none'),value:'none'},{title:this.t('relation_continues'),value:'continues'},
   {title:this.t('relation_corrects'),value:'corrects'},{title:this.t('relation_confirms'),value:'confirms'},
   {title:this.t('relation_contradicts'),value:'contradicts'},{title:this.t('relation_based_on'),value:'based-on'},
   {title:this.t('relation_influenced_by'),value:'influenced-by'}]},
  roleItems(){return[{title:this.t('role_member'),value:'member'},{title:this.t('role_admin'),value:'admin'}]},
  occurrenceItems(){return[...this.events].reverse().map(e=>({value:e.id,title:this.short(this.humanTitle(e),72)}))}
 },
 async mounted(){
  const pack=await MyTruesI18n.load('portal');this.i18n=pack.d;this.locale=pack.locale;document.documentElement.lang=pack.locale;
  await this.loadMe();
  if(this.me?.role!=='unbound'){await this.search();if(this.me?.role==='admin')await this.loadAdmin()}
 },
 methods:{
  t(k){return this.i18n[k]||k},
  async api(url,opt={}){
   const r=await fetch(url,{credentials:'same-origin',headers:{'Content-Type':'application/json',...(opt.headers||{})},...opt});
   if(r.status===401){location.href='/login';throw new Error('auth')}
   const d=await r.json().catch(()=>({}));if(!r.ok)throw new Error(d.detail||this.t('error_generic'));return d
  },
  async loadMe(){this.me=await this.api('/api/me')},
  go(id){if(id==='new'){this.openNew();return}this.section=id;if(id==='people')this.loadAdmin()},
  switchLocale(){MyTruesI18n.setLocale(this.locale==='pt-BR'?'en':'pt-BR')},
  async search(){
   this.loading=true;
   try{const d=await this.api('/api/history?q='+encodeURIComponent(this.query||''));this.events=d.events||[]}
   catch(e){this.toast(e.message)}finally{this.loading=false}
  },
  openNew(){this.form={subject:this.query||'',statement:'',kind:'truth',relation:'none',related_occurrence:null};this.truthDialog=true},
  continueFrom(e,rel='continues'){this.form={subject:this.subjectOf(e)||this.query||'',statement:'',kind:rel==='corrects'?'correction':'truth',relation:rel,related_occurrence:e.id};this.truthDialog=true},
  async saveTruth(){
   this.saving=true;
   try{const d=await this.api('/api/occurrences',{method:'POST',body:JSON.stringify(this.form)});this.truthDialog=false;this.query=this.form.subject;await this.search();this.section='memory';this.toast(d.id)}
   catch(e){this.toast(e.message)}finally{this.saving=false}
  },
  async loadAdmin(){
   if(this.me?.role!=='admin')return;
   try{
    this.admin=await this.api('/api/admin/overview');
    this.people=this.admin.people||[];
   }catch(e){this.toast(e.message)}
  },
  async loadPeople(){return this.loadAdmin()},
  async savePerson(){
   try{
    const d=await this.api('/api/people',{method:'POST',body:JSON.stringify(this.personForm)});
    this.lastInvite=d.invite_code;
    await this.loadAdmin();
    this.toast(this.t('person_created_ok'));
   }catch(e){this.toast(e.message)}
  },
  async claim(){try{await this.api('/api/claim',{method:'POST',body:JSON.stringify({code:this.claimCode})});location.reload()}catch(e){this.toast(e.message)}},
  toast(s){this.message=s;this.snackbar=true;setTimeout(()=>this.snackbar=false,4200)},
  initials(s){return String(s||'?').split(/\s+/).slice(0,2).map(x=>x[0]||'').join('').toUpperCase()},
  link(e,k){return e.links?.find(l=>l.key===k)},
  val(e,k){const l=this.link(e,k);return l?(l.valueLexical||this.labelValue(l.value)):''},
  subjectOf(e){return this.val(e,'key:subject')},
  bucket(e){const t=e.type||this.link(e,'key:type')?.value||'';if(String(t).includes('decision'))return'decision';if(String(t).includes('correction'))return'correction';if(String(t).includes('preference'))return'preference';return'experience'},
  humanType(e){return({decision:this.t('type_decision'),correction:this.t('type_correction'),preference:this.t('type_preference'),experience:this.t('type_observation')})[this.bucket(e)]},
  humanTitle(e){return this.val(e,'key:statement')||e.id.replace('occ:','')},
  humanBody(e){const subject=this.subjectOf(e),author=this.val(e,'key:author');return [subject,author].filter(Boolean).join(' · ')},
  labelValue(v){return String(v||'').replace(/^occ:/,'').replace(/^[a-z-]+:/,'').replaceAll('-',' ')},
  date(v){if(!v)return'';const d=new Date(v);return Number.isNaN(d.getTime())?v:d.toLocaleString(this.locale,{day:'2-digit',month:'short',year:'numeric',hour:'2-digit',minute:'2-digit'})},
  short(s,n){s=String(s||'');return s.length>n?s.slice(0,n-1)+'…':s}
 }
}).mount('#app');