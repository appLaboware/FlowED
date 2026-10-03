(()=>{
const canvas=document.getElementById('ambient'); if(!canvas) return;
const ctx=canvas.getContext('2d',{alpha:true}); let w=0,h=0,dpr=1,start=performance.now();
const reduced=matchMedia('(prefers-reduced-motion: reduce)').matches;
function resize(){dpr=Math.min(devicePixelRatio||1,2);w=innerWidth;h=innerHeight;canvas.width=w*dpr;canvas.height=h*dpr;canvas.style.width=w+'px';canvas.style.height=h+'px';ctx.setTransform(dpr,0,0,dpr,0,0)}
function blob(x,y,r,color,a){const g=ctx.createRadialGradient(x,y,0,x,y,r);g.addColorStop(0,color.replace('ALPHA',a));g.addColorStop(.48,color.replace('ALPHA',a*.48));g.addColorStop(1,color.replace('ALPHA','0'));ctx.fillStyle=g;ctx.fillRect(x-r,y-r,r*2,r*2)}
function frame(now){ctx.clearRect(0,0,w,h);const t=(now-start)/1000;
 const f=reduced?0:t;
 const x1=w*(.20+.10*Math.sin(f*.72)), y1=h*(.28+.11*Math.cos(f*.62));
 const x2=w*(.78+.09*Math.cos(f*.56)), y2=h*(.66+.12*Math.sin(f*.68));
 const x3=w*(.56+.06*Math.sin(f*.83+1.4)), y3=h*(.18+.07*Math.cos(f*.77));
 blob(x1,y1,Math.max(w,h)*.36,'rgba(29,104,76,ALPHA)',.085);
 blob(x2,y2,Math.max(w,h)*.31,'rgba(231,117,61,ALPHA)',.075);
 blob(x3,y3,Math.max(w,h)*.24,'rgba(113,150,120,ALPHA)',.045);
 if(!reduced) requestAnimationFrame(frame)
}
addEventListener('resize',resize,{passive:true});resize();requestAnimationFrame(frame);
})();