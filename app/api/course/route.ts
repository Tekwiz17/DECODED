import {getChatGPTUser} from '../../chatgpt-auth';
import algebra1 from '../../../curriculum/courses/algebra1.json';
import geometry from '../../../curriculum/courses/geometry.json';
import algebra2 from '../../../curriculum/courses/algebra2.json';
import biology from '../../../curriculum/courses/biology.json';
import earth from '../../../curriculum/courses/earth.json';
import chemistry from '../../../curriculum/courses/chemistry.json';
import physics from '../../../curriculum/courses/physics.json';
import ela from '../../../curriculum/courses/ela.json';
import globalHistory from '../../../curriculum/courses/global.json';
import us from '../../../curriculum/courses/us.json';
const all:Record<string,unknown>={algebra1,geometry,algebra2,biology,earth,chemistry,physics,ela,global:globalHistory,us};
export const dynamic='force-dynamic';
export async function GET(req:Request){if(!await getChatGPTUser())return Response.json({error:'Sign in to learn.'},{status:401,headers:{'Cache-Control':'no-store'}});const id=new URL(req.url).searchParams.get('id')||'';if(!Object.hasOwn(all,id))return Response.json({error:'Unknown course'},{status:404});return Response.json(all[id],{headers:{'Cache-Control':'private, no-store','Vary':'Cookie'}})}
