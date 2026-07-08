# Mental Health Agent

Language: [中文](README.md) | **English**

![Risk Warning: Not Medical Service](https://img.shields.io/badge/Risk_Warning-Not_Medical_Service-red)

> [!WARNING]
> **Important: This project is not a medical device and does not provide diagnosis, treatment, prescriptions, medication adjustments, emergency care, or crisis intervention.**
>
> This project is intended for psychoeducation, symptom relief support, self-help guidance, screening assistance, and help-seeking guidance. Outputs must not replace qualified clinicians, therapists, counselors, pharmacists, or emergency services.
>
> If you or someone else may be in immediate danger, including self-harm, suicide, violence risk, overdose, severe loss of control, chest pain, fainting, severe breathing difficulty, neurological symptoms, or other urgent medical concerns, seek immediate human or medical support.

This is a Chinese-user-oriented mental-health support agent prototype containing project-local Codex skills, safety rules, and synthetic evaluation cases.

The first phase focuses on anxiety support. The project intentionally starts with safety infrastructure before adding more intervention workflows.

## Project Structure

- `.agents/skills/`: project-local Codex skills.
- `safety/`: shared safety boundaries, routing rules, and response constraints.
- `evals/`: synthetic safety and regression test cases.
- `docs/`: design notes and evidence documentation.

## Current Skills

- `mental-health-safety-harness`: top-level safety gate for all mental-health workflows.
- `risk-crisis-triage`: routing for crisis, self-harm, violence risk, psychosis-like symptoms, severe impairment, medication risks, and medical red flags.

## Non-Clinical Positioning

This project supports symptom relief, psychoeducation, self-help guidance, screening support, and referral guidance. It is not a diagnostic system, treatment system, medication advice system, or crisis service.

Internal formulation is used only for safer routing and must never be exposed as a diagnosis or disease label.

## Language Policy

- User-facing documentation is available in Chinese and English.
- Internal agent instructions, safety rules, skills, evaluation logic, and clinical terminology are written in English for precision and maintainability.
- The final product should respond in the user's preferred language.
