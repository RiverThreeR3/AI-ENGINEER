import {readFileSync} from 'node:fs';
import {pathToFileURL} from 'node:url';

const GATES=Object.freeze([
  'implementation','tests_ci','evaluation','security','reproducibility','demo'
]);
const STATUS=new Set(['PENDING','BLOCKED','FAILED','VERIFIED']);
const FULL_SHA=/^[a-f0-9]{40}$/i;

function validEvidence(e){
  if(!e||typeof e!=='object'||Array.isArray(e))return false;
  try{
    const u=new URL(e.url);
    if(u.protocol!=='https:'||!(u.hostname==='github.com'||u.hostname.endsWith('.github.com')))return false;
  }catch{return false}
  return FULL_SHA.test(e.commit||'')&&
    e.result==='PASS'&&
    typeof e.reviewedAt==='string'&&!Number.isNaN(Date.parse(e.reviewedAt))&&
    typeof e.note==='string'&&e.note.trim().length>=12;
}

/**
 * A ledger is a record of manually verified evidence, not a live GitHub
 * attestation. CI results and proof links MUST be checked independently.
 */
export function summarizeProgress(ledger){
  if(!ledger||ledger.schema_version!==1||
      ledger.repository!=='RiverThreeR3/AIEngineer'||
      !Array.isArray(ledger.tracks)||ledger.tracks.length!==11||
      JSON.stringify(ledger.gates)!==JSON.stringify(GATES))
    throw new Error('invalid_ai_engineer_ledger');
  let verified=0,completedTracks=0;
  const ids=new Set();
  for(const track of ledger.tracks){
    if(!track||typeof track.name!=='string'||track.name.trim().length<3||
      !/^(0[1-9]|1[01])$/.test(track.id)||ids.has(track.id)||
      !track.gates||Object.keys(track.gates).length!==GATES.length)
      throw new Error('invalid_ai_engineer_track');
    ids.add(track.id);
    let verifiedInTrack=0;
    for(const name of GATES){
      const gate=track.gates[name];
      if(!gate||!STATUS.has(gate.status)||!Array.isArray(gate.evidence))
        throw new Error('invalid_ai_engineer_gate');
      if(gate.status==='VERIFIED'){
        if(gate.evidence.length===0||!gate.evidence.every(validEvidence))
          throw new Error('verified_gate_without_reviewable_evidence');
        verified++;verifiedInTrack++;
      }
    }
    if(verifiedInTrack===GATES.length)completedTracks++;
  }
  const total=11*GATES.length;
  const percent=Number((verified*100/total).toFixed(1));
  const filled=Math.floor(percent/5);
  const meter='█'.repeat(filled)+'░'.repeat(20-filled);
  return Object.freeze({
    percent,verified,total,remaining:total-verified,
    completedTracks,totalTracks:11,remainingTracks:11-completedTracks,
    meter,status:verified===total?'ZERADO / 100%':'EM ANDAMENTO',
    sourceDate:ledger.as_of
  });
}

export function renderProgress(summary){
  return [
    `AI ENGINEER | ${summary.meter} ${summary.percent.toFixed(1)}%`,
    `Critérios verificados: ${summary.verified}/${summary.total} | Pendentes: ${summary.remaining}`,
    `Trilhas concluídas: ${summary.completedTracks}/${summary.totalTracks} | Restam: ${summary.remainingTracks}`,
    `Estado: ${summary.status} | Base: ${summary.sourceDate}`
  ].join('\n');
}

if(process.argv[1]&&import.meta.url===pathToFileURL(process.argv[1]).href){
  const ledger=JSON.parse(readFileSync(
    new URL('../data/ai-engineer-progress.json',import.meta.url),'utf8'
  ));
  process.stdout.write(renderProgress(summarizeProgress(ledger))+'\n');
}
