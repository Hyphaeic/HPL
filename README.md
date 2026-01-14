# Hyphaeic Public License (HPL-1.0)

A software license derived from Apache 2.0 with additional conditions restricting use by operators of censorship and surveillance infrastructure.

## Quick Summary

| You CAN use HPL-licensed software if you... | You CANNOT use HPL-licensed software if you... |
|---------------------------------------------|------------------------------------------------|
| Build open source or commercial software | Operate platforms that censor lawful speech without transparency |
| Develop defense/military applications against lawful combatants | Operate surveillance systems targeting civilian populations |
| Run a small company with content moderation | Provide cloud/API services to censorship or surveillance operators |
| Are an individual or researcher | Are a dominant platform with viewpoint-based content policies |

## What This License Does

HPL-1.0 grants the same permissions as Apache 2.0 (use, modify, distribute, sublicense, patent protection) with one additional section: **Conditions on Information Sovereignty** (Section 4).

Section 4 prohibits use by entities that operate:
- **Suppression Infrastructure**: Systems that censor lawful expression without transparency
- **Surveillance Infrastructure**: Systems that monitor civilian populations without consent

It also prohibits providing material support (hosting, APIs, compute) to such operators.

---

## Use Case Examples

### Suppression Infrastructure

**What it means**: Systems that restrict lawful speech based on viewpoint, without public justification, transparent reversal rates, or equal treatment of speakers.

| Scenario | Permitted? | Why |
|----------|------------|-----|
| Social platform removes illegal content (CSAM, direct threats) | ✅ Yes | Illegal content is not "lawful expression" |
| Platform removes posts with public notice citing specific violation | ✅ Yes | Meets transparency requirement |
| Platform removes political content without explanation | ❌ No | No contemporaneous, specific justification |
| Platform publishes quarterly transparency report with reversal rates | ✅ Yes | Meets transparency requirement |
| Platform bans users based on off-platform political affiliations | ❌ No | Asymmetric application based on identity |
| Small forum (<100 employees, <$50M revenue) with arbitrary moderation | ✅ Yes | Safe harbor applies |
| University restricts campus network access to certain sites | ✅ Yes | Not a communications/social platform; institutional network |

**The test**: Does the system restrict lawful speech AND fail to provide (a) specific public justification, (b) published reversal metrics, or (c) viewpoint-neutral application?

---

### Surveillance Infrastructure

**What it means**: Systems targeting noncombatant populations that collect personal data without consent, correlate identity across contexts, or provide government access without judicial oversight.

| Scenario | Permitted? | Why |
|----------|------------|-----|
| Military reconnaissance drone targeting enemy combatants | ✅ Yes | Targets lawful combatants, not civilians |
| License plate reader sharing data with local police | ❌ No | Surveillance of civilian population |
| Analytics platform with user consent and data portability | ✅ Yes | Explicit, informed, revocable consent |
| Facial recognition for foreign military intelligence | ✅ Yes | Defense application against combatants |
| Facial recognition database for domestic law enforcement | ❌ No | Targets noncombatant civilian population |
| Smart city sensors feeding police real-time location data | ❌ No | Civilian monitoring without individual consent |
| Corporate security cameras on private property, no police access | ✅ Yes | No government access provision |
| Startup (<100 employees) building ALPR for police departments | ❌ No | **No safe harbor** for surveillance infrastructure |
| End-to-end encrypted messaging app | ✅ Yes | Does not provide government access |
| Messaging app with law enforcement backdoor | ❌ No | Provides government access without judicial order |

**The test**: Does the system target civilians AND (a) collect data without consent, (b) correlate identity across contexts, or (c) give government access without judicial oversight?

**Important**: There is NO safe harbor for surveillance infrastructure. A 10-person startup building police surveillance tools cannot use HPL-licensed software.

---

### Material Support

**What it means**: Providing compute, hosting, APIs, training data, or integration services to entities operating Suppression or Surveillance Infrastructure.

| Scenario | Permitted? | Why |
|----------|------------|-----|
| Cloud provider hosting a transparency-compliant social platform | ✅ Yes | Client doesn't operate prohibited infrastructure |
| Cloud provider hosting Clearview AI | ❌ No | Material support to surveillance infrastructure |
| API provider serving a platform with opaque content moderation | ❌ No | Material support to suppression infrastructure |
| Open source contributor whose code is used by bad actors | ✅ Yes | Downstream misuse ≠ material support |
| Consulting firm helping police department deploy facial recognition | ❌ No | Integration services for surveillance |
| Data center providing power/cooling to surveillance company | ⚠️ Gray | May constitute material support depending on knowledge and specificity |

**The test**: Are you knowingly providing resources that specifically enable the operation of prohibited infrastructure?

---

### Dominant Position

**What it means**: Entities with >$1B annual revenue from communications/social/search services OR >50M monthly active users.

| Scenario | Permitted? | Why |
|----------|------------|-----|
| Large platform, content policy limited to illegal content, uniform enforcement | ✅ Yes | Meets 4.1(d) requirements |
| Large platform with viewpoint-based "misinformation" policies | ❌ No | Not limited to illegal content |
| Large platform, same rules for all users regardless of identity | ✅ Yes | Uniform application |
| Large platform, selective enforcement against political opponents | ❌ No | Not applied uniformly |
| Small platform (<50M users, <$1B) with arbitrary policies | ✅ Yes | Not in Dominant Position |

**The test**: If you're big, your content restrictions must be (a) limited to jurisdictionally illegal content AND (b) applied uniformly regardless of viewpoint.

---

### Defense Applications

**What it means**: Military and defense uses are explicitly permitted when targeting lawful combatants under international humanitarian law.

| Scenario | Permitted? | Why |
|----------|------------|-----|
| Autonomous drone targeting enemy military installation | ✅ Yes | Lawful military objective |
| Missile guidance system | ✅ Yes | Defense application |
| Military intelligence gathering on foreign armed forces | ✅ Yes | Targets combatants |
| Border surveillance of civilians | ❌ No | Targets noncombatants |
| "Counter-terrorism" system monitoring domestic political groups | ❌ No | Domestic civilian monitoring |
| Police drone surveillance labeled as "defense" | ❌ No | Label doesn't change civilian targeting |
| National Guard deployment against domestic protesters | ❌ No | Civilians are noncombatants regardless of state classification |

**The test**: Is the target a lawful combatant under international humanitarian law? A state calling its own citizens "enemies" doesn't make them combatants.

---

## Enforcement Provisions

HPL-1.0 includes provisions designed to make violations costly:

| Provision | Effect |
|-----------|--------|
| **Retroactive termination** | Violation voids the license as if it was never granted |
| **Discovery consent** | Violators agree to disclose internal moderation policies and communications |
| **Audit consent** | Violators agree to independent compliance audits at their expense |
| **Asymmetric jurisdiction** | Disputes resolved in jurisdiction selected by licensor |
| **Fee shifting** | Non-prevailing party pays all legal costs |

These provisions are designed to make legal/compliance teams flag HPL-licensed software as high-risk for entities that might violate Section 4.

---

## Frequently Asked Questions

**Is this OSI-approved?**

No. Section 4 discriminates based on use case, which violates the Open Source Definition. This is intentional.

**Can I use this for my own projects?**

Yes. HPL-1.0 is designed to be reusable. See the APPENDIX in the license for boilerplate.

**What if I'm not sure if my use case is permitted?**

If you're asking, you're probably fine. The restrictions target specific categories of institutional actors. Individual developers, researchers, small companies, and most businesses are unaffected.

**Does using HPL-licensed code in my project make my project HPL-licensed?**

No. HPL-1.0 is not copyleft. You can use HPL-licensed code in proprietary projects. The restrictions apply to *who* can use the code, not what license derivatives must carry.

**What about AI training?**

HPL-1.0 doesn't specifically address training data. Standard copyright principles apply. If your AI system would itself constitute Suppression or Surveillance Infrastructure, you cannot use HPL-licensed code in it.

**I operate a small forum with moderation. Am I affected?**

Probably not. The Safe Harbor (Section 4.5) exempts entities with <100 employees and <$50M revenue from Suppression Infrastructure restrictions. However, if you're building surveillance tools for law enforcement, there is no safe harbor regardless of company size.

**What's the difference between this and ethical source licenses?**

Most ethical source licenses (Hippocratic License, etc.) restrict harmful uses like weapons and military applications. HPL-1.0 inverts this: military/defense uses are explicitly permitted, while censorship and civilian surveillance are restricted.

**Can a government agency use HPL-licensed software?**

Depends on the application. Military and intelligence agencies targeting foreign combatants: yes. Domestic law enforcement conducting mass surveillance: no. A government IT department running internal tools: yes.

**Is this enforceable?**

Some provisions may face enforceability challenges depending on jurisdiction. However, the primary function is signaling and filtering: compliance teams will flag these provisions as risk factors regardless of ultimate enforceability.

---

## Files in This Repository

| File | Description |
|------|-------------|
| `LICENSE` | The complete Hyphaeic Public License, Version 1.0 |
| `NOTICE` | Attribution notice template |
| `README.md` | This document |

---

## Applying HPL-1.0 to Your Project

1. Copy `LICENSE` to your repository root
2. Add the boilerplate notice to source files (see APPENDIX in LICENSE)
3. Update package metadata:

**Cargo.toml (Rust):**
```toml
license = "HPL-1.0"
license-file = "LICENSE"
```

**package.json (Node.js):**
```json
"license": "SEE LICENSE IN LICENSE"
```

**pyproject.toml (Python):**
```toml
license = {file = "LICENSE"}
```

---

## License

This repository is licensed under [HPL-1.0](LICENSE).

---

## Contact

- **Repository**: [github.com/hyphaeic/hpl](https://github.com/hyphaeic/hpl)
- **Organization**: [Hyphaeic SPC](https://hyphaeic.com)

With Love, Hyphaeic
