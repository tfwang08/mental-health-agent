# Measurement Reference Notes

## NHS Talking Therapies

Title: NHS Talking Therapies for anxiety and depression

Organization: NHS England

URL: https://www.england.nhs.uk/mental-health/adults/nhs-talking-therapies/

## What this repository uses it for

- Routine outcome monitoring as a design pattern.
- Use of standardized measures to support monitoring and next-step conversations.
- Stepped-care framing: offer the least intrusive appropriate support first.
- Separation between screening or monitoring and diagnosis.

## What this repository does not infer from it

- Scale scores must not be used as diagnosis.
- Scale scores must not be used alone for safety decisions.
- The agent must not claim to reproduce NHS Talking Therapies, clinical supervision, or therapy delivery.
- The agent must not present itself as a therapist or clinician.

## Implementation notes

Measurement-related skills should explicitly tell users that scores can help track symptoms or guide next-step conversations, but cannot confirm a condition. Any concerning item related to immediate safety must route through the safety harness rather than remain inside ordinary score interpretation.
