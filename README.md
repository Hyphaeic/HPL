# Hyphaeic Public License (HPL-1.0)

A software license derived from Apache 2.0 with additional conditions restricting use by operators of censorship and surveillance infrastructure.

## Philosophy

This software is provided for the advancement of open infrastructure and individual sovereignty. The Licensor declines monetary compensation in favor of a specific ethical exchange: **You may use this Work only if You respect the digital rights of end-users.** This ethical compliance is the sole and material consideration for this License. If You cannot pay this price, You have no right to the Work.

## Quick Summary

| You CAN use HPL-licensed software if you... | You CANNOT use HPL-licensed software if you... |
|---------------------------------------------|------------------------------------------------|
| Build open source or commercial software | Operate platforms that censor lawful speech without transparency |
| Develop defense/military applications against lawful combatants | Operate surveillance systems targeting civilian populations |
| Run a small company with content moderation | Provide cloud/API services to censorship or surveillance operators |
| Are an individual or researcher | Are a dominant platform with viewpoint-based content policies |
| Build defense systems without law enforcement integration | Build any system with law enforcement integration |

## What This License Does

HPL-1.0 grants the same permissions as Apache 2.0 (use, modify, distribute, sublicense, patent protection) with one additional section: **Conditions on Information Sovereignty** (Section 4).

Section 4 prohibits use by entities that operate:
- **Suppression Infrastructure**: Systems that censor lawful expression without transparency
- **Surveillance Infrastructure**: Systems that monitor civilian populations without consent
- **Law Enforcement Integration**: Systems designed to feed data to government/police

It also prohibits providing material support (hosting, APIs, compute) to such operators.

---

## Understanding Suppression Infrastructure

This is the core concept that distinguishes HPL from other licenses. Read this section carefully.

### The Three-Prong Test

A system becomes "Suppression Infrastructure" if it restricts the transmission, display, or discoverability of **lawful expression** based on viewpoint, political content, or deviation from institutional consensus, where such restriction **fails ANY** of these requirements:

| Prong | Requirement | What It Means |
|-------|-------------|---------------|
| **(a) TRANSPARENCY** | Each restriction must have a permanently accessible public record containing: (i) a cryptographic hash of the restricted content, (ii) the specific policy clause cited, and (iii) a substantive explanation of how the content violated that clause | You must publish a hash of removed content, cite the exact rule, AND explain *how* the content violated it—sufficiently for an independent observer to evaluate. Bare citations like "violated Policy 7.3" do NOT satisfy this. |
| **(b) ACCOUNTABILITY** | Must provide a dispute resolution process AND publish quarterly: (i) total restrictions applied, (ii) restrictions reversed on dispute, and (iii) disaggregated data sufficient to detect asymmetric enforcement | You need an appeals process AND quarterly stats that are broken down enough to reveal if you're enforcing selectively against certain viewpoints or speaker categories. |
| **(c) NEUTRALITY** | Restrictions must be applied uniformly without regard to identity, political affiliation, viewpoint, or perceived status. Identical content must receive identical treatment regardless of source. | You cannot enforce rules selectively based on who is speaking. Patterns of selective enforcement constitute asymmetric application **regardless of facial neutrality of stated policies**. |

**These are disjunctive (OR)**: Failing ANY single prong makes your system Suppression Infrastructure.

### Transparency Is Necessary But Not Sufficient

A common misreading of this license is that it merely requires transparency—that if you explain your censorship thoroughly enough, you're compliant. **This is incorrect.**

Consider the three prongs together:

- **Prong (a)** requires transparency about *what* you remove (with cryptographic proof and substantive reasoning)
- **Prong (b)** requires transparency about your *error rate* and *enforcement patterns*
- **Prong (c)** requires *uniform application regardless of speaker identity*

A platform could satisfy (a) and (b) perfectly—publishing detailed justifications for every removal and quarterly statistics—while still violating (c) by enforcing rules selectively. Conversely, a platform could apply rules uniformly while failing to provide public justification.

**All three prongs must be satisfied simultaneously.**

### What Is "Lawful Expression"?

The license restricts interference with "lawful expression." This is jurisdiction-specific:

| Content Type | Status |
|--------------|--------|
| Content illegal where the user is located | Not lawful expression—removal is fine |
| Content legal where the user is located but illegal elsewhere | Lawful expression for that user—removal is restricted |
| Content that violates platform ideology but is legal | Lawful expression—removal is restricted |
| Content that is distasteful but legal | Lawful expression—removal is restricted |

**Key principle**: The legality question is answered from the perspective of the affected user's jurisdiction, not the platform's headquarters, not the most restrictive jurisdiction where the platform operates, and not the platform's own preferences.

---

## What Counts as Valid Content Removal

This section clarifies what content removal is permitted versus prohibited under HPL-1.0.

### Always Permitted (Not "Lawful Expression")

These removals are always fine because the content isn't protected as "lawful expression":

| Content Category | Examples | Why Permitted |
|------------------|----------|---------------|
| **Illegal content** | CSAM, credible death threats, content illegal in the user's jurisdiction | Not lawful expression by definition |
| **Spam and commercial fraud** | Bot networks, scam operations, fake reviews | Commercial fraud is illegal |
| **Technical abuse** | DDoS coordination, malware distribution, platform exploitation | Illegal activity |
| **Court-ordered removal** | Content subject to valid judicial order in affected jurisdiction | Legal process satisfied |

### Permitted If Transparent (Lawful Expression With Compliance)

These removals involve lawful expression but can be compliant if all three prongs are satisfied:

| Action | Requirements for Compliance |
|--------|----------------------------|
| Remove content that violates disclosed rules | (a) Public record with hash, policy citation, and substantive explanation, (b) dispute process + quarterly disaggregated stats, (c) enforce identically regardless of speaker |
| Restrict content to logged-in users | Same transparency requirements |
| Apply geographic restrictions | Must be based on actual illegality in that jurisdiction, not platform preference |
| Downrank or reduce distribution | Same transparency requirements as removal—algorithmic suppression is still suppression |

### Never Permitted (Fails Regardless of Transparency)

These removals cannot be made compliant because they inherently violate prong (c):

| Policy Type | Why It Fails |
|-------------|--------------|
| **"Hate speech" removal of lawful content** | Viewpoint-based restriction; selectively enforced based on speaker/target identity |
| **"Misinformation" or "disinformation" labels/removal** | Viewpoint-based; assumes platform authority to determine truth on contested questions |
| **"Harassment" policies applied to lawful criticism** | Asymmetrically enforced based on who is criticizing whom |
| **Deplatforming for off-platform speech or associations** | Punishment based on identity/affiliation, not content |
| **"Coordinated inauthentic behavior" applied to political organizing** | Selectively applied to disfavored political movements |
| **"Community guidelines" that are vague or selectively enforced** | Enables asymmetric application by design |

### The "Hate Speech" Problem

"Hate speech" policies deserve specific attention because they are often presented as neutral when they are inherently viewpoint-based.

**Why "hate speech" removal of lawful content fails the test:**

1. **It's viewpoint-based by definition**: "Hate speech" policies restrict expression *because of the viewpoint expressed*, not because of any illegal act.

2. **It's inherently asymmetric**: In practice, "hate speech" policies protect some groups but not others. Criticism of Group A is "hate speech"; identical criticism of Group B is permitted. This is textbook prong (c) violation.

3. **It substitutes platform ideology for law**: If the speech is actually illegal (incitement to imminent violence, true threats), it can be removed as illegal content. If it's legal but the platform disapproves, removing it is viewpoint-based censorship of lawful expression.

4. **Transparency doesn't cure it**: A platform could publish detailed explanations of every "hate speech" removal and still operate Suppression Infrastructure, because the policy itself is viewpoint-based.

**The test is simple**: If you're removing content that isn't illegal, ask why. If the answer is "because we disagree with it" or "because it offends people we want to protect," that's viewpoint-based suppression of lawful expression.

---

## Suppression Infrastructure Examples

| Scenario | Permitted? | Why |
|----------|------------|-----|
| Platform removes CSAM | ✅ Yes | Illegal content, not lawful expression |
| Platform removes credible death threats | ✅ Yes | Illegal content |
| Platform removes posts with public record (hash + policy + substantive explanation) | ✅ Yes | Meets transparency requirements (if rules are viewpoint-neutral) |
| Platform removes political content without explanation | ❌ No | Fails prong (a): no public justification |
| Platform publishes quarterly transparency report with disaggregated reversal data | ✅ Yes | Satisfies prong (b), but must also satisfy (a) and (c) |
| Platform bans users for off-platform political affiliations | ❌ No | Fails prong (c): punishment based on identity/affiliation |
| Platform removes "hate speech" that is legal in user's jurisdiction | ❌ No | Viewpoint-based restriction of lawful expression |
| Platform labels lawful content as "misinformation" | ❌ No | Viewpoint-based; platform claiming authority over contested truth |
| Platform removes "harassment" (lawful criticism of public figures) | ❌ No | Asymmetric enforcement based on target identity |
| Platform enforces identical rules but only against one political tendency | ❌ No | Fails prong (c): asymmetric application regardless of facial neutrality |
| Platform removes content legal in user's country because it's illegal in another country | ❌ No | Lawful expression for that user |
| Platform uses algorithmic downranking instead of removal | ❌ No | Suppression of discoverability still counts |
| Platform has vague "community guidelines" with selective enforcement | ❌ No | Vagueness enables asymmetric application |
| Large platform removes only jurisdictionally illegal content, uniformly enforced | ✅ Yes | Meets Section 4.1(d) requirements |
| Small forum (<100 employees, <$50M revenue) with arbitrary moderation | ✅ Yes | Safe harbor applies |
| University restricts campus network access to certain sites | ✅ Yes | Institutional network, not public communications platform |

---

## Surveillance Infrastructure

**What it means**: Systems targeting noncombatant populations that:
- Collect personal data without explicit, informed, revocable consent for each distinct use case
- Enable correlation of identity across contexts without user initiation
- Provide government/law enforcement/intelligence access without a public, individualized judicial order

**"Noncombatant"** means any individual not actively engaged in armed conflict as a member of an organized armed force. Civilian populations, including citizens subject to domestic law enforcement, are noncombatants. A state's unilateral classification of its own civilians as combatants does not alter their status under this License.

| Scenario | Permitted? | Why |
|----------|------------|-----|
| Military reconnaissance drone targeting enemy combatants | ✅ Yes | Targets lawful combatants, not civilians |
| License plate reader sharing data with local police | ❌ No | Surveillance of civilian population |
| Analytics platform with explicit user consent and data portability | ✅ Yes | Explicit, informed, revocable consent |
| Facial recognition for foreign military intelligence | ✅ Yes | Defense application against combatants |
| Facial recognition database for domestic law enforcement | ❌ No | Targets noncombatant civilian population |
| Smart city sensors feeding police real-time location data | ❌ No | Civilian monitoring without individual consent |
| Corporate security cameras on private property, no police access | ✅ Yes | No government access provision |
| Startup (<100 employees) building ALPR for police departments | ❌ No | **No safe harbor** for surveillance infrastructure |
| End-to-end encrypted messaging app | ✅ Yes | Does not provide government access |
| Messaging app with law enforcement backdoor | ❌ No | Provides government access without judicial order |
| Workplace monitoring software with employee consent | ✅ Yes | Consent obtained, not government surveillance |
| School surveillance system with police integration | ❌ No | Targets noncombatant minors with government access |

**The test**: Does the system target civilians AND (a) collect data without consent, (b) correlate identity across contexts, or (c) give government access without judicial oversight?

**Important**: There is **NO safe harbor** for surveillance infrastructure. A 10-person startup building police surveillance tools cannot use HPL-licensed software.

---

## Law Enforcement Integration

**What it means**: Any feature, API, data pipeline, or contractual arrangement designed to facilitate automated export, mirroring, or real-time access of data to any system controlled by or accessible to a government entity, law enforcement agency, or intelligence service.

This includes:
- **Backdoor access**: Administrative keys or privileges provided to state actors
- **Automated reporting**: Tools that transmit user data without a public, individualized judicial order
- **Predictive policing feeds**: Ingestion of data into predictive policing databases or fusion centers

| Scenario | Permitted? | Why |
|----------|------------|-----|
| App with no government data sharing | ✅ Yes | No LEI |
| App with warrant-based data disclosure (case-by-case judicial orders) | ✅ Yes | Individualized judicial process, not automated integration |
| App with automated "hash matching" reporting to law enforcement | ❌ No | Automated reporting without individualized judicial order |
| Platform with "transparency portal" for police bulk requests | ❌ No | Facilitates bulk access |
| Defense contractor system with FBI data feed | ❌ No | LEI disqualifies even defense applications |
| Security camera system with police API | ❌ No | Real-time access provision to law enforcement |
| Security camera system, recordings only disclosed via warrant | ✅ Yes | Individualized judicial process |

**Critical interaction with Defense Applications**: Section 4.6 permits defense/military uses, but **explicitly excludes** any system incorporating Law Enforcement Integration. You can build weapons systems; you cannot build domestic surveillance systems, even if you call them "defense."

---

## Material Support

**What it means**: Providing compute, hosting, APIs, training data, or integration services to entities operating Suppression or Surveillance Infrastructure.

| Scenario | Permitted? | Why |
|----------|------------|-----|
| Cloud provider hosting a transparency-compliant social platform | ✅ Yes | Client doesn't operate prohibited infrastructure |
| Cloud provider hosting Clearview AI | ❌ No | Material support to surveillance infrastructure |
| API provider serving a platform with opaque content moderation | ❌ No | Material support to suppression infrastructure |
| Open source contributor whose code is used by bad actors | ✅ Yes | Downstream misuse ≠ material support |
| Consulting firm helping police department deploy facial recognition | ❌ No | Integration services for surveillance |
| Data center providing power/cooling to surveillance company | ⚠️ Gray | May constitute material support depending on knowledge and specificity |
| CDN serving a platform that censors lawful political speech | ❌ No | Infrastructure support for suppression |
| Payment processor serving surveillance company | ⚠️ Gray | Generic financial services vs. specific enablement |

**The test**: Are you knowingly providing resources that specifically enable the operation of prohibited infrastructure?

---

## Dominant Position

**What it means**: Entities with >$1B annual revenue from communications/social/search services OR >50M monthly active users.

Dominant platforms face stricter requirements under Section 4.1(d): their content restrictions must be **(i)** strictly limited to content illegal in the jurisdiction of the affected user, and **(ii)** applied uniformly without regard to viewpoint.

| Scenario | Permitted? | Why |
|----------|------------|-----|
| Large platform, content policy limited to illegal content, uniform enforcement | ✅ Yes | Meets 4.1(d) requirements |
| Large platform with "hate speech" policies beyond illegal content | ❌ No | Not limited to illegal content |
| Large platform with "misinformation" policies | ❌ No | Viewpoint-based, not limited to illegal content |
| Large platform, same rules for all users regardless of identity | ✅ Yes | Uniform application |
| Large platform, selective enforcement against political opponents | ❌ No | Not applied uniformly |
| Small platform (<50M users, <$1B) with arbitrary policies | ✅ Yes | Not in Dominant Position; safe harbor may apply |

**The test**: If you're big, your content restrictions must be (a) limited to jurisdictionally illegal content AND (b) applied uniformly regardless of viewpoint. "Hate speech," "misinformation," and similar viewpoint-based policies are not compatible with Dominant Position status.

---

## Defense Applications

**What it means**: Military and defense uses are explicitly permitted when targeting lawful combatants under international humanitarian law.

| Scenario | Permitted? | Why |
|----------|------------|-----|
| Autonomous drone targeting enemy military installation | ✅ Yes | Lawful military objective |
| Missile guidance system | ✅ Yes | Defense application |
| Military intelligence gathering on foreign armed forces | ✅ Yes | Targets combatants |
| Border surveillance of domestic civilians | ❌ No | Targets noncombatants |
| "Counter-terrorism" system monitoring domestic political groups | ❌ No | Domestic civilian monitoring |
| Police drone surveillance labeled as "defense" | ❌ No | Label doesn't change civilian targeting |
| National Guard deployment against domestic protesters | ❌ No | Civilians are noncombatants regardless of state classification |
| Defense system with law enforcement data integration | ❌ No | **LEI exclusion applies** |
| Military system feeding data to FBI/DHS | ❌ No | **LEI exclusion applies** |

**The test**: Is the target a lawful combatant under international humanitarian law? A state calling its own citizens "enemies" or "terrorists" doesn't make them combatants.

**Critical limitation**: Defense permissions **explicitly exclude** any system incorporating Law Enforcement Integration. Individual self-defense is permitted; state-sponsored mass surveillance via law enforcement pipelines is prohibited, even under a "defense" label.

---

## Enforcement Provisions

HPL-1.0 includes provisions designed to make violations costly:

| Provision | Effect |
|-----------|--------|
| **Retroactive termination** | Violation voids the license as if it was never granted—all past use becomes infringement |
| **Verification consent** | Upon prima facie showing of violation, you agree to independent technical audit of moderation logs and policy enforcement records |
| **Trade secret waiver** | You waive trade secret claims regarding existence or error rates of moderation systems (but not source code) |
| **Audit cost splitting** | Each party bears its own costs; auditor fees split equally unless otherwise agreed |
| **Rebuttable presumption** | Refusal to cooperate with verification within 60 days creates presumption of non-compliance |
| **Injunctive relief without bond** | Licensor can seek injunction without posting bond |
| **Fee shifting (one-way)** | If Licensor prevails in enforcement, violator pays Licensor's attorneys' fees and costs |
| **Jurisdiction** | Disputes resolved in Licensor's jurisdiction (specified in NOTICE file, or where Licensor resides) |

These provisions are designed to make legal/compliance teams flag HPL-licensed software as high-risk for entities that might violate Section 4.

---

## Licensor Protections

HPL-1.0 includes provisions protecting the Licensor:

| Provision | Effect |
|-----------|--------|
| **No enforcement obligation** | Licensor is not required to monitor for or enforce violations; non-enforcement is not waiver |
| **Zero liability cap** | Licensor's total aggregate liability is $0 USD |
| **Good faith standard** | Enforcement must be based on credible evidence; no vexatious or bad-faith actions |
| **Exclusive remedies** | Licensor's only remedies are injunctive relief, license termination, and public disclosure |
| **Damages waiver** | Licensor explicitly waives compensatory and statutory monetary damages (but NOT attorneys' fees) |
| **Enforcement immunity** | Licensor not liable for costs arising from enforcement or non-enforcement decisions |

---

## Essential Consideration

HPL-1.0 treats Section 4 compliance as the **sole consideration** for the license grant:

| Principle | Effect |
|-----------|--------|
| **Ethical exchange** | Your compliance with Section 4 is what you "pay" for the right to use the software |
| **Indivisibility** | If Section 4 is held unenforceable by a court, the entire license is void due to failure of consideration |
| **Immediate termination** | If Section 4 fails, all rights terminate immediately |
| **Post-termination use** | Continued use after termination constitutes copyright infringement |
| **Limited remedy** | Licensor waives compensatory damages for post-termination use; sole remedy is injunctive relief |

This means you cannot argue "Section 4 is unenforceable, so I get Apache 2.0 terms." If Section 4 fails, you get nothing.

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

**We have transparent "hate speech" policies. Are we compliant?**

No. Transparency is necessary but not sufficient. "Hate speech" removal of lawful content is viewpoint-based by definition and inherently asymmetric in application. You cannot make a viewpoint-based policy compliant by being transparent about it.

**What if we only remove content that most people find offensive?**

Popularity doesn't determine lawfulness. If the content is legal, it's lawful expression. Removing it because it's unpopular or offensive is viewpoint-based suppression.

**Can we remove "misinformation" if we're transparent about it?**

No. "Misinformation" policies assume platform authority to determine truth on contested questions. This is viewpoint-based content restriction. If content is actually illegal (fraud, defamation), remove it as illegal content. If it's legal but you disagree with it, you cannot remove it without operating Suppression Infrastructure.

**What's the difference between Law Enforcement Integration and responding to warrants?**

Responding to individualized, public judicial orders (warrants) on a case-by-case basis is permitted. Building automated pipelines, backdoors, or bulk access systems for law enforcement is LEI and prohibited.

**Can I build defense software that also has law enforcement uses?**

No. The defense permissions explicitly exclude systems with Law Enforcement Integration. If your system feeds data to domestic law enforcement, it's not covered by the defense carve-out.

**What happens if a court finds Section 4 unenforceable?**

The entire license is void. You don't fall back to Apache 2.0 terms—you lose all rights to use the software. This is the "Essential Consideration" provision.

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
3. Specify your jurisdiction in the copyright notice
4. Update package metadata:

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
