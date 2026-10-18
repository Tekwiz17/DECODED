/* Coordinate-accurate SVG learning models with cancellable, reduced-motion-aware animation. */
const GeoLab=(()=>{
 let kind='',value=0,target=0,raf=0,playing=false,last=0,direction=1;
 const reduced=window.matchMedia('(prefers-reduced-motion: reduce)');
 const specs={
 'geo-radical':['Square roots you can see','Square side',1,10,6,'The area is side². Its principal square root is the side length.'],
 'geo-triangle':['Build a right triangle','Vertical leg',1,10,4,'The horizontal leg stays 3. The diagonal is always opposite the right angle.'],
 'geo-quadratic':['Move a parabola, find its roots','Vertical shift',-5,5,-4,'The graph is y = x² + k. Roots are the x-values where y = 0.'],
 'geo-system':['Count the intersections','Horizontal line height',-2,6,4,'The curve is y = x². The line is y = k. A solution belongs to both graphs.'],
 'geo-segment':['A segment, piece by piece','Position of B (%)',10,90,40,'B stays between A and C. The two parts always add to the whole.'],
 'geo-midpoint':['Find the middle','Endpoint B: x',-2,8,6,'A = (−4,−2), B = (b,4). The midpoint averages x and y separately.'],
 'geo-slope':['Watch rise over run','Slope m',-3,3,1,'The line is y = mx + 1. Each horizontal run of 1 changes y by m.'],
 'geo-angle':['Turn, classify, bisect','Angle (degrees)',10,180,70,'The dashed ray bisects the whole angle into two congruent angles.'],
 'geo-parallel':['One transversal, matching angles','Transversal angle',25,155,65,'The two horizontal lines stay parallel. Matching positions have equal angle measures.'],
 'geo-lines':['Parallel or perpendicular?','Original slope',-3,3,1,'Purple is the original line, green is parallel, and orange is perpendicular.'],
 'geo-centers':['Two centers, two different jobs','Triangle height',2,6,3,'The incenter touches sides with equal perpendicular radii. The circumcenter reaches all vertices.']
 };
 const n=x=>Number(x.toFixed(2));
 const line=(x1,y1,x2,y2,color='#8871dc',dash='')=>`<line x1="${n(x1)}" y1="${n(y1)}" x2="${n(x2)}" y2="${n(y2)}" stroke="${color}" stroke-width="3" ${dash?'stroke-dasharray="6 5"':''}/>`;
 const text=(x,y,s,color='#29364c')=>`<text x="${n(x)}" y="${n(y)}" fill="${color}" font-size="14" text-anchor="middle">${s}</text>`;
 const dot=(x,y,label,color='#8871dc')=>`<circle cx="${n(x)}" cy="${n(y)}" r="5" fill="${color}"/>${text(x,y-13,label,color)}`;
 const P=(x,y)=>[300+x*25,165-y*25];
 function axes(){let s='';for(let i=-10;i<=10;i++){s+=line(300+i*25,20,300+i*25,310,'#e6e8f0');if(i>=-5&&i<=5)s+=line(40,165+i*25,560,165+i*25,'#e6e8f0')}return s+line(40,165,560,165,'#adb6c5')+line(300,20,300,310,'#adb6c5')+text(550,185,'x')+text(315,30,'y')+text(289,184,'0')+text(325,184,'1')}
 function graphLine(m,b,color){return line(...P(-11,m*-11+b),...P(11,m*11+b),color)}
 function stop(){cancelAnimationFrame(raf);raf=0;playing=false;last=0}
 function mount(id){stop();kind=id;const s=specs[id];if(!s)return;value=target=s[4];document.querySelector('#model-slot').innerHTML=`<section class="model animated-model geo-model"><span class="eyebrow">PREDICT · MOVE · EXPLAIN</span><h3>${s[0]}</h3><p>${s[5]}</p><div class="controls"><label for="geo-control">${s[1]} <output id="geo-value">${value}</output><input id="geo-control" type="range" min="${s[2]}" max="${s[3]}" step="${['geo-slope','geo-lines','geo-centers'].includes(id)?'.25':'1'}" value="${value}" oninput="GeoLab.set(this.value)"></label><button class="btn light" id="geo-play" aria-pressed="false" onclick="GeoLab.toggle()">Play demo</button><button class="btn light" onclick="GeoLab.reset()">Reset</button></div><div class="model-stage"><svg id="geo-svg" viewBox="0 0 600 330" role="img" aria-label="${s[0]}"></svg></div><div id="model-explain" class="output" aria-live="polite"></div><p class="mini">${reduced.matches?'Reduced motion: instant changes; autoplay is disabled.':'Smooth motion · pause anytime · use arrow keys on the slider.'} Readouts use your chosen value. Graphs are clipped to the viewing window.</p></section>`;paint();explain()}
 function set(v){playing=false;button();target=Number(v);document.getElementById('geo-value').textContent=target;explain();if(reduced.matches){value=target;paint()}else wake()}
 function button(){const b=document.getElementById('geo-play');if(b){b.textContent=playing?'Pause demo':'Play demo';b.setAttribute('aria-pressed',String(playing))}}
 function toggle(){if(reduced.matches){const e=document.getElementById('model-explain');e.innerHTML+='<p>Move the slider to explore with reduced motion.</p>';return}playing=!playing;button();wake()}
 function reset(){set(specs[kind][4]);document.getElementById('geo-control').value=target}
 function wake(){if(!raf){last=0;raf=requestAnimationFrame(frame)}}
 function frame(t){raf=0;if(!document.getElementById('geo-svg')?.isConnected){stop();return}let dt=Math.min(40,last?t-last:16);last=t;if(playing){const s=specs[kind];target+=direction*(s[3]-s[2])*dt/6500;if(target>=s[3]||target<=s[2]){direction*=-1;target=Math.max(s[2],Math.min(s[3],target))}document.getElementById('geo-control').value=target;document.getElementById('geo-value').textContent=n(target);explain()}value+=(target-value)*(1-Math.exp(-dt/100));if(Math.abs(value-target)<.005)value=target;paint();if(playing||value!==target)raf=requestAnimationFrame(frame)}
 function explain(){let v=target,s='';if(kind==='geo-radical')s=`Area = ${n(v)}² = ${n(v*v)}. √${n(v*v)} = ${n(v)}. Side lengths are nonnegative.`;
 if(kind==='geo-triangle')s=`3² + ${n(v)}² = c², so c = √${n(9+v*v)} ≈ ${n(Math.sqrt(9+v*v))}. The radical form is exact; the decimal is rounded.`;
 if(kind==='geo-quadratic'||kind==='geo-system') {let k=kind==='geo-quadratic'?-v:v;s=kind==='geo-quadratic'?`y = x² ${v<0?'−':'+'} ${n(Math.abs(v))}. `:`y = x² and y = ${n(v)}. `;s+=k<0?'No real intersections with the target horizontal line.':k===0?'One intersection at x = 0.':`Two intersections: x = ±√${n(k)} ≈ ±${n(Math.sqrt(k))}.`;if(kind==='geo-quadratic')s+=' The target line is the x-axis (y = 0).'}
 if(kind==='geo-segment')s=`AB = ${n(v/10)}, BC = ${n(10-v/10)}. AB + BC = 10 = AC.`;
 if(kind==='geo-midpoint')s=`M = ((−4 + ${n(v)})/2, (−2 + 4)/2) = (${n((v-4)/2)}, 1). AM = MB.`;
 if(kind==='geo-slope')s=`y = ${n(v)}x + 1. Run = 1, rise = ${n(v)}, so m = ${n(v)}. ${v===0?'This line is horizontal.':v>0?'The line rises left to right.':'The line falls left to right.'}`;
 if(kind==='geo-angle')s=`Whole angle = ${n(v)}°. Each bisected half = ${n(v/2)}°. ${v<90?'Acute':v===90?'Right':v<180?'Obtuse':'Straight'} angle. Its supplement is ${n(180-v)}°.`;
 if(kind==='geo-parallel')s=`Corresponding angles = ${n(v)}° each. Their linear-pair partners = ${n(180-v)}°. Same-side interior angles total 180°.`;
 if(kind==='geo-lines')s=v===0?'Original and parallel are horizontal (slope 0). The perpendicular is vertical (undefined slope).':`Original and parallel slopes = ${n(v)}. Perpendicular slope = ${n(-1/v)}. Their product is −1.`;
 if(kind==='geo-centers')s='I (green) is the incenter: equal distance to the three sides. O (purple) is the circumcenter: equal distance to all three vertices. Move the top vertex up or down. The circumcenter can move outside; the incenter stays inside.';
 document.getElementById('model-explain').textContent=s}
 function paint(){const svg=document.getElementById('geo-svg');if(!svg)return;const v=value;let s='';
 if(kind==='geo-radical'){const side=v*22,x=300-side/2,y=155-side/2;s=`<rect x="${x}" y="${y}" width="${side}" height="${side}" rx="2" fill="#d8eebc" stroke="#69894c" stroke-width="3"/>`;for(let i=1;i<v;i++)s+=line(x+i*22,y,x+i*22,y+side,'#b5cf97')+line(x,y+i*22,x+side,y+i*22,'#b5cf97');s+=text(300,300,`Side ${n(v)} · Area ${n(v*v)}`)}
 if(kind==='geo-triangle'){let a=[150,290],b=[225,290],c=[225,290-v*25];s=`<path d="M${a} L${b} L${c} Z" fill="#e7e0ff" stroke="#8871dc" stroke-width="3"/><path d="M213 290V278H225" fill="none" stroke="#29364c"/>`+text(185,315,'3')+text(250,(580-v*25)/2,n(v))+text(150,(580-v*25)/2,'c')}
 if(['geo-quadratic','geo-system','geo-slope','geo-lines','geo-midpoint'].includes(kind))s=axes();
 if(kind==='geo-quadratic'||kind==='geo-system'){let shift=kind==='geo-quadratic'?v:0,path='';for(let x=-4;x<=4;x+=.05){let p=P(x,x*x+shift);path+=(path?'L':'M')+p.join(',')}s+=`<path d="${path}" fill="none" stroke="#8871dc" stroke-width="3"/>`;let root=kind==='geo-quadratic'?-v:v;if(kind==='geo-system')s+=graphLine(0,v,'#6c9547');if(root>=0)for(const x of new Set([-Math.sqrt(root),Math.sqrt(root)]))s+=dot(...P(x,kind==='geo-system'?v:0),'');}
 if(kind==='geo-slope'){s+=graphLine(v,1,'#8871dc')+line(...P(0,1),...P(1,1),'#d38b35')+line(...P(1,1),...P(1,1+v),'#6c9547')+dot(...P(0,1),'(0,1)')+dot(...P(1,1+v),'')}
 if(kind==='geo-lines'){s+=graphLine(v,0,'#8871dc')+graphLine(v,2,'#6c9547');s+=Math.abs(v)<.001?line(...P(0,-7),...P(0,7),'#d38b35'):graphLine(-1/v,0,'#d38b35')}
 if(kind==='geo-segment'){let x=80+440*v/100;s=line(80,170,520,170)+dot(80,170,'A')+dot(x,170,'B','#6c9547')+dot(520,170,'C')+text((80+x)/2,210,'AB')+text((520+x)/2,210,'BC')}
 if(kind==='geo-midpoint'){let a=P(-4,-2),b=P(v,4),m=P((v-4)/2,1);s+=line(...a,...b)+dot(...a,'A')+dot(...b,'B')+dot(...m,'M','#6c9547')}
 if(kind==='geo-angle'){let r=v*Math.PI/180,h=r/2,o=[300,260];s=line(...o,510,260)+line(...o,300+210*Math.cos(r),260-210*Math.sin(r))+line(...o,300+190*Math.cos(h),260-190*Math.sin(h),'#6c9547','dash')+`<path d="M370 260 A70 70 0 ${v>180?1:0} 0 ${300+70*Math.cos(r)} ${260-70*Math.sin(r)}" fill="none" stroke="#d38b35" stroke-width="3"/>`+dot(...o,'V')+text(300,310,`${n(v)}° split into ${n(v/2)}° + ${n(v/2)}°`)}
 if(kind==='geo-parallel'){let dx=90/Math.tan(v*Math.PI/180),x1=300+dx/2,x2=300-dx/2;s=line(40,100,560,100,'#6c9547')+line(40,190,560,190,'#6c9547')+line(300+dx*1.5,10,300-dx*1.5,280,'#8871dc')+text(x1+35,85,`${n(v)}°`)+text(x2+35,175,`${n(v)}°`)+text(70,80,'ℓ₁ ∥ ℓ₂')}
 if(kind==='geo-centers'){
 const a=[-4,0],b=[4,0],c=[1,v],dist=(p,q)=>Math.hypot(p[0]-q[0],p[1]-q[1]);let A=dist(b,c),B=dist(a,c),C=8,per=A+B+C,I=[(A*a[0]+B*b[0]+C*c[0])/per,8*v/per],radius=8*v/per,O=[0,(v*v-15)/(2*v)],R=dist(O,a);const pp=q=>[300+q[0]*27,190-q[1]*27];s=`<circle cx="${pp(O)[0]}" cy="${pp(O)[1]}" r="${R*27}" fill="none" stroke="#ad9ce6" stroke-width="2"/><circle cx="${pp(I)[0]}" cy="${pp(I)[1]}" r="${radius*27}" fill="#d8eebc" fill-opacity=".5" stroke="#6c9547" stroke-width="2"/><path d="M${pp(a)}L${pp(b)}L${pp(c)}Z" fill="none" stroke="#29364c" stroke-width="3"/>`+line(...pp(O),...pp(a),'#ad9ce6','d')+line(...pp(I),...pp([I[0],0]),'#6c9547','d')+dot(...pp(I),'I','#6c9547')+dot(...pp(O),'O')+dot(...pp(a),'A')+dot(...pp(b),'B')+dot(...pp(c),'C')}
 svg.innerHTML=`<defs><clipPath id="geo-clip"><rect width="600" height="330"/></clipPath></defs><g clip-path="url(#geo-clip)">${s}</g>`}
 return {mount,set,toggle,reset,stop,specs};
})();
const originalModelMount=ModelLab.mount,originalModelStop=ModelLab.stop;
ModelLab.stop=function(){GeoLab.stop();originalModelStop()};
ModelLab.mount=function(id){if(id.startsWith('geo-')){ModelLab.stop();GeoLab.mount(id)}else originalModelMount(id)};
