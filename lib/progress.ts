import catalog from "./course-catalog.json";
const topicQuestions:Record<string,number[]>=Object.fromEntries(Object.entries(catalog.topics).map(([id,t])=>[id,t.questions]));
const ids=new Set(Object.keys(topicQuestions));
const date=(v:unknown):v is string=>typeof v==='string'&&/^\d{4}-\d{2}-\d{2}$/.test(v);
const bounded=(v:unknown,max:number)=>typeof v==='number'&&Number.isFinite(v)?Math.max(0,Math.min(max,Math.floor(v))):0;
const list=(v:unknown,max:number)=>Array.isArray(v)?[...new Set(v.filter(n=>Number.isInteger(n)&&n>=0&&n<max))]:[];
export function cleanProgress(p:unknown){
 if(!p||typeof p!=='object'||Array.isArray(p))return null;
 const x=p as Record<string,unknown>;
 const done=Array.isArray(x.done)?[...new Set(x.done.filter(n=>typeof n==='string'&&ids.has(n)))]:[];
 const days=Array.isArray(x.days)?[...new Set(x.days.filter(date))].sort().slice(-366):[];
 const review:Record<string,{due:string,last:string,streak:number}>={};
 if(x.review&&typeof x.review==='object'&&!Array.isArray(x.review)){
  for(const [id,value]of Object.entries(x.review).slice(0,catalog.cards)){
   if(!/^\d+$/.test(id)||Number(id)>=catalog.cards||!value||typeof value!=='object')continue;
   const v=value as Record<string,unknown>;
   if(date(v.due)&&date(v.last))review[id]={due:v.due,last:v.last,streak:bounded(v.streak,4)};
  }
 }
 let resume=null;
 if(x.resume&&typeof x.resume==='object'&&!Array.isArray(x.resume)){
  const r=x.resume as Record<string,unknown>;
  if(typeof r.id==='string'&&ids.has(r.id)&&['learn','model','question'].includes(String(r.stage))&&Array.isArray(r.questionIds)&&r.questionIds.length>0&&r.questionIds.length<=3&&r.questionIds.every(n=>Number.isInteger(n)&&topicQuestions[r.id as string].includes(n))){
   const partMax:Record<string,number>=Object.fromEntries(Object.entries(catalog.topics).map(([id,t])=>[id,t.partMax]));
   const questionIds=[...new Set(r.questionIds)];
   const selected=Number.isInteger(r.selected)&&Number(r.selected)>=0&&Number(r.selected)<4?r.selected as number:null;
   resume={id:r.id,stage:r.stage,part:bounded(r.part,partMax[r.id]),qindex:bounded(r.qindex,questionIds.length-1),questionIds,selected,revealed:r.revealed===true&&selected!==null,firstTry:bounded(r.firstTry,3),missed:list(r.missed,catalog.questions).filter(id=>topicQuestions[r.id as string].includes(id))};
  }
 }
 return {lessonSchema:x.lessonSchema===2?2:1,flashcardSchema:x.flashcardSchema===2?2:1,subject:x.subject==='geometry'?'geometry':'biology',unit:x.subject==='geometry'&&[1,2,3,4].includes(Number(x.unit))?Number(x.unit):x.subject==='geometry'?1:2,review,resume,readingLevel:['easy','medium','expert'].includes(String(x.readingLevel))?String(x.readingLevel):'medium',done,known:list(x.known,catalog.cards),missed:list(x.missed,catalog.questions),xp:bounded(x.xp,1000000),days,goal:[10,20,30].includes(Number(x.goal))?Number(x.goal):20,daily:bounded(x.daily,100000),dailyDate:date(x.dailyDate)?x.dailyDate:'',awards:Array.isArray(x.awards)?[...new Set(x.awards.filter(a=>typeof a==='string'&&/^(lesson|practice):[a-z0-9-]{1,30}$/.test(a)))].slice(-100):[]};
}
