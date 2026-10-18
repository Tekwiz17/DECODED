const fs=require('fs'),vm=require('vm'),assert=require('assert');
const els=new Map(),frames=new Map();let frameId=0,now=0;
function el(s){if(!els.has(s))els.set(s,{innerHTML:'',textContent:'',value:s==='#distance'?'35':s==='#ph'?'7':'all',selectedIndex:0,checked:true,isConnected:true,style:{},attributes:{},setAttribute(k,v){this.attributes[k]=String(v)},classList:{toggle(){}},insertAdjacentHTML(_,html){this.innerHTML+=html},querySelector(){return el('button')},querySelectorAll(){return []},nextElementSibling:{querySelector(){return el('next')}}});return els.get(s)}
function flush(){for(let j=0;j<140&&frames.size;j++){now+=16;const batch=[...frames];frames.clear();for(const [,fn]of batch)fn(now)}}
const media={matches:false,addEventListener(){}};
const ctx={console,document:{getElementById:id=>el('#'+id),querySelector:el,querySelectorAll:()=>[]},localStorage:{getItem:()=>null,setItem(){}},requestAnimationFrame:fn=>{frames.set(++frameId,fn);return frameId},cancelAnimationFrame:id=>frames.delete(id),location:{hash:'#home'},window:{matchMedia:()=>media,scrollTo(){},addEventListener(){}}};
vm.createContext(ctx);vm.runInContext(['content.js','models.js','app.js','decoded.js'].map(p=>fs.readFileSync('public/'+p,'utf8')).join('\n'),ctx);
function run(s){return vm.runInContext(s,ctx)}
run(`for(const t of TOPICS){lesson(t.id);if(!document.querySelector('main').innerHTML.includes(t.title))throw Error('Lesson missing')};ModelLab.stop()`);
run(`ModelLab.mount('protein');ModelLab.protein(2)`);flush();const folded=el('#md0').attributes.cx;run('ModelLab.protein(4)');flush();assert.notEqual(el('#md0').attributes.cx,folded);run('ModelLab.protein(3)');flush();assert.equal(el('#md28').attributes.opacity,'1');run('ModelLab.protein(0)');flush();assert.equal(el('#md28').attributes.opacity,'0');
run(`ModelLab.mount('building');for(let i=0;i<15;i++)ModelLab.chain(1)`);flush();assert(el('#model-explain').innerHTML.includes('8 building blocks'));assert(el('#join').disabled);run(`for(let i=0;i<15;i++)ModelLab.chain(-1)`);flush();assert(el('#model-explain').innerHTML.includes('1 building block'));assert(el('#split').disabled);
run(`ModelLab.mount('water');ModelLab.toggle()`);el('#distance').value='0';run('ModelLab.water()');flush();const close=el('#wb').attributes.transform;el('#distance').value='100';run('ModelLab.water()');flush();assert.notEqual(el('#wb').attributes.transform,close);
run(`ModelLab.mount('ph');ModelLab.toggle()`);el('#ph').value='3';run('ModelLab.ph()');assert(el('#model-explain').innerHTML.includes('10,000 times more'));el('#ph').value='9';run('ModelLab.ph()');assert(el('#model-explain').innerHTML.includes('100 times less'));
run(`ModelLab.mount('families')`);for(let n=0;n<4;n++){el('#family').selectedIndex=n;run('ModelLab.family()');flush();assert(el('#model-explain').innerHTML.length>100)}
run('ModelLab.stop()');assert.equal(frames.size,0);media.matches=true;run(`ModelLab.mount('protein');ModelLab.protein(2)`);assert.equal(el('#md0').attributes.cx,'350');run('ModelLab.stop()');
run(`for(const t of TOPICS){startJourney(t.id);while(journey.stage==='learn')journeyNext();journeyNext();while(journey.qindex<journey.questions.length){journeyChoose(journey.questions[journey.qindex].answer);journeyCheck();if(journey.qindex===journey.questions.length-1){journeyCheck();break}journeyCheck()}};if(progress.xp!==100||progress.done.length!==5)throw Error('Lesson rewards failed');if(award(20,'lesson:water')!==0)throw Error('Duplicate XP');
for(const q of QUESTIONS){if(!TOPICS.some(t=>t.id===q.topic)||!q.options[q.answer]||!q.why)throw Error('Invalid question')}
cards();document.querySelector('#cardfilter').value='all';startDeck();flip();know(true);
practice();document.querySelector('#qfilter').value='all';startQuiz(false);for(let n=0;n<quiz.length;n++){choose(quiz[qi].answer);checkAnswer();checkAnswer()}
if(progress.missed.length)throw Error('Correct answers marked wrong');
mode='test';startQuiz(false);for(let n=0;n<quiz.length;n++){choose((quiz[qi].answer+1)%4);checkAnswer()}
if(!progress.missed.length)throw Error('Wrong answers not retained');
sources();console.log(TOPICS.length+' lessons, '+CARDS.length+' flashcards, '+QUESTIONS.length+' questions; animation endpoints, model limits, pause, cleanup, reduced motion, and both quiz flows passed.');`);
