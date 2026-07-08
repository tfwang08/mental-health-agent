# Security Policy

## Reporting Security Issues

If you discover issues that may cause user harm, privacy leakage, unauthorized diagnosis, medication misinformation, crisis-handling failures, or safety bypasses, please avoid publicly sharing reproducible exploit details.

Use GitHub Security Advisory or a private communication channel with maintainers. Add contact information here when available.

## High-Risk Issues

Examples include:

- Producing diagnostic conclusions or suspected disorder labels as facts.
- Telling users that medical red flags are "just anxiety".
- Providing medication dosage, stopping, tapering, switching, or mixing advice.
- Providing methods or concealment strategies related to self-harm, suicide, violence, overdose, or evasion of help.
- Continuing ordinary self-help instead of directing users to human support during crises.
- Exposing or unnecessarily storing sensitive mental-health information.
- Prompt injection or instruction attacks that disable the safety harness.

## Security Principles

- Prioritize user safety.
- Avoid storing sensitive mental-health information by default.
- All mental-health workflows must pass through `mental-health-safety-harness`.
- Crisis, medical red flags, medication risks, and substance-use risks must pass through `risk-crisis-triage`.
