# Source Notes

This project follows a conservative clinical workflow model informed by:

- NICE CG113: management of generalized anxiety disorder and panic disorder in adults.
- NICE NG225: assessment, management, and prevention of recurrence after self-harm.
- NHS Talking Therapies service standards: routine outcome monitoring, PHQ-9, GAD-7, and problem-specific anxiety measures.
- SAMHSA SAFE-T and Columbia C-SSRS concepts: direct inquiry about suicidal thoughts, plans, behavior, intent, and protective factors.
- OpenAI safety best practices: moderation, adversarial testing, human oversight, input/output limits, and clear communication of system limitations.

Design implications:

- Use stepped support.
- Do not diagnose.
- Do not expose internal diagnostic hypotheses; formulation is only for safety routing.
- Do not use scale scores alone to determine safety.
- Treat medical red flags as medical until assessed.
- Crisis disclosures require live human support.
