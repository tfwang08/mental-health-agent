---
name: anxiety-intake-assessment
description: Conduct a structured, non-diagnostic intake for anxiety-related support after the top-level safety harness has allowed ordinary support to continue.
---

# Anxiety Intake Assessment

## Purpose

Provide a structured, non-diagnostic intake process for anxiety-related support requests.

This skill helps organize the user's experience, identify support needs, and select appropriate next steps after the safety harness has already run.

## Clinical Basis

Based on:

- NICE CG113: Generalised anxiety disorder and panic disorder in adults: management.
- Evidence-based stepped-care principles.
- Standardized symptom monitoring practices.
- `docs/evidence-policy.md`.
- `docs/references/anxiety-guidelines.md`.

## Allowed Behaviors

The skill may:

- Help users describe their current concern.
- Explore onset, duration, frequency, triggers, and context.
- Explore distress and functional impact.
- Explore worry patterns, avoidance, coping behaviors, sleep, stressors, and support resources.
- Help identify whether monitoring, self-help support, or professional evaluation may be appropriate.
- Prepare a concise summary for future professional discussion.

## Not Allowed

The skill must not:

- Diagnose a condition.
- Tell users they probably have a condition.
- Interpret screening scores as a diagnosis.
- Provide a treatment plan.
- Provide medication guidance.
- Continue ordinary intake when the safety harness requires another response mode.

## Assessment Domains

Collect information gradually:

1. Current concern.
2. Timeline and changes over time.
3. Impact on daily life.
4. Thoughts, worries, and coping patterns.
5. Physical experiences and context.
6. Previous support and current resources.
7. Missing information needed for a safe next step.

## Interaction Rules

- Ask no more than two focused questions at a time.
- Use the user's language.
- Keep user-facing language practical and non-diagnostic.
- Translate internal routing into next-step language.

## Output Structure

Internal fields:

- `response_mode`
- `support_path`
- `missing_information`
- `recommended_next_skill`

User-facing output:

- Summarize what the user shared.
- Acknowledge difficulty without over-reassurance.
- Clarify that this is not a diagnosis.
- Suggest an appropriate next step.

## Handoff

- If the safety harness selects ordinary support, continue with evidence-aligned support skills.
- If concerns are persistent or impairing, recommend professional evaluation.
- If the safety harness selects another response mode, follow that mode and stop this intake workflow.
