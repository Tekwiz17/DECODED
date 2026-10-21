"""Compile authored NY paths, verified source links, and assessment metadata."""
import json,runpy
from pathlib import Path
root=Path('curriculum/research')
C=runpy.run_path('curriculum/author.py')['COURSES'];alignment=json.loads((root/'unit-alignment.json').read_text());standards=json.loads((root/'standards-map.json').read_text());exams=json.loads((root/'exam-mapped.json').read_text())
modelmap={'biology':{2:['osmosis','enzyme'],3:['photosynthesis'],6:['inheritance'],8:['population']},'earth':{3:['sunlight'],5:['plates'],8:['albedo']},'chemistry':{2:['decay'],6:['gas'],7:['reaction']},'physics':{2:['force'],4:['impulse'],6:['wave'],7:['circuit']}}
source_meta={};manifest={'courses':{},'lessons':[],'cards':[],'models':[],'examItems':[]};catalog=[]
for c in C:
 id=c['id'];s=standards[id];c['framework']=s['framework'];c['sources']=s['sources'];c['sequenceNote']=s['sequenceNote'];c['alignmentNote']='Standards-family mapping and course-spanning study sequence; not a claim that every performance expectation is fully assessed.'
 for u in c['units']:
  a=alignment[id];u['standards']=a.get(u['id'],[]) if isinstance(a,dict)else[]
  u['models']=modelmap.get(id,{}).get(u['number'],[])
  for l in u['lessons']:
   l['unitId']=u['id'];l['courseId']=id
   manifest['lessons'].append(l['id'])
   for j,v in enumerate(l['vocab']):v['id']=l['id']+'-v'+str(j);v['unitId']=u['id'];manifest['cards'].append(v['id'])
  for m in u['models']:manifest['models'].append(m)
 paper=exams[id]
 for x in paper['items']:
  keys=x.get('unitIds',[x['unitId']]);new=[]
  for k in keys:
   n=int(k.split('-u')[1])
   if id=='global'and n>=9:n+=1
   if id=='ela'and n==8:n=9
   new.append(f'{id}-u{n}')
  x['unitIds']=new;x['unitId']=new[0];x['id']=f"{id}-2026-{'06' if id=='physics' else '08'}-q{x['number']}"
  manifest['examItems'].append(x['id'])
 c['exam']=paper
 path=Path('curriculum/courses');path.mkdir(exist_ok=True);(path/(id+'.json')).write_text(json.dumps(c,ensure_ascii=False,separators=(',',':'))+'\n')
 manifest['courses'][id]={'units':[u['id']for u in c['units']],'lessons':[l['id']for u in c['units']for l in u['lessons']]}
 catalog.append({k:c[k]for k in ['id','title','group','description','state','framework','sources','sequenceNote','alignmentNote']}|{'units':[{'id':u['id'],'number':u['number'],'title':u['title'],'standards':u['standards'],'lessons':len(u['lessons']),'models':u['models']}for u in c['units']],'lessonCount':len(manifest['courses'][id]['lessons']),'examCount':len(paper['items'])})
Path('public/catalog.json').write_text(json.dumps({'version':3,'state':'NY','stateName':'New York','verified':'2026-10-19','courses':catalog},ensure_ascii=False,separators=(',',':'))+'\n')
Path('lib/learning-manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
Path('curriculum/source-notes.json').write_text(json.dumps({'reviewed':'2026-10-19','basis':standards,'examNotes':{k:v['notes']for k,v in exams.items()},'limitations':['Suggested study order is DECODED’s, not a state-mandated unit order.','Individual performance-expectation alignment and classroom case-study depth need further review.','Exam item index is selected, not every historical paper; source documents remain on NYSED.','Digital models do not replace required classroom investigations or teacher evaluation.']},ensure_ascii=False,indent=2)+'\n')
print(len(C),'courses;',len(manifest['lessons']),'lessons;',len(manifest['cards']),'term cards;',len(manifest['examItems']),'exam items')

runpy.run_path('curriculum/expand.py',init_globals={'base_courses':C})
