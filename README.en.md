# Mental Health Agent

Language: [中文](README.md) | **English**

![Risk Warning: Not Medical Service](https://img.shields.io/badge/Risk_Warning-Not_Medical_Service-red)

> [!WARNING]
> **Important: This project is not a medical device and does not provide diagnosis, treatment, prescriptions, medication adjustments, emergency care, or crisis intervention.**
>
> This project is intended for psychoeducation, symptom relief support, self-help guidance, screening assistance, and help-seeking guidance. Outputs must not replace qualified clinicians, therapists, counselors, pharmacists, or emergency services.
>
> If you or someone else may be in immediate danger, including self-harm, suicide, violence risk, overdose, severe loss of control, chest pain, fainting, severe breathing difficulty, neurological symptoms, or other urgent medical concerns, seek immediate human or medical support.

This is a mental-health support agent prototype containing project-local Codex skills, safety rules, and synthetic evaluation cases.

The first phase focuses on anxiety support. The project intentionally starts with safety infrastructure before adding more intervention workflows.

## Current Status

This repository is currently a **safety- and evidence-first prototype**, not a complete mental-health product.

The current focus is to establish:

- non-diagnostic boundaries;
- crisis and medical-red-flag routing;
- clinical-source-first skill design rules;
- synthetic safety evaluation cases;
- an engineering foundation for later anxiety-support workflows.

## Project Highlights

### 1. Clinical sources first, not model improvisation

The core principle is **evidence-first**: mental-health skills must be grounded in clinical guidelines, public-health guidance, validated measurement practices, or clearly identified low-risk supportive techniques.

The project should not let the model invent diagnoses, treatment suggestions, or professional-sounding explanations without a traceable source.

### 2. Non-diagnostic by design

Internal formulation is used only for safety routing and support-path selection. It must not be exposed to users as a diagnosis, suspected condition, or disease label.

User-facing language should prefer:

- "This is not a diagnosis."
- "This pattern is worth discussing with a qualified professional."
- "Let's check safety first, then decide on a suitable next step."

It should avoid:

- "You have this disorder."
- "You probably have this diagnosis."
- "This score confirms a condition."

### 3. Safety routing before self-help

Every mental-health workflow should pass through `mental-health-safety-harness` first.

If crisis signals, medical red flags, medication or substance risks, or severe functional impairment are present, the system should route to safety guidance before ordinary anxiety exercises.

### 4. Clinical source families

Current design is informed by:

- NICE CG113: management of generalized anxiety disorder and panic disorder in adults;
- NICE NG225: assessment, management, and prevention of recurrence after self-harm;
- NHS Talking Therapies: stepped care, standardized measures, and outcome monitoring;
- WHO psychological self-help and scalable psychological intervention materials;
- SAFE-T / C-SSRS concepts: direct inquiry and safety-relevant elements for suicide-related risk.

These sources constrain what the agent may do, what it must not do, and when it should redirect to human or medical support. They are not used to let the agent diagnose users.

## How is this different from chatting directly in Codex?

Directly chatting with Codex or a general-purpose chat model mostly depends on the current prompt, the model's default behavior, and any temporary reminders added by the user. This repository is not meant to make the model simply "chat better". Its purpose is to engineer the safety boundaries, clinical grounding, and workflow constraints needed for mental-health support scenarios.

Main differences:

| Dimension | Direct chat | This project |
|---|---|---|
| Clinical grounding | Often depends on the model's current answer, with limited traceability | Each mental-health skill should document its clinical basis, scope, and limitations |
| Safety order | The conversation may jump directly into reassurance, analysis, or suggestions | Mental-health workflows pass through the safety harness before ordinary support continues |
| Diagnostic boundary | Users can easily push the model toward doctor-like judgments | Diagnosis and user-facing suspected disorder labels are explicitly prohibited |
| Medical red flags | Physical warning signs may be over-explained as anxiety | Medical red flags are handled before anxiety explanations |
| Reuse | Each conversation starts over | Rules, skills, docs, and evals live in the repo and can be reviewed, reused, and improved |
| Regression testing | It is hard to know whether a prompt change weakened safety | Synthetic eval cases and validation scripts can catch safety regressions over time |
| Extension model | Add more prompt instructions | Add evidence-aligned skills, references, and eval cases |

In short: **direct chat is a one-off model interaction; this project is a reviewable, testable, and extensible mental-health agent engineering scaffold.**

## Project Structure

- `.agents/skills/`: project-local Codex skills.
- `safety/`: shared safety boundaries, routing rules, and response constraints.
- `evals/`: synthetic safety and regression test cases.
- `docs/`: design notes and evidence documentation.
- `scripts/`: local validation and test scripts.

## Current Skills

- `mental-health-safety-harness`: top-level safety gate for all mental-health workflows.
- `risk-crisis-triage`: routing for crisis, self-harm, violence risk, psychosis-like symptoms, severe impairment, medication risks, and medical red flags.
- `anxiety-intake-assessment`: non-diagnostic structured intake for anxiety-related support.

## Non-Clinical Positioning

This project supports symptom relief, psychoeducation, self-help guidance, screening support, and referral guidance. It is not a diagnostic system, treatment system, medication advice system, or crisis service.

Internal formulation is used only for safer routing and must never be exposed as a diagnosis or disease label.

## Language Policy

- User-facing documentation is available in Chinese and English.
- Internal agent instructions, safety rules, skills, evaluation logic, and clinical terminology are written in English for precision and maintainability.
- The final product should respond in the user's preferred language.
