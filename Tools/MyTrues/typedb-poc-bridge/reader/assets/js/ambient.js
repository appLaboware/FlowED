(()=>{
const canvas=document.getElementById('ambient');if(!canvas)return;
const ctx=canvas.getContext('2d',{alpha:true});let w=0,h=0,dpr=1,start=performance.now();
const reduced=matchMedia('(prefers-reduced-motion: reduce)').matches;
function resize(){dpr=Math.min(devicePixelRatio||1,2);w=innerWidth;h=innerHeight;canvas.width=w*dpr;canvas.height=h*dpr;canvas.style.width=w+'px';canvas.style.height=h+'px';ctx.setTransform(dpr,0,0,dpr,0,0)}
function blob(x,y,r,rgb,a){const g=ctx.createRadialGradient(x,y,0,x,y,r);g.addColorStop(0,`rgba(${rgb},${a})`);g.addColorStop(.48,`rgba(${rgb},${a*.48})`);g.addColorStop(1,`rgba(${rgb},0)`);ctx.fillStyle=g;ctx.fillRect(x-r,y-r,r*2,r*2)}
function frame(now){ctx.clearRect(0,0,w,h);const t=reduced?0:(now-start)/1000;
 const x1=w*(.20+.11*Math.sin(t*.82)),y1=h*(.27+.12*Math.cos(t*.71));
 const x2=w*(.79+.10*Math.cos(t*.63)),y2=h*(.67+.13*Math.sin(t*.77));
 const x3=w*(.56+.07*Math.sin(t*.94+1.2)),y3=h*(.17+.08*Math.cos(t*.86));
 blob(x1,y1,Math.max(w,h)*.36,'27,101,73',.078);
 blob(x2,y2,Math.max(w,h)*.30,'230,116,58',.066);
 blob(x3,y3,Math.max(w,h)*.23,'127,151,116',.040);
 if(!reduced)requestAnimationFrame(frame)}
addEventListener('resize',resize,{passive:true});resize();requestAnimationFrame(frame);
})();