const fs=require('fs'),vm=require('vm'),assert=require('assert');const els=new Map();function el(s){if(!els.has(s))els.set(s,{innerHTML:'',textContent:'',value:s==='#p1'||s==='#p2'?'Aa':'7',selectedIndex:0,checked:true,style:{},classList:{toggle(){}},querySelector(){return el('button')},querySelectorAll(){return []},nextElementSibling:{querySelector(){return el('next')}}});return els.get(s)}const ctx={console,document:{querySelector:el,querySelectorAll:()=>[]},localStorage:{getItem:()=>null,setItem(){}},location:{hash:'#home'},window:{scrollTo(){},addEventListener(){}}};vm.createContext(ctx);vm.runInContext(fs.readFileSync('dist/content.js','utf8')+fs.readFileSync('dist/app.js','utf8'),ctx);vm.runInContext(`
assertCount=TOPICS.length;
for(const t of TOPICS){lesson(t.id);if(!document.querySelector('main').innerHTML.includes(t.title))throw Error('Lesson missing');}
for(const m of ['water','ph','building','families','protein']){document.querySelector('#p1').value='Aa';document.querySelector('#p2').value='Aa';renderModel(m)}
for(let n=0;n<5;n++)protein(n);
for(let n=0;n<15;n++)chain(1);chain(-1);
for(const q of QUESTIONS){if(!TOPICS.some(t=>t.id===q.topic)||!q.options[q.answer]||!q.why)throw Error('Invalid question')}
cards();document.querySelector('#cardfilter').value='all';startDeck();flip();know(true);
practice();document.querySelector('#qfilter').value='all';startQuiz(false);for(let n=0;n<quiz.length;n++){choose(quiz[qi].answer);checkAnswer();checkAnswer()}
if(progress.missed.length)throw Error('Correct answers marked wrong');
mode='test';startQuiz(false);for(let n=0;n<quiz.length;n++){choose((quiz[qi].answer+1)%4);checkAnswer()}
if(!progress.missed.length)throw Error('Wrong answers not retained');
sources();
console.log(TOPICS.length+' lessons, '+CARDS.length+' flashcards, '+QUESTIONS.length+' questions validated; all models and both quiz flows executed.');`,ctx);
