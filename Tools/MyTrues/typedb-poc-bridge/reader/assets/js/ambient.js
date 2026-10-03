(()=>{
const canvas=document.getElementById('ambient');if(!canvas)return;
const ctx=canvas.getContext('2d',{alpha:false});
const reduced=matchMedia('(prefers-reduced-motion: reduce)').matches;
let w=0,h=0,dpr=1,start=performance.now(),last=0;

function resize(){
  dpr=Math.min(devicePixelRatio||1,1.5);
  w=innerWidth;h=innerHeight;
  canvas.width=Math.max(1,Math.round(w*dpr));
  canvas.height=Math.max(1,Math.round(h*dpr));
  canvas.style.width=w+'px';canvas.style.height=h+'px';
  ctx.setTransform(dpr,0,0,dpr,0,0);
}

function splitX(y,t){
  const yn=y/Math.max(h,1);
  const base=w*(w<560?.52:.56);
  const broad=Math.sin(t*.42+yn*Math.PI*1.35)*w*(w<560?.075:.06);
  const detail=Math.sin(t*.68-yn*Math.PI*3.15+1.4)*w*(w<560?.024:.018);
  return base+broad+detail;
}

function fillField(t){
  ctx.fillStyle='#f3f1eb';ctx.fillRect(0,0,w,h);

  const cool=ctx.createLinearGradient(0,0,w*.72,h);
  cool.addColorStop(0,'#e6ebe7');
  cool.addColorStop(.58,'#e9ede9');
  cool.addColorStop(1,'#eff1ed');
  ctx.fillStyle=cool;ctx.fillRect(0,0,w,h);

  const warm=ctx.createLinearGradient(w*.25,0,w,h);
  warm.addColorStop(0,'#efe5de');
  warm.addColorStop(.55,'#ecd9cd');
  warm.addColorStop(1,'#e8cbbb');

  ctx.beginPath();
  ctx.moveTo(w,0);ctx.lineTo(splitX(0,t),0);
  const step=Math.max(18,Math.round(h/44));
  for(let y=0;y<=h+step;y+=step)ctx.lineTo(splitX(y,t),y);
  ctx.lineTo(w,h);ctx.closePath();ctx.fillStyle=warm;ctx.fill();

  const seam=ctx.createLinearGradient(0,0,w,h);
  seam.addColorStop(0,'rgba(45,91,75,.055)');
  seam.addColorStop(.48,'rgba(255,255,255,.12)');
  seam.addColorStop(1,'rgba(201,104,61,.06)');
  ctx.beginPath();ctx.moveTo(splitX(0,t),0);
  for(let y=0;y<=h+step;y+=step)ctx.lineTo(splitX(y,t),y);
  ctx.strokeStyle=seam;ctx.lineWidth=Math.max(96,Math.min(w,h)*.22);ctx.lineCap='round';ctx.stroke();
}

function cell(x,y,r,inner,outer,alpha){
  const g=ctx.createRadialGradient(x,y,0,x,y,r);
  g.addColorStop(0,inner.replace('ALPHA',alpha));
  g.addColorStop(.42,inner.replace('ALPHA',alpha*.54));
  g.addColorStop(1,outer);
  ctx.fillStyle=g;ctx.fillRect(x-r,y-r,r*2,r*2);
}

function thoughts(t){
  const s=Math.max(w,h);
  cell(
    w*(.16+.10*Math.sin(t*.46)),
    h*(.22+.11*Math.cos(t*.39)),
    s*.34,'rgba(31,91,72,ALPHA)','rgba(31,91,72,0)',.105
  );
  cell(
    w*(.84+.08*Math.cos(t*.43+1.2)),
    h*(.72+.12*Math.sin(t*.40)),
    s*.37,'rgba(196,94,50,ALPHA)','rgba(196,94,50,0)',.095
  );
  cell(
    w*(.55+.15*Math.sin(t*.36+2.4)),
    h*(.45+.13*Math.cos(t*.41+1.1)),
    s*.27,'rgba(255,255,255,ALPHA)','rgba(255,255,255,0)',.34
  );
}

function frame(now){
  if(!reduced&&now-last<30){requestAnimationFrame(frame);return}
  last=now;
  const t=reduced?1.2:(now-start)/1000;
  fillField(t);thoughts(t);
  if(!reduced)requestAnimationFrame(frame);
}

addEventListener('resize',resize,{passive:true});
resize();requestAnimationFrame(frame);
})();