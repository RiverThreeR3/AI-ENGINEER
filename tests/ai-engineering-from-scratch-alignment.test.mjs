import test from 'node:test';
import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';
import {checkCurriculum} from '../scripts/ai-engineering-from-scratch-alignment.mjs';
const base=JSON.parse(readFileSync(
  new URL('../data/ai-engineering-from-scratch-curriculum.json',import.meta.url),'utf8'
));
const copy=()=>structuredClone(base);
test('20 upstream phases account for exactly 542 course lessons',()=>{
  const result=checkCurriculum(base);
  assert.equal(result.phases,20);
  assert.equal(result.lessons,542);
  assert.equal(result.mapped,17);
  assert.deepEqual(result.optional,['06','09','12']);
  assert.match(result.personalLearningProgress,/NÃO VERIFICADO/);
});
test('course phases cannot be confused with 11 local engineering tracks',()=>{
  assert.equal(base.phases.length,20);
  assert.equal(base.course_total_phases,20);
  assert.equal(new Set(base.phases.flatMap(x=>x.local_track_ids)).size,11);
  assert.ok(!JSON.stringify(base).includes('lessonCompletion'));
  assert.ok(!JSON.stringify(base).includes('learnerEmail'));
});
test('broken counts, duplicate phases and unknown track links fail closed',()=>{
  const a=copy();a.phases[0].lesson_count=999;
  assert.throws(()=>checkCurriculum(a),/upstream_lesson_count_mismatch/);
  const b=copy();b.phases[0].phase='01';
  assert.throws(()=>checkCurriculum(b),/invalid_upstream_phase/);
  const c=copy();c.phases[3].local_track_ids.push('99');
  assert.throws(()=>checkCurriculum(c),/invalid_upstream_phase/);
  const d=copy();d.course_total_phases=11;
  assert.throws(()=>checkCurriculum(d),/invalid_upstream_curriculum_version/);
});
