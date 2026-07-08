# Local Resource Routing

## Purpose

Define how the agent should handle location-dependent support resources.

## Rules

- Do not guess local resources when the user's region is unknown.
- Prefer official local services when location information is available.
- Ask for country or region only when it helps connect the user to appropriate resources.
- Keep resource guidance short and practical.
- Do not replace local emergency systems or professional services.

## Design Note

Future implementations may connect a location-aware resource lookup tool instead of maintaining static lists.
