import json,runpy
from pathlib import Path
C=base_courses+runpy.run_path('curriculum/grade-paths.py')['COURSES'];grades={'algebra1':[9],'geometry':[10],'algebra2':[11],'biology':[9,10],'earth':[9,10],'chemistry':[10,11],'physics':[11,12],'global':[10],'us':[11],'ela':[9,10,11,12]};M={'courses':{},'lessons':[],'cards':[],'models':[],'examItems':[]};cat=[]
for c in C:
 cid=c['id'];c.setdefault('grades',grades.get(cid,[]));c.setdefault('levelLabel','Grade '+ '–'.join(map(str,sorted(set([min(c['grades']),max(c['grades'])])))))
 if cid=='biology':c['title']='Biology A – Regents'
 if cid=='geometry':c['title']='Geometry A – Regents'
 for u in c['units']:
  M['models']+=u['models']
  for l in u['lessons']:
   M['lessons'].append(l['id']);M['cards'] +=[v['id']for v in l['vocab']]
 M['courses'][cid]={'units':[u['id']for u in c['units']],'lessons':[l['id']for u in c['units']for l in u['lessons']]}
 if c['exam']:M['examItems'] +=[i['id']for i in c['exam']['items']]
 Path('curriculum/courses/'+cid+'.json').write_text(json.dumps(c,ensure_ascii=False,separators=(',',':'))+'\n')
 cat.append({k:c[k]for k in ['id','title','group','description','state','grades','levelLabel','framework','sources','sequenceNote','alignmentNote']}|{'lessonCount':len(M['courses'][cid]['lessons']),'examCount':len(c['exam']['items'])if c['exam']else 0,'units':[{k:u[k]for k in ['id','title','number','standards','models']}|{'lessons':len(u['lessons']),'lessonIndex':[{'id':l['id'],'title':l['title'],'terms':[v['term']for v in l['vocab']]}for l in u['lessons']]}for u in c['units']]})
Path('public/catalog.json').write_text(json.dumps({'version':4,'state':'NY','stateName':'New York','courses':cat},ensure_ascii=False,separators=(',',':'))+'\n');Path('lib/learning-manifest.json').write_text(json.dumps(M,indent=2)+'\n')
f=Path('app/api/course/route.ts');s=f.read_text();s=s[s.index('export const dynamic'):];f.write_text("import {getChatGPTUser} from '../../chatgpt-auth';\n"+'\n'.join("import c%d from '../../../curriculum/courses/%s.json';"%(i,c['id'])for i,c in enumerate(C))+'\nconst all:Record<string,unknown>={'+','.join(json.dumps(c['id'])+':c'+str(i)for i,c in enumerate(C))+'};\n'+s)
print(len(C),'courses',len(M['lessons']),'lessons',len(M['cards']),'terms')
