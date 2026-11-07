import test from 'node:test';
import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';
import {summarizeProgress,renderProgress} from '../scripts/ai-engineer-progress.mjs';

const source=JSON.parse(readFileSync(
  new URL('../data/ai-engineer-progress.json',import.meta.url),'utf8'
));
const duplicate=()=>structuredClone(source);
const fixture=()=>({
  url:'https://github.com/RiverThreeR3/AIEngineer/commit/'+ 'a'.repeat(40),
  commit:'a'.repeat(40),result:'PASS',
  reviewedAt:'2026-11-07T12:00:00Z',
  note:'Synthetic unit-test fixture only, not a real CI attestation'
});
test('baseline never claims completion for open PRs or WIP projects',()=>{
  const p=summarizeProgress(source);
  assert.equal(p.total,66);
  assert.equal(p.verified,0);
  assert.equal(p.percent,0);
  assert.equal(p.completedTracks,0);
  assert.equal(p.remaining,66);
  assert.equal(p.remainingTracks,11);
  assert.match(renderProgress(p),/0\.0%/);
  assert.match(renderProgress(p),/0\/11/);
});

test('one accepted technical gate increases granular progress but not finished tracks',()=>{
  const d=duplicate();
  d.tracks[0].gates.implementation={status:'VERIFIED',evidence:[fixture()]};
  const p=summarizeProgress(d);
  assert.equal(p.verified,1);
  assert.equal(p.percent,1.5);
  assert.equal(p.completedTracks,0);
  assert.match(p.meter,/░/);
});

test('all six gates required for exactly one completed track',()=>{
  const d=duplicate();
  for(const key of d.gates)d.tracks[0].gates[key]={
    status:'VERIFIED',evidence:[fixture()]
  };
  const p=summarizeProgress(d);
  assert.equal(p.verified,6);
  assert.equal(p.completedTracks,1);
  assert.equal(p.percent,9.1);
  assert.equal(p.remainingTracks,10);
});

test('100% is impossible until all 66 acceptance gates are verified',()=>{
  const d=duplicate();
  for(const track of d.tracks)for(const key of d.gates)
    track.gates[key]={status:'VERIFIED',evidence:[fixture()]};
  const p=summarizeProgress(d);
  assert.equal(p.percent,100);
  assert.equal(p.verified,66);
  assert.equal(p.completedTracks,11);
  assert.equal(p.meter,'█'.repeat(20));
  assert.equal(p.status,'ZERADO / 100%');
});

test('never count an unreviewed or malformed acceptance claim',()=>{
  for(const badEvidence of [
    [],[{...fixture(),result:'FAIL'}],
    [{...fixture(),commit:'short'}],
    [{...fixture(),url:'http://github.com/fake'}],
    [{...fixture(),reviewedAt:'invalid'}],
    [{...fixture(),note:'too short'}]
  ]){
    const d=duplicate();
    d.tracks[0].gates.implementation={
      status:'VERIFIED',evidence:badEvidence
    };
    assert.throws(()=>summarizeProgress(d),
      /verified_gate_without_reviewable_evidence/);
  }
});
test('reject duplicate or invented track IDs and missing gates',()=>{
  const a=duplicate();
  a.tracks[0].id=a.tracks[1].id;
  assert.throws(()=>summarizeProgress(a),/invalid_ai_engineer_track/);
  const b=duplicate();
  delete b.tracks[0].gates.demo;
  assert.throws(()=>summarizeProgress(b),/invalid_ai_engineer_track/);
  const c=duplicate();
  c.tracks.push(structuredClone(c.tracks[0]));
  assert.throws(()=>summarizeProgress(c),/invalid_ai_engineer_ledger/);
});
