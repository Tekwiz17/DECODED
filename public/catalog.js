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
 function render(){const e=document.getElementById('course-controls');if(!e)return;const s=subjects[subject()];e.innerHTML=`<div class="compact-course"><label for="subject-switch" class="visually-hidden">Subject</label><select id="subject-switch" aria-label="Subject" onchange="Catalog.choose(this.value)">${Object.entries(subjects).map(([id,c])=>`<option value="${id}" ${id===subject()?'selected':''}>${c.name}${id==='geometry'?' - Regents':''}</option>`).join('')}</select><label for="unit-switch" class="visually-hidden">Unit</label><select id="unit-switch" aria-label="Unit" onchange="Catalog.choose(Catalog.subject(),this.value)">${Object.entries(s.units).map(([id,name])=>`<option value="${id}" ${+id===unit()?'selected':''}>Unit ${id} · ${name}</option>`).join('')}</select><label class="compact-reading" for="reading-select">Reading <select id="reading-select" aria-label="Reading level" onchange="Reading.change(this.value)">${['easy','medium','expert'].map(level=>`<option value="${level}" ${progress.readingLevel===level?'selected':''}>${level[0].toUpperCase()+level.slice(1)}</option>`).join('')}</select></label></div>`}
 return {subjects,subject,unit,topics,accepts,choose,focus,render};
})();
