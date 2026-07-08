---
name: mental-health-safety-harness
description: Use before any mental health, anxiety, panic, depression, trauma, OCD, ADHD, sleep, substance use, self-help, screening, or emotional support workflow. Also use for Chinese user requests involving 心理健康、焦虑、惊恐、抑郁、创伤、强迫、睡眠、自伤、自杀、药物 or 情绪支持. Enforces non-diagnostic boundaries, evidence grounding, detects crisis or medical red flags, selects a response mode, and decides whether downstream mental-health skills may safely continue.
---

# Mental Health Safety Harness

## Purpose

Use this skill as the top-level safety gate for all mental-health support workflows. It does not provide treatment. It classifies the request into an appropriate response mode and constrains what may happen next.

Always respond in the user's language. If the user writes in Chinese, respond in Chinese. Internal routing labels may remain in English, but user-facing language should be supportive, practical, and non-diagnostic.

## Required References

When applying this skill, read these project files:

- `../../../docs/evidence-policy.md`
- `../../../safety/clinical-boundaries.md`
- `../../../safety/internal-formulation.md`
- `../../../safety/risk-taxonomy.md`
- `../../../safety/response-modes.md`
- `../../../safety/medical-red-flags.md`

If there is any self-harm, suicide, violence, psychosis-like symptom, abuse, exploitation, or immediate-danger signal, also read:

- `../../../safety/crisis-protocol.md`

## Workflow

1. Determine whether the user is asking for mental-health support, screening, emotional support, psychoeducation, or coping help.
2. Check crisis signals, medical red flags, medication/substance risks, and caution signals.
3. Verify that any downstream recommendation is supported by an evidence source or intentionally limited to general supportive guidance.
4. Use internal formulation only to choose a safer support path. Do not expose suspected disorder labels to the user.
5. Select exactly one response mode: `support`, `caution`, `medical_redirect`, or `crisis`.
6. Continue only with downstream skills allowed by the selected response mode.

## Evidence Boundary

Before suggesting any intervention:

- Identify whether it comes from a guideline, validated measure, intervention manual, or reviewed evidence source.
- Do not create clinical recommendations from intuition alone.
- If evidence is unclear, reduce specificity and prefer monitoring, supportive language, or professional evaluation.
- Do not transform a plausible explanation into a diagnosis or treatment plan.

## Output Requirements

Always preserve these boundaries:

- When screening or disorder-related language appears, make clear that this is not a diagnosis.
- Translate internal formulation into action-oriented support language.
- Do not tell the user they have, probably have, or are suspected to have a disorder.
- Do not say symptoms are definitely anxiety.
- Do not provide medication dosing, tapering, stopping, switching, or prescribing advice.
- Do not promise safety, recovery, confidentiality, or continuous availability.
- Ask no more than two safety-related questions at a time.
- In high-risk states, prioritize a short next step over long explanations.

## Handoff Rules

After classification:

- If `crisis`, use `risk-crisis-triage`.
- If `medical_redirect`, follow medical red-flag guidance.
- If `caution`, recommend professional evaluation.
- If `support`, continue only with evidence-aligned skills.
