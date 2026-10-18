/* Compass-and-straightedge tutorials. Positions are computed from exact geometric relationships. */
const Construction=(()=>{
 let chosen='',step=0,timer=0,playing=false,available=[],concept='';
 const green='#568344',purple='#8670cc',orange='#c28b37',ink='#29364c';
 const titles={'copy-segment':'Copy a segment',midpoint:'Construct a midpoint','copy-angle':'Copy an angle','angle-bisector':'Bisect an angle',incircle:'Construct an incenter and incircle','parallel-corresponding':'Parallel line: corresponding angles','parallel-alternate':'Parallel line: alternate interior angles','perpendicular-on':'Perpendicular through a point on a line','perpendicular-off':'Perpendicular from a point off a line','perpendicular-bisector':'Construct a perpendicular bisector',circumcircle:'Construct a circumcenter and circumcircle'};
 const steps={
 'copy-segment':[
 ['Start with a ray','Use a straightedge to draw a ray beginning at C. The copied segment will begin here.','A ray gives the copy a starting point and direction.'],
 ['Take the original length','Place the compass point at A and its pencil at B. Keep this compass opening fixed.','The compass stores length AB without a ruler.'],
 ['Transfer that length','Move the compass point to C without changing its opening. Draw an arc crossing the new ray.','Every point on the arc is AB units from C.'],
 ['Mark the endpoint','Label the ray–arc intersection D. Segment CD is congruent to AB.','The copied radius gives CD = AB.']],
 midpoint:[
 ['Start with segment AB','The goal is its midpoint. Do not estimate the middle by eye.','A midpoint must create two congruent segments.'],
 ['Choose one compass opening','Open the compass to more than half of AB. Keep this opening for arcs from both endpoints.','This ensures the two equal-radius circles intersect twice.'],
 ['Draw arcs from A','Center the compass at A and draw an arc above and below AB.','Each arc point has the same distance from A.'],
 ['Draw matching arcs from B','Keep exactly the same opening. Center at B and cross the first arcs above and below AB.','Each intersection is equidistant from A and B.'],
 ['Join the arc intersections','Use an unmarked straightedge through P and Q. Draw their connecting line.','Two points equidistant from A and B determine the perpendicular bisector.'],
 ['Label the midpoint','Label M where that line crosses AB. AM = MB, and the crossing is 90°.','The construction locates the midpoint and the perpendicular bisector together.']],
 'copy-angle':[
 ['Draw a new base ray','The original angle has vertex O. Draw a ray beginning at P for the copy.','The new angle needs a vertex and one ray.'],
 ['Draw an arc on the original','Center at O. Draw an arc crossing both rays; label the intersections U and V.','OU and OV are the same compass radius.'],
 ['Use the same radius at P','Without changing the opening, draw an arc from P crossing the new base ray at S.','PS equals OU and OV.'],
 ['Measure the chord','Set the compass opening to UV, the distance between the two original arc marks.','This chord captures the separation of the rays at a fixed radius.'],
 ['Transfer the chord','Center the compass at S. With opening UV, cross the arc centered at P. Label the upper intersection T.','ST = UV and PT = OV; choose the intersection on the intended side.'],
 ['Complete the copied angle','Draw ray PT using a straightedge. The angle at P is congruent to the original angle at O.','The two radius sides and the chord match, so the corresponding angles match.']],
 'angle-bisector':[
 ['Start with the angle','The two rays share vertex O. The goal is two congruent angles.','An angle bisector begins at the vertex.'],
 ['Mark equal distances on the rays','Center the compass at O. Draw one arc crossing both rays at U and V.','OU = OV because both are radii of one circle.'],
 ['Draw an arc from U','Choose a compass opening large enough for the next two arcs to meet. Draw an arc inside the angle.','Keep this new opening unchanged for the next step.'],
 ['Match it from V','Center at V with the same opening. Cross the previous arc at C inside the angle.','UC = VC, and OU = OV.'],
 ['Draw the bisector','Join O to C and extend the ray. The two resulting angles are congruent.','The equal-radius construction creates matching triangles on the two sides.']],
 incircle:[
 ['Start with the triangle','We will use internal angle bisectors, not side perpendicular bisectors.','The incenter is equidistant from the sides.'],
 ['Begin the bisector at A','Draw an arc centered at A that intersects both adjacent sides.','The two marked points are equally far from A.'],
 ['Cross equal arcs','From the two marks, draw arcs with one unchanged compass opening.','Their interior intersection determines the bisector direction.'],
 ['Draw the first bisector','Draw a line from A through the new arc intersection into the triangle.','This divides angle A into congruent angles.'],
 ['Repeat at B','Repeat the same arc method at B and draw its internal angle bisector.','Two angle bisectors are enough to locate the common intersection.'],
 ['Mark the incenter I','Label the intersection I. It lies inside the triangle.','The third internal angle bisector passes through this same point.'],
 ['Set a perpendicular radius','Drop a perpendicular from I to side AB, meeting it at F. Set the compass to IF.','Distance to a side is measured perpendicularly, not to a vertex.'],
 ['Draw the incircle','Keep the compass centered at I and draw the circle with radius IF.','The circle touches all three sides because I is equally distant from them.']],
 'parallel-corresponding':[
 ['Choose a transversal','Draw a transversal from point P through the given line at A.','The transversal connects P with the line we want to parallel.'],
 ['Mark an angle at A','Use an arc centered at A to mark the angle between the rightward line ray and ray AP.','We will copy this angle in the same relative position at P.'],
 ['Use the same arc at P','Extend the transversal beyond P and draw the same-radius arc centered at P.','Corresponding angle positions use the same transversal direction.'],
 ['Transfer the chord','Transfer the original arc-mark distance onto the new arc. Mark Q to the right of P.','The same two radii and chord reproduce the angle.'],
 ['Draw the parallel','Draw line PQ through the copied angle mark.','Congruent corresponding angles establish that PQ is parallel to the given line.']],
 'parallel-alternate':[
 ['Choose a transversal','Draw the transversal through A on the given line and the external point P.','We will use alternate interior angles.'],
 ['Mark the original interior angle','At A, mark the angle between the rightward line ray and ray AP.','This angle lies between the two intended parallel lines.'],
 ['Mark an equal radius at P','At P, draw an arc crossing ray PA, directed back toward A.','The copied angle will be on the opposite side of the transversal.'],
 ['Transfer to the opposite side','Copy the original chord distance from the new transversal mark; choose Q to the left of P.','The matching angle lies inside the lines on the other side of the transversal.'],
 ['Draw the parallel','Draw the full line through P and Q.','Congruent alternate interior angles establish the parallel relationship.']],
 'perpendicular-on':[
 ['Start with P on the line','The constructed perpendicular must pass through this given point.','Do not choose a different crossing point.'],
 ['Mark equal distances from P','Center at P and draw an arc crossing the line at A and B.','PA = PB, so P is the midpoint of AB.'],
 ['Draw an arc from A','Choose an opening greater than half of AB and draw an arc above the line.','The next arc must use this same opening.'],
 ['Match the arc from B','Without changing the compass, draw an arc from B to meet the previous arc at Q.','Q is equidistant from A and B.'],
 ['Join P and Q','Draw the line through P and Q. It is perpendicular to the original line.','P and Q lie on the perpendicular bisector of AB.']],
 'perpendicular-off':[
 ['Start with P off the line','The new perpendicular must pass through P and meet the given line.','The existing point is fixed.'],
 ['Create two line intersections','Center at P. Open the compass far enough for its arc to cross the line twice, at A and B.','PA = PB because both are radii of the same circle.'],
 ['Draw an arc from A','Choose an opening large enough for arcs from A and B to intersect.','Keep the opening unchanged in the next step.'],
 ['Cross it from B','Draw the same-radius arc from B. Select an intersection Q different from P.','Both P and Q are equidistant from A and B.'],
 ['Join P to Q','Draw the full line through P and Q. Mark its intersection with the original line F.','The line is the perpendicular bisector of AB, so it makes a 90° angle at F.']],
 circumcircle:[
 ['Start with triangle ABC','We need a point equally distant from all three vertices.','Use side perpendicular bisectors; angle bisectors locate a different center.'],
 ['Use equal arcs on AB','From A and B, draw arcs with one opening greater than half of AB. Mark their intersections.','Both intersection points are equidistant from A and B.'],
 ['Draw the first perpendicular bisector','Join the two arc intersections on opposite sides of AB.','Every point on this line is equidistant from A and B.'],
 ['Repeat for AC','Use equal arcs from A and C, then join their intersections.','Every point on this second bisector is equidistant from A and C.'],
 ['Mark the circumcenter O','Label the intersection of the two perpendicular bisectors O.','OA = OB = OC. The third side perpendicular bisector also passes through O.'],
 ['Set the radius to a vertex','Center the compass at O and open it to A.','Use the distance to a vertex, not a side.'],
 ['Draw the circumcircle','Draw the circle centered at O. Check that it passes through A, B, and C.','The equal vertex distances make all three vertices lie on the same circle.']]
 };
 steps['perpendicular-bisector']=steps.midpoint.map(x=>[...x]);steps['perpendicular-bisector'][0]=['Start with segment AB','We need a line through its midpoint that also makes a 90° angle.','A general segment bisector alone does not guarantee perpendicularity.'];
 function stop(){clearTimeout(timer);timer=0;playing=false}
 function mount(ids,model){stop();available=ids;concept=model;chosen=ids[0];step=0;view()}
 function select(id){stop();chosen=id;step=0;view()}
 function move(n){stop();step=Math.max(0,Math.min(steps[chosen].length-1,step+n));view()}
 function reset(){stop();step=0;view()}
 function play(){if(playing){stop();view();return}if(step===steps[chosen].length-1)step=0;playing=true;view();schedule()}
 function schedule(){timer=setTimeout(()=>{if(!playing)return;step++;if(step>=steps[chosen].length-1){step=steps[chosen].length-1;playing=false}view();if(playing)schedule()},4300)}
 function showConcept(){stop();ModelLab.mount(concept);Reading.guide(concept);document.getElementById('model-slot').insertAdjacentHTML('beforeend',`<button class="btn light" onclick="Construction.reopen()">Back to construction steps</button>`)}
 function restore(id,n){if(!available.includes(id))return;chosen=id;step=Math.min(n,steps[id].length-1);view()}
 function hub(){main.innerHTML=`<span class="kicker">GEOMETRY A · FROM YOUR NOTES</span><h1 class="toolbox-title">Construction studio.</h1><p>Follow the compass and straightedge method, understand each step, then try it on paper.</p><div class="construction-hub">${TOPICS.filter(t=>t.constructions?.length).map(t=>`<section class="quest-card"><span class="kicker">UNIT ${t.unit} · DAY ${t.day}</span><h2>${t.title}</h2>${t.constructions.map(id=>`<a class="construction-link" href="#construct/${id}">${titles[id]} <b>→</b></a>`).join('')}<a class="mini" href="#learn/${t.id}">Open the daily lesson →</a></section>`).join('')}</div>`}
 function reopen(){stop();view()}
 const xy=p=>p.map(x=>Number(x.toFixed(3))).join(',');
 const line=(a,b,c=purple,dash=false)=>`<line x1="${a[0]}" y1="${a[1]}" x2="${b[0]}" y2="${b[1]}" stroke="${c}" stroke-width="2.5" ${dash?'stroke-dasharray="6 5"':''}/>`;
 const label=(p,t,c=ink)=>`<circle cx="${p[0]}" cy="${p[1]}" r="3.7" fill="${c}"/><text x="${p[0]+9}" y="${p[1]-8}" font-size="15" fill="${c}">${t}</text>`;
 const circle=(p,r,c=orange)=>`<circle cx="${p[0]}" cy="${p[1]}" r="${r}" fill="none" stroke="${c}" stroke-width="1.8" opacity=".7"/>`;
 const path=(p,c=purple)=>`<path d="${p}" fill="none" stroke="${c}" stroke-width="2.5"/>`;
 const norm=(a,b,r)=>{let d=Math.hypot(b[0]-a[0],b[1]-a[1]);return [a[0]+(b[0]-a[0])*r/d,a[1]+(b[1]-a[1])*r/d]};
 const arc=(o,r,a,b,c=orange)=>{const p=[o[0]+r*Math.cos(a),o[1]+r*Math.sin(a)],q=[o[0]+r*Math.cos(b),o[1]+r*Math.sin(b)];return path(`M${xy(p)} A${r} ${r} 0 ${Math.abs(b-a)>Math.PI?1:0} ${b>a?1:0} ${xy(q)}`,c)};
 function intersections(a,b,r){const d=Math.hypot(b[0]-a[0],b[1]-a[1]),m=[(a[0]+b[0])/2,(a[1]+b[1])/2],h=Math.sqrt(Math.max(0,r*r-d*d/4)),v=[-(b[1]-a[1])*h/d,(b[0]-a[0])*h/d];return [[m[0]+v[0],m[1]+v[1]],[m[0]-v[0],m[1]-v[1]]]}
 function bisector(v,a,b,phase){const u=norm(v,a,60),w=norm(v,b,60),r=55,cs=intersections(u,w,r),c=cs.sort((p,q)=>Math.hypot(q[0]-v[0],q[1]-v[1])-Math.hypot(p[0]-v[0],p[1]-v[1]))[0];let s=circle(v,60);if(phase>=1)s+=circle(u,r)+circle(w,r);if(phase>=2)s+=line(v,norm(v,c,330),green);return s}
 function perpendicularBisector(a,b,phase,r=0){r||=Math.hypot(b[0]-a[0],b[1]-a[1])*.68;let [p,q]=intersections(a,b,r);let s=circle(a,r)+circle(b,r);if(phase>=1){const mid=[(a[0]+b[0])/2,(a[1]+b[1])/2];s+=line(norm(mid,p,450),norm(mid,q,450),green)}return s}
 function diagram(){let s='',k=step;
 if(chosen==='copy-segment'){let A=[70,65],B=[230,65],C=[90,235],D=[250,235];s=line(A,B,ink)+label(A,'A')+label(B,'B')+line(C,[530,235],ink)+label(C,'C');if(k>=1)s+=line(A,B,orange,true)+arc(A,160,-.35,.35);if(k>=2)s+=arc(C,160,-1,0.45)+line(C,D,orange,true);if(k>=3)s+=line(C,D,green)+label(D,'D',green)}
 if(chosen==='midpoint'||chosen==='perpendicular-bisector'){let A=[160,175],B=[440,175],r=165,[P,Q]=intersections(A,B,r);s=line(A,B,ink)+label(A,'A')+label(B,'B');if(k>=1)s+=line(A,[325,175],orange,true);if(k>=2)s+=circle(A,r);if(k>=3)s+=circle(B,r)+label(P,'P')+label(Q,'Q');if(k>=4)s+=line([300,20],[300,335],green);if(k>=5)s+=label([300,175],'M',green)+path('M300 163h12v12',green)+line([224,170],[224,180],ink)+line([376,170],[376,180],ink)}
 if(chosen==='copy-angle'){let O=[90,150],P=[355,275],a=-55*Math.PI/180,U=[170,150],V=[O[0]+80*Math.cos(a),O[1]+80*Math.sin(a)],S=[435,275],T=[P[0]+80*Math.cos(a),P[1]+80*Math.sin(a)],d=Math.hypot(U[0]-V[0],U[1]-V[1]);s=line(O,[265,150],ink)+line(O,norm(O,V,145),ink)+label(O,'O')+line(P,[570,275],ink)+label(P,'P');if(k>=1)s+=arc(O,80,-1.2,.2)+label(U,'U')+label(V,'V');if(k>=2)s+=arc(P,80,-1.2,.2)+label(S,'S');if(k>=3)s+=line(U,V,orange,true);if(k>=4)s+=circle(S,d)+label(T,'T',green);if(k>=5)s+=line(P,norm(P,T,210),green)}
 if(chosen==='angle-bisector'){const O=[165,280],a=[455,280],b=[335,35],U=norm(O,a,100),V=norm(O,b,100),cs=intersections(U,V,90),C=cs.sort((p,q)=>Math.hypot(q[0]-O[0],q[1]-O[1])-Math.hypot(p[0]-O[0],p[1]-O[1]))[0];s=line(O,a,ink)+line(O,b,ink)+label(O,'O');if(k>=1)s+=arc(O,100,-1.25,.15)+label(U,'U')+label(V,'V');if(k>=2)s+=circle(U,90);if(k>=3)s+=circle(V,90)+label(C,'C',green);if(k>=4)s+=line(O,norm(O,C,310),green)}
 if(chosen==='incircle'){const A=[125,280],B=[475,280],C=[270,45],a=Math.hypot(B[0]-C[0],B[1]-C[1]),b=Math.hypot(A[0]-C[0],A[1]-C[1]),c=350,per=a+b+c,I=[(a*A[0]+b*B[0]+c*C[0])/per,(a*A[1]+b*B[1]+c*C[1])/per],r=280-I[1],F=[I[0],280];s=path(`M${xy(A)}L${xy(B)}L${xy(C)}Z`,ink)+label(A,'A')+label(B,'B')+label(C,'C');if(k>=1)s+=bisector(A,B,C,Math.min(2,k-1));if(k>=4)s+=bisector(B,A,C,2);if(k>=5)s+=label(I,'I',green);if(k>=6)s+=line(I,F,green,true)+label(F,'F')+path(`M${F[0]-10} 280v-10h10`,green);if(k>=7)s+=circle(I,r,green)}
 if(chosen.startsWith('parallel-')){const A=[220,270],P=[350,105],ang=Math.atan2(P[1]-A[1],P[0]-A[0]),r=65,U=[A[0]+r,A[1]],V=norm(A,P,r),alt=chosen==='parallel-alternate',W=alt?norm(P,A,r):norm(P,[480,-60],r),Q=[P[0]+(alt?-r:r),P[1]],d=Math.hypot(U[0]-V[0],U[1]-V[1]);s=line([55,270],[565,270],ink)+line(norm(A,P,-70),norm(A,P,290),ink)+label(A,'A')+label(P,'P',green);if(k>=1)s+=arc(A,r,ang-.16,.15)+label(U,'U')+label(V,'V');if(k>=2)s+=alt?arc(P,r,ang+Math.PI-.15,Math.PI+.15):arc(P,r,ang-.2,.15);if(k>=2)s+=label(W,'S');if(k>=3)s+=circle(W,d)+label(Q,'Q',green);if(k>=4)s+=line([55,105],[565,105],green)}
 if(chosen==='perpendicular-on'||chosen==='perpendicular-off'){const off=chosen==='perpendicular-off',P=[300,off?65:205],A=[170,205],B=[430,205],r=170,[u,v]=intersections(A,B,r),Q=off?u:v;s=line([50,205],[550,205],ink)+label(P,'P',purple);if(k>=1)s+=circle(P,Math.hypot(P[0]-A[0],P[1]-A[1]))+label(A,'A')+label(B,'B');if(k>=2)s+=circle(A,r);if(k>=3)s+=circle(B,r)+label(Q,'Q',green);if(k>=4)s+=line([300,20],[300,330],green)+path('M300 193h12v12',green)+(off?label([300,205],'F'):'')}
 if(chosen==='circumcircle'){const A=[165,235],B=[435,235],C=[285,60],O=[300,235+((C[0]-300)**2+(C[1]-235)**2-135**2)/(2*(C[1]-235))],r=Math.hypot(O[0]-A[0],O[1]-A[1]);s=path(`M${xy(A)}L${xy(B)}L${xy(C)}Z`,ink)+label(A,'A')+label(B,'B')+label(C,'C');if(k>=1)s+=perpendicularBisector(A,B,k>=2?1:0);if(k>=3)s+=perpendicularBisector(A,C,1);if(k>=4)s+=label(O,'O',green);if(k>=5)s+=line(O,A,orange,true);if(k>=6)s+=circle(O,r,green)}
 return `<svg viewBox="0 0 600 350" role="img" aria-label="${titles[chosen]} — step ${k+1}: ${steps[chosen][k][0]}"><defs><clipPath id="construction-clip"><rect width="600" height="350"/></clipPath></defs><g class="construction-reveal" clip-path="url(#construction-clip)">${s}</g></svg>`}
 function view(){const list=steps[chosen],item=list[step],e=document.getElementById('model-slot');if(!e)return;e.innerHTML=`<section class="construction-studio"><div class="construction-top"><span class="kicker">COMPASS + STRAIGHTEDGE STUDIO</span><h2>Build it. See why it works.</h2><label for="construction-select">Construction</label><select id="construction-select" onchange="Construction.select(this.value)">${available.map(id=>`<option value="${id}" ${id===chosen?'selected':''}>${titles[id]}</option>`).join('')}</select></div><div class="construction-layout"><div class="construction-drawing">${diagram()}<div class="construction-key"><span>● Given figure</span><span>● Compass arcs</span><span>● Constructed result</span></div><p class="mini">${step+1}/${list.length} · Keep the compass opening fixed whenever the instructions say to. No ruler measurements or protractor are needed.</p></div><div class="construction-instructions"><span class="step-tag">STEP ${step+1} OF ${list.length}</span><h3>${item[0]}</h3><p>${item[1]}</p><details open><summary>Why this step works</summary><p>${item[2]}</p></details><div class="construction-nav"><button class="btn light" ${step===0?'disabled':''} onclick="Construction.move(-1)">← Back</button><button class="btn" ${step===list.length-1?'disabled':''} onclick="Construction.move(1)">Next step →</button></div><div class="actions"><button class="text-button" onclick="Construction.reset()">Start again</button><button class="text-button" aria-pressed="${playing}" onclick="Construction.play()">${playing?'Pause replay':'Auto replay'}</button></div></div></div><details class="construction-practice"><summary>Your turn: construct it on paper</summary><ol><li>Use a compass and an unmarked straightedge. Draw the given figure.</li><li>Hide the instructions and complete the construction. Leave your arcs visible.</li><li>Explain which distances or angles are equal, and why.</li><li>Replay the steps to check your work. A sketch that only looks correct is not enough.</li></ol><p><b>Check your reasoning:</b> ${list[list.length-1][2]}</p></details><button class="btn light" onclick="Construction.showConcept()">Explore the related concept model →</button></section>`}
 return {mount,hub,restore,select,move,reset,play,stop,showConcept,reopen,titles,steps,diagram,get current(){return chosen},get step(){return step}};
})();
const stopBeforeConstruction=ModelLab.stop;ModelLab.stop=function(){Construction.stop();stopBeforeConstruction()};
