# Hyphaeic Public License (HPL-1.0)

An Apache 2.0 derivative with additional conditions regarding information sovereignty.

## Summary

HPL-1.0 grants standard open source permissions (use, modify, distribute, patent rights) with restrictions on use by operators of:

| Restricted | Definition |
|------------|------------|
| **Suppression Infrastructure** | Systems restricting lawful expression based on viewpoint without transparent justification and public reversal metrics |
| **Surveillance Infrastructure** | Systems aggregating noncombatant data without consent or providing government access without judicial oversight |

Defense applications targeting lawful combatants under international humanitarian law are explicitly permitted.

## Quick Reference

| Use Case | Permitted |
|----------|-----------|
| Individual developers | ✅ |
| Small companies (<100 employees, <$50M revenue) | ✅ Safe harbor for suppression provisions |
| Defense/military against combatants | ✅ Explicitly permitted |
| Academic research | ✅ |
| Platforms with opaque content moderation | ❌ |
| Surveillance vendors (any size) | ❌ No safe harbor |
| Cloud providers serving surveillance infrastructure | ❌ Material support clause |

## Applying HPL-1.0

### 1. Add LICENSE and NOTICE files

Copy `LICENSE` and `NOTICE` to your repository root.

### 2. Add source headers (optional)

```
Copyright [year] [name]
SPDX-License-Identifier: HPL-1.0
```

### 3. Reference in package manifest

```toml
# Cargo.toml
license-file = "LICENSE"
```

```json
// package.json
"license": "SEE LICENSE IN LICENSE"
```

## Key Provisions

**Section 4.1** — Prohibited uses (suppression, surveillance, material support)

**Section 4.2** — Automatic retroactive termination upon violation

**Section 4.3** — Discovery and audit consent in disputes

**Section 4.4** — Asymmetric jurisdiction (licensor selects venue)

**Section 4.5** — Safe harbor for small entities (suppression only; no safe harbor for surveillance)

**Section 4.6** — Defense applications carve-out

## Compatibility

HPL-1.0 is **not** OSI-approved. The Information Sovereignty conditions discriminate by use case, which is intentional.

Code under HPL-1.0 can incorporate Apache 2.0, MIT, and BSD-licensed dependencies. Incorporating GPL-licensed code would require releasing under GPL, which conflicts with HPL-1.0's additional restrictions.

## License

The Hyphaeic Public License itself is dedicated to the public domain under [CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/). You may use, modify, and adapt the license text for your own projects without attribution.

## Links

- [Full License Text](LICENSE)
- [NOTICE Template](NOTICE)
- [Hyphaeic](https://hyphaeic.com)

---

*With love, Hyphaeic SPC · Seattle, WA*
