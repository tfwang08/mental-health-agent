---
name: mental-health-safety-harness
description: Use before any mental health, anxiety, panic, depression, trauma, OCD, ADHD, sleep, substance use, self-help, screening, or emotional support workflow. Also use for Chinese user requests involving 心理健康、焦虑、惊恐、抑郁、创伤、强迫、睡眠、自伤、自杀、药物 or 情绪支持. Enforces non-diagnostic boundaries, detects crisis or medical red flags, selects a response mode, and decides whether downstream mental-health skills may safely continue.
---

# Mental Health Safety Harness

## Purpose

Use this skill as the top-level safety gate for all mental-health support workflows. It does not provide treatment. It classifies the request into an appropriate response mode and constrains what may happen next.

Always respond in the user's language. If the user writes in Chinese, respond in Chinese. Internal routing labels may remain in English, but user-facing language should be supportive, practical, and non-diagnostic.

## Required References

When applying this skill, read these project files:

- `../../../safety/clinical-boundaries.md`
- `../../../safety/internal-formulation.md`
- `../../../safety/risk-taxonomy.md`
- `../../../safety/response-modes.md`
- `../../../safety/medical-red-flags.md`

If there is any self-harm, suicide, violence, psychosis-like symptom, abuse, exploitation, or immediate-danger signal, also read:

- `../../../safety/crisis-protocol.md`

## Workflow

1. Determine whether the user is asking for mental-health support, screening, emotional support, psychoeducation, or coping help.
2. Check crisis signals: suicide, self-harm, harm to others, psychosis-like experiences, severe self-neglect, abuse, exploitation, or immediate danger.
3. Check medical red flags: chest pain, fainting, severe breathing difficulty, neurological symptoms, suspected overdose or withdrawal, medication changes, pregnancy/postpartum complications, head injury, or first severe panic-like symptoms in a medically high-risk person.
4. Check medication or substance-use signals: dosage changes, stopping or tapering medication, interactions, mixing with alcohol or drugs, withdrawal, or replacing treatment with supplements.
5. Check caution signals: persistent functional impairment, complex comorbidity, repeated panic attacks, severe insomnia with unusually high energy, minors, pregnancy/postpartum, or medically vulnerable users.
6. Use internal formulation only to choose a safer support path. Do not expose suspected disorder labels to the user.
7. Select exactly one response mode: `support`, `caution`, `medical_redirect`, or `crisis`.
8. Continue only with downstream skills allowed by the selected response mode.

## Response Mode Rules

- `support`: Continue with ordinary self-help, screening support, monitoring, and coping skills.
- `caution`: Provide limited coping support and recommend professional evaluation. Avoid deep therapy work.
- `medical_redirect`: Stop ordinary mental-health support and recommend medical evaluation.
- `crisis`: Stop ordinary support and use immediate safety guidance.

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
- If `medical_redirect`, follow medical red-flag guidance. Do not continue anxiety exercises except as a very brief bridge while the user seeks help.
- If `caution`, recommend professional evaluation. Use low-intensity skills only when they do not delay help-seeking.
- If `support`, continue with anxiety, panic, screening, worry-sorting, relaxation, or action-planning skills as appropriate.
