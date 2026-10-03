(()=>{
const canvas=document.getElementById('ambient');if(!canvas)return;
const ctx=canvas.getContext('2d',{alpha:true});let w=0,h=0,dpr=1,start=performance.now();
const reduced=matchMedia('(prefers-reduced-motion: reduce)').matches;
function resize(){dpr=Math.min(devicePixelRatio||1,2);w=innerWidth;h=innerHeight;canvas.width=w*dpr;canvas.height=h*dpr;canvas.style.width=w+'px';canvas.style.height=h+'px';ctx.setTransform(dpr,0,0,dpr,0,0)}
function glow(x,y,r,rgb,a){const g=ctx.createRadialGradient(x,y,0,x,y,r);g.addColorStop(0,'rgba('+rgb+','+a+')');g.addColorStop(.42,'rgba('+rgb+','+(a*.46)+')');g.addColorStop(1,'rgba('+rgb+',0)');ctx.fillStyle=g;ctx.fillRect(x-r,y-r,r*2,r*2)}
function ribbon(t,phase,color,alpha){ctx.save();ctx.globalAlpha=alpha;ctx.lineWidth=Math.max(1,w*.0011);ctx.strokeStyle=color;ctx.beginPath();const amp=h*.085;for(let x=-40;x<=w+40;x+=26){const y=h*(.52+.17*Math.sin(t*.48+phase))+amp*Math.sin(x/w*5.2+t*.9+phase);if(x===-40)ctx.moveTo(x,y);else ctx.lineTo(x,y)}ctx.stroke();ctx.restore()}
function frame(now){ctx.clearRect(0,0,w,h);const t=reduced?0:(now-start)/1000;const s=Math.max(w,h);
glow(w*(.16+.19*Math.sin(t*.55)),h*(.26+.15*Math.cos(t*.48)),s*.39,'26,89,70',.086);
glow(w*(.82+.16*Math.cos(t*.47+1)),h*(.69+.17*Math.sin(t*.58)),s*.35,'205,108,64',.072);
glow(w*(.54+.12*Math.sin(t*.71+2.1)),h*(.16+.09*Math.cos(t*.64)),s*.27,'105,139,105',.045);
ribbon(t,0,'rgba(22,63,52,.20)',.26);ribbon(t,2.25,'rgba(201,111,67,.22)',.22);
if(!reduced)requestAnimationFrame(frame)}
addEventListener('resize',resize,{passive:true});resize();requestAnimationFrame(frame);
})();