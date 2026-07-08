# Evidence Policy

This project is evidence-first. Mental-health skills must be grounded in clinical guidelines, public-health guidance, validated measurement practices, or clearly identified low-risk supportive techniques.

## Core Rule

Do not invent clinical advice.

A skill may only provide an intervention, routing rule, screening workflow, or user-facing recommendation when it can be traced to one of the accepted source types below. If the evidence basis is unclear, the skill must either:

- reduce the output to general supportive language;
- ask a safety-relevant clarification;
- recommend professional evaluation; or
- mark the proposed behavior as a TODO rather than implementing it.

## Accepted Source Hierarchy

Prefer sources in this order:

1. Current or recently updated clinical guidelines from recognized bodies, such as NICE, NHS, WHO, APA, VA/DoD, SAMHSA, CDC, or equivalent national health systems.
2. Validated manuals or implementation guides for psychological interventions, especially stepped-care, CBT-based self-help, applied relaxation, psychological first aid, and crisis/safety planning.
3. Peer-reviewed systematic reviews, meta-analyses, randomized controlled trials, or validation papers for measures and interventions.
4. Official scale documentation or widely accepted clinical measurement practices.
5. Expert consensus only when higher-level evidence is unavailable, clearly marked as lower confidence.

Avoid relying on blogs, marketing pages, anecdotal examples, social media, or model-generated rationales as clinical evidence.

## Required Clinical Traceability for Each Skill

Each mental-health skill should include a `Clinical Basis` section with:

- the guideline, manual, measure, or source family it follows;
- what the skill is allowed to do;
- what the skill must not do;
- when the skill must redirect to professional, medical, or crisis support;
- any known limitations or uncertainty.

## User-Facing Constraint

Even when internal routing uses clinical concepts, user-facing responses must not present diagnostic labels, suspected disorder labels, or diagnostic certainty.

Translate clinical reasoning into practical support language:

- Preferred: "This pattern is worth discussing with a qualified professional."
- Preferred: "This score can help track symptoms, but it cannot confirm a condition."
- Not allowed: "You probably have panic disorder."
- Not allowed: "This means you have generalized anxiety disorder."

## Screening and Measures

Screening scores may be used for monitoring and next-step support. They must not be used as diagnosis.

Scores must not be used alone to decide safety, treatment eligibility, or whether someone needs help. Safety decisions must consider the user's current intent, plan, access to means, functional state, medical red flags, substance or medication context, and support availability.

## Interventions

Low-intensity self-help skills should stay within conservative, structured, evidence-aligned boundaries:

- psychoeducation;
- active monitoring;
- brief grounding or stabilization;
- CBT-style worry sorting;
- problem-solving for controllable stressors;
- applied relaxation or breathing as symptom support;
- small action planning;
- preparing a summary for professional care.

Do not provide unsupervised deep therapy, trauma processing, detailed exposure therapy, medication management, or treatment plans for complex presentations.

## Evidence Gaps

When evidence is limited, mixed, or outside the repository's reviewed scope, the skill should say less, not more. It should prefer safe support, monitoring, and professional referral over confident claims.

## Maintenance

When adding or changing a mental-health skill:

1. Add or update the `Clinical Basis` section.
2. Add or update source notes in `docs/source-notes.md` if a new clinical source family is introduced.
3. Add eval cases for unsupported diagnosis, overconfident advice, medical red flags, and crisis handling.
4. Review the change against `safety/clinical-boundaries.md` and `safety/internal-formulation.md`.
