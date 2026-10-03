(()=>{
const canvas=document.getElementById('ambient');if(!canvas)return;
const ctx=canvas.getContext('2d',{alpha:true});let w=0,h=0,dpr=1,start=performance.now(),raf=0;
const reduced=matchMedia('(prefers-reduced-motion: reduce)').matches;
const palette={green:[35,72,59],orange:[216,121,69],sage:[104,128,112]};
function resize(){
  dpr=Math.min(devicePixelRatio||1,1.75);w=innerWidth;h=innerHeight;
  canvas.width=Math.max(1,Math.floor(w*dpr));canvas.height=Math.max(1,Math.floor(h*dpr));
  canvas.style.width=w+'px';canvas.style.height=h+'px';ctx.setTransform(dpr,0,0,dpr,0,0)
}
function glow(x,y,r,rgb,a){
  const g=ctx.createRadialGradient(x,y,0,x,y,r);
  g.addColorStop(0,`rgba(${rgb.join(',')},${a})`);
  g.addColorStop(.45,`rgba(${rgb.join(',')},${a*.34})`);
  g.addColorStop(1,`rgba(${rgb.join(',')},0)`);
  ctx.fillStyle=g;ctx.fillRect(x-r,y-r,r*2,r*2)
}
function thread(y,amp,phase,rgb,a,width=1){
  ctx.beginPath();
  const steps=32;
  for(let i=0;i<=steps;i++){
    const x=(i/steps)*w;
    const envelope=.45+.55*Math.sin((i/steps)*Math.PI);
    const yy=y+Math.sin((i/steps)*Math.PI*2.15+phase)*amp*envelope+
      Math.sin((i/steps)*Math.PI*5.2-phase*.62)*amp*.18;
    if(i===0)ctx.moveTo(x,yy);else ctx.lineTo(x,yy)
  }
  ctx.strokeStyle=`rgba(${rgb.join(',')},${a})`;ctx.lineWidth=width;ctx.stroke()
}
function frame(now){
  ctx.clearRect(0,0,w,h);
  const t=reduced?0:(now-start)/1000;
  const phase=t*1.08;
  glow(w*(.17+.055*Math.sin(t*.72)),h*(.30+.055*Math.cos(t*.58)),Math.max(w,h)*.31,palette.green,.045);
  glow(w*(.84+.045*Math.cos(t*.64)),h*(.72+.06*Math.sin(t*.69)),Math.max(w,h)*.27,palette.orange,.038);
  ctx.save();ctx.globalCompositeOperation='multiply';
  for(let i=0;i<6;i++)thread(h*(.18+i*.115),18+i*2.6,phase+i*.72,palette.green,.028+i*.003,.7);
  for(let i=0;i<4;i++)thread(h*(.34+i*.145),14+i*3.3,-phase*.86+i*.95,palette.orange,.022+i*.004,.72);
  thread(h*.58,24,phase*.58+1.4,palette.sage,.022,.62);
  ctx.restore();
  if(!reduced)raf=requestAnimationFrame(frame)
}
addEventListener('resize',resize,{passive:true});resize();
if(reduced)frame(start);else raf=requestAnimationFrame(frame);
document.addEventListener('visibilitychange',()=>{if(document.hidden&&raf){cancelAnimationFrame(raf);raf=0}else if(!document.hidden&&!reduced&&!raf){start=performance.now();raf=requestAnimationFrame(frame)}})
})();
