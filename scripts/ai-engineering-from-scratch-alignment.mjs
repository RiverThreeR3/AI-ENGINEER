import {readFileSync} from 'node:fs';
import {pathToFileURL} from 'node:url';
const IDS=Array.from({length:20},(_,i)=>String(i).padStart(2,'0'));
const TRACKS=new Set(Array.from({length:11},(_,i)=>String(i+1).padStart(2,'0')));
export function checkCurriculum(c){
  if(!c||c.schema_version!==1||c.upstream!=='rohitg00/ai-engineering-from-scratch'||
     c.course_total_lessons!==542||c.course_total_phases!==20||
     !Array.isArray(c.phases)||c.phases.length!==20)
    throw new Error('invalid_upstream_curriculum_version');
  const phases=new Set();
  let lessons=0;
  for(const p of c.phases){
    if(!p||typeof p.phase!=='string'||!IDS.includes(p.phase)||phases.has(p.phase)||
       typeof p.name!=='string'||p.name.trim().length<3||
       !Number.isInteger(p.lesson_count)||p.lesson_count<=0||
       !Array.isArray(p.local_track_ids)||
       p.local_track_ids.some(x=>!TRACKS.has(x))||
       new Set(p.local_track_ids).size!==p.local_track_ids.length)
      throw new Error('invalid_upstream_phase');
    phases.add(p.phase);
    lessons+=p.lesson_count;
  }
  if(lessons!==542)throw new Error('upstream_lesson_count_mismatch');
  return Object.freeze({phases:phases.size,lessons,
    mapped: c.phases.filter(x=>x.local_track_ids.length>0).length,
    optional: c.phases.filter(x=>!x.local_track_ids.length).map(x=>x.phase),
    sourceDate:c.source_checked_at,
    personalLearningProgress:'NÃO VERIFICADO — acompanhamento pessoal privado'
  });
}

if(process.argv[1]&&import.meta.url===pathToFileURL(process.argv[1]).href){
  const source=JSON.parse(readFileSync(
    new URL('../data/ai-engineering-from-scratch-curriculum.json',import.meta.url),'utf8'
  ));
  const s=checkCurriculum(source);
  console.log(`AI ENGINEERING FROM SCRATCH — Referência: ${s.phases} fases / ${s.lessons} aulas`);
  console.log(`Fases com ligação ao portfólio: ${s.mapped}/${s.phases}; sem trilha direta: ${s.optional.join(',')}`);
  console.log(`Conclusão pessoal das aulas: ${s.personalLearningProgress}`);
}
