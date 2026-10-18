/* Stable topic and card identities keep Biology progress unchanged as courses grow. */
const Catalog=(()=>{
 const subjects={biology:{name:'Biology A - Regents',icon:'✳',units:{2:'Chemistry of life'}},geometry:{name:'Geometry A',icon:'◇',units:{1:'Radicals & right triangles',2:'Quadratics & systems',3:'Coordinates & segments',4:'Angles, lines & constructions'}}};
 for(const t of TOPICS){t.subject||='biology';t.unit||=2}
 function subject(){return subjects[progress?.subject]?progress.subject:'biology'}
 function unit(){const s=subjects[subject()];return s.units[progress?.unit]?Number(progress.unit):Number(Object.keys(s.units)[0])}
 function topics(){return TOPICS.filter(t=>t.subject===subject()&&t.unit===unit())}
 function accepts(id){return topics().some(t=>t.id===id)}
 function choose(s,u){if(!subjects[s])return;ModelLab.stop();journey=null;progress.subject=s;progress.unit=subjects[s].units[u]?Number(u):Number(Object.keys(subjects[s].units)[0]);save();if(location.hash==='#path')route();else location.hash='path'}
 function focus(id){const t=TOPICS.find(t=>t.id===id||t.model===id);if(t){progress.subject=t.subject;progress.unit=t.unit}}
 function render(){const e=document.getElementById('course-controls');if(!e)return;const s=subjects[subject()];e.innerHTML=`<div class="course-switch"><label>Subject <select id="subject-switch" onchange="Catalog.choose(this.value)">${Object.entries(subjects).map(([id,c])=>`<option value="${id}" ${id===subject()?'selected':''}>${c.icon} ${c.name}${id==='geometry'?' · Regents':''}</option>`).join('')}</select></label><label>Unit <select id="unit-switch" onchange="Catalog.choose(Catalog.subject(),this.value)">${Object.entries(s.units).map(([id,name])=>`<option value="${id}" ${+id===unit()?'selected':''}>Unit ${id} · ${name}</option>`).join('')}</select></label><a href="#path">Open learning path →</a></div>`}
 return {subjects,subject,unit,topics,accepts,choose,focus,render};
})();
