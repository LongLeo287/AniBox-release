# AniBox Release — Review Instructions

## Scope

This repository distributes AniBox releases and update metadata. Prioritize release integrity, supply-chain security, update reliability, and user safety.

## Review Priorities

- Verify versionCode and versionName consistency.
- Validate release URLs, filenames, and metadata structure.
- Ensure SHA-256 values correspond to intended release artifacts.
- Check APK signing certificate consistency and update compatibility.
- Review GitHub Actions permissions, triggers, tokens, and API operations.
- Detect unauthorized or unintended release modifications.
- Prevent broken update paths, incorrect latest-release references, and invalid metadata.
- Ensure release notes accurately describe verified changes.
- Preserve compatibility with existing AniBox clients.
- Check for accidental exposure of credentials or sensitive data.

## Review Discipline

- Prioritize actionable security and release-integrity defects.
- Avoid unrelated application architecture or UX/UI suggestions.
- Distinguish metadata consistency checks from actual artifact verification.
- Never claim an APK is safe or authentic without sufficient evidence.
- Communicate review findings in Vietnamese.
