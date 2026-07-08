# Contributing Guide

Thank you for contributing. This project involves mental-health support workflows, so all changes must prioritize safety and evidence-based behavior.

## Contribution Principles

- Do not add diagnosis functionality.
- Do not add medication dosage, stopping, tapering, switching, or prescribing advice.
- Do not expose internal formulation to users.
- Do not use scale scores as the only basis for safety decisions.
- Do not interpret medical red flags as anxiety by default.
- Do not keep crisis users inside ordinary self-help workflows.
- Do not add clinical behavior without documenting its evidence basis.

## Modifying Skills

When changing anything under `.agents/skills/`, verify:

- The workflow still passes through `mental-health-safety-harness`.
- High-risk scenarios still route through `risk-crisis-triage`.
- User-facing language remains non-diagnostic and action-oriented.
- Clinical basis, limitations, and evaluation cases are updated when needed.

## Before Submitting Changes

At minimum:

- Read `AGENTS.md`.
- Read relevant files under `safety/`.
- Review `docs/evidence-policy.md`.
- Run skill validation if available.
- Check that no user-facing diagnosis labels or medication advice were introduced.
