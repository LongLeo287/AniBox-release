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

## Release Rules (added 08-10-2026, owner-approved)

- **Updates are mandatory.** Since AniBox 2.9.6-hotfix, any newer `versionCode` in `version.json` forces every AniBox user to update the next time the app opens. A wrong `version.json` breaks every user at once. `"mandatory": false` in `version.json` turns the next release back into a soft update (emergency valve). To recover from a bad release, roll `version.json` back to the previous good version.
- **Publishing order:**
  1. Sign the APK with the AniBox release key (`signerSha256` must match).
  2. Create the GitHub release and upload `AniBox.apk`, the versioned APK and `SHA256SUMS.txt`.
  3. Download `releases/latest/download/AniBox.apk` again and check that its SHA-256 equals `sha256` in `version.json`.
  4. Update `README.md` and `SHA256SUMS.txt`.
  5. Update `version.json` last.
- **Version numbers step minimally, with no jumps.**
  - Hotfixes add a fourth number: the next one after 2.9.6-hotfix2 is `2.9.6.3`, then `2.9.6.4`, and so on.
  - Raise the minor or major number only for a large batch of new features, and only with owner approval.
  - `versionCode` always goes up by exactly 1. Never use `-hotfix` suffixes again.
- **Smoke test first.** Before `version.json` changes, test the exact signed APK (the x86 twin on the emulator, or the real box) by installing it over the previous release. History, favourites and settings must survive, and the update gate must report CURRENT.
- **AniSub compatibility.** A new AniBox must keep working with every released AniSub (0.2.x–0.4.x) and with no AniSub installed. The `AniSubCompatibilityMatrixTest` in the AniBox repo is a release gate.
