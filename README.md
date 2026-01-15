# Hyphaeic Public License (HPL-1.0)

## How This Works

HPL-1.0 is Apache 2.0 with a legal landmine against entities that enable opaque suppression of information, surveillance technologies and their material beneficiaries.

A deployable legal trojan horse for small teams, indie devs, open hardware projects, researchers and others. Licensors are extensively protected.

It lists explicit terms,including differentiating law enforcement and military usage against lawful combatants. 

The objective is to lay license traps in the open source ecosystem that will inevitably get scooped up into larger codebases of entities enabling digital surveillance & suppression. These entities are them thus in violation of this license, which opens grounds to seek injunction.

The discovery process is early and public. This licence lists internal moderation informstion and brings it into the public's eye through the courts. 

1. **Retroactive termination**: If they violate Section 4, the license is void *ab initio*—as if it was never granted. All prior use becomes copyright infringement.

2. **Audit consent**: They've agreed to let an independent auditor inspect their moderation logs and policy enforcement. They've waived trade secret protection over their moderation systems.

3. **Fee shifting**: If the licensor wins enforcement, the violator pays attorneys' fees.

4. **Jurisdiction selection**: Disputes happen where the licensor lives, not where the violator is headquartered.

5. **No fallback**: The "Essential Consideration" clause means if a court strikes down Section 4, the entire license is void. They don't get Apache 2.0 terms—they get nothing.

The goal is to make this code radioactive to surveillance companies and censorship platforms. Their lawyers will flag it. Their compliance teams will say no. And if they use it anyway without reading carefully, they've walked into a trap.

For everyone else—small teams, indie devs, open hardware projects, researchers—the safe harbor means none of this applies to you. Apache 2.0 with bite. 

---

## Who This Is For

| You | What HPL Gives You |
|-----|-------------------|
| **Solo developers** | Use it, ship it, sell it. No restrictions. |
| **Small teams (<100 people)** | Full safe harbor. Moderate your community however you want. |
| **Open hardware projects** | Your FPGA firmware, PCB layouts, robot code—all protected. |
| **Startups under $50M** | The restrictions don't touch you. |
| **Researchers & academics** | Your work stays in the commons. |
| **Defense contractors** | Build weapons systems—just not domestic surveillance. |

**The safe harbor**: Fewer than 100 employees and less than $50M in revenue? The content moderation rules don't apply to you.

---

## Who This Is Not For

| Them | What HPL Denies Them |
|------|---------------------|
| **Platforms that censor lawful speech without transparency** | Can't use your code |
| **Surveillance companies building tools to track civilians** | Can't use your code |
| **Cloud providers hosting censorship/surveillance infrastructure** | Can't use your code to do it |
| **Big Tech with viewpoint-based "trust and safety"** | Can't use your code |
| **Police tech vendors** | No safe harbor, no exceptions |

---

## The Philosophy

We decline monetary compensation in favor of a specific ethical exchange:

**You may use this Work only if you respect the digital rights of end-users.**

This is the sole consideration for this license. If you cannot pay this price, you have no right to the Work.

---

## Quick Reference

| You CAN use HPL-licensed software if you... | You CANNOT use HPL-licensed software if you... |
|---------------------------------------------|------------------------------------------------|
| Build open source or commercial software | Operate platforms that censor lawful speech without transparency |
| Are a small team with any moderation policy | Operate surveillance systems targeting civilian populations |
| Develop defense/military applications against lawful combatants | Provide cloud/API services to censorship or surveillance operators |
| Are an individual, researcher, or hobbyist | Are a dominant platform with viewpoint-based content policies |
| Build hardware, firmware, FPGA designs, robotics | Build any system with law enforcement integration |

---

## What This License Does

HPL-1.0 is Apache 2.0 with one additional section: **Conditions on Information Sovereignty** (Section 4).

**You get everything Apache 2.0 gives you:**
- Use commercially
- Modify freely
- Distribute widely
- Sublicense
- Patent protection
- No copyleft requirements

**Section 4 prohibits use by operators of:**
- **Suppression Infrastructure**: Systems that censor lawful expression without transparency
- **Surveillance Infrastructure**: Systems that monitor civilian populations without consent
- **Law Enforcement Integration**: Systems designed to feed data to government/police

It also prohibits providing material support (hosting, APIs, compute) to such operators.

---

## The Safe Harbor

Section 4.5 creates a complete safe harbor for small organizations.

**If you meet ALL of these conditions:**
- Fewer than 100 employees
- Less than $50M annual revenue  
- Not a dominant platform (>$1B or >50M users)

**Then the Suppression Infrastructure rules do not apply to you.**

This means you can:
- Moderate your community however you want
- Ban users for any reason
- Remove content without explanation
- Have vague community guidelines
- Enforce rules inconsistently

You're building a community, not a public utility.

### No Safe Harbor for Surveillance

There is no safe harbor for surveillance infrastructure, regardless of company size. A 10-person startup building facial recognition for police cannot use HPL-licensed software.

---

## Open Hardware

HPL-1.0 works for any copyrightable work:

| Domain | Examples |
|--------|----------|
| **Electronics** | PCB designs, schematics, FPGA/ASIC code, firmware |
| **Robotics** | Control systems, motion planning, sensor fusion |
| **Manufacturing** | CNC toolpaths, 3D printer firmware, parametric designs |
| **Embedded systems** | Microcontroller code, drivers, bootloaders |
| **Scientific instruments** | Lab equipment designs, data acquisition systems |
| **Agriculture tech** | Sensor networks, automation systems |
| **Energy systems** | Solar controllers, battery management |

---

## For the Lawyers: Suppression Infrastructure

A system becomes "Suppression Infrastructure" if it restricts lawful expression and **fails ANY** of these requirements:

### (a) TRANSPARENCY

Each restriction must have a permanently accessible public record containing:
- A cryptographic hash of the restricted content
- The specific policy clause cited
- A substantive explanation of how the content violated that clause

Bare citations like "violated Policy 7.3" don't satisfy this.

### (b) ACCOUNTABILITY  

The system must provide:
- A dispute resolution process
- Quarterly publication of: total restrictions, reversals on dispute, and disaggregated data sufficient to detect asymmetric enforcement

### (c) NEUTRALITY

Restrictions must be applied uniformly without regard to identity, political affiliation, viewpoint, or perceived status of the speaker.

Patterns of selective enforcement constitute asymmetric application regardless of facial neutrality of stated policies.

### All Three Required

Transparency doesn't cure viewpoint-based enforcement. Uniform application doesn't cure opacity. All three prongs must be satisfied simultaneously.

### What Is "Lawful Expression"?

Content that is legal in the affected user's jurisdiction—not where your servers are, not where your HQ is.

| Content Type | Status |
|--------------|--------|
| Illegal where user is located | Not protected—remove freely |
| Legal where user is but illegal elsewhere | Protected for that user |
| Legal but platform disagrees | Protected—viewpoint-based removal prohibited |

---

## For the Lawyers: Surveillance Infrastructure

Systems targeting noncombatant populations that:
- Collect personal data without explicit, informed, revocable consent for each distinct use case
- Enable correlation of identity across contexts without user initiation
- Provide government/law enforcement/intelligence access without a public, individualized judicial order

**"Noncombatant"** means civilians. A state calling protesters "terrorists" doesn't make them legitimate targets.

---

## For the Lawyers: Law Enforcement Integration

Any system designed to facilitate automated data access by government/law enforcement:

- **Backdoors**: Admin keys or privileges for state actors
- **Automated reporting**: Data transmission without individualized judicial orders  
- **Predictive policing feeds**: Ingestion into police databases or fusion centers

Responding to warrants is fine. Building automated pipelines is not.

Defense applications explicitly exclude systems with Law Enforcement Integration.

---

## Examples: Permitted

| Scenario | Why |
|----------|-----|
| Indie dev ships a SaaS product | Safe harbor, commercial use fine |
| Open hardware collective shares PCB designs | This is who it's for |
| Startup (<$50M) runs a forum with strict moderation | Safe harbor covers content moderation |
| Game studio uses HPL code in commercial title | Commercial use permitted |
| Defense contractor builds missile guidance | Defense applications permitted |
| Researcher publishes ML code | Academic use encouraged |
| Security researcher builds vulnerability scanner | Security research is not surveillance |
| Platform removes illegal content (CSAM, threats) | Illegal content isn't "lawful expression" |

## Examples: Prohibited

| Scenario | Why |
|----------|-----|
| Big Tech platform with opaque content moderation | Fails transparency requirements |
| Platform removes "hate speech" (lawful content) | Viewpoint-based restriction |
| Platform labels content "misinformation" | Platform claiming authority over truth |
| Clearview AI or similar facial recognition | Surveillance infrastructure |
| Startup building license plate readers for police | No safe harbor for surveillance |
| Cloud provider hosting surveillance company | Material support |
| "Smart city" sensors with police access | Civilian surveillance |
| Defense system with FBI data integration | LEI exclusion applies |

---

## Enforcement Provisions

| Provision | Effect |
|-----------|--------|
| **Retroactive termination** | Violation voids the license *ab initio*—all past use becomes infringement |
| **Audit consent** | Violators agree to independent technical audits |
| **Trade secret waiver** | Can't hide behind "proprietary moderation systems" |
| **Injunctive relief without bond** | Licensor can seek immediate court orders |
| **One-way fee shifting** | If Licensor wins, violator pays attorneys' fees |
| **Jurisdiction selection** | Disputes in Licensor's home jurisdiction |

---

## Licensor Protections

| Provision | Effect |
|-----------|--------|
| **No enforcement obligation** | You don't have to police violations |
| **Zero liability** | You can't be sued for enforcement decisions |
| **Good faith standard** | Prevents vexatious enforcement |
| **Damages waiver** | Seeking compliance, not money |

---

## Essential Consideration

Section 4 compliance is the sole consideration for the license. If a court finds Section 4 unenforceable, the entire license is void. You don't fall back to Apache 2.0—you lose all rights.

This prevents the attack: "Your restrictions are unenforceable, so I get permissive licensing for free."

---

## FAQ

**I'm a solo dev / small team. Do I need to worry about any of this?**

No. The safe harbor covers you completely for content moderation. Just don't build surveillance tools for police.

**Is this OSI-approved?**

No. Section 4 discriminates based on use case, which violates the Open Source Definition.

**Can I use this for my hardware project?**

Yes. HPL works for any copyrightable work: software, firmware, documentation, HDL code.

**Does using HPL code make my project HPL-licensed?**

No. HPL is not copyleft. The restrictions are on *who* can use it, not what license derivatives carry.

**What about AI training?**

If your AI system would itself constitute Suppression or Surveillance Infrastructure, you can't use HPL code in it. Otherwise, standard copyright principles apply.

**Can the military use this?**

Yes, for defense applications targeting lawful combatants. No, for domestic surveillance.

**We have transparent content moderation. Are we compliant?**

Transparency is necessary but not sufficient. If you're removing lawful content based on viewpoint, you're operating Suppression Infrastructure regardless of transparency.

**What if a court strikes down Section 4?**

The entire license is void. This prevents the "restrictions are unenforceable so I get Apache 2.0" attack.

**Is this enforceable?**

Some provisions may face challenges. The primary function is signaling: compliance teams will flag this as high-risk regardless of ultimate enforceability.

---

## Using HPL-1.0

1. Copy `LICENSE` to your repository root
2. Add the boilerplate notice (see APPENDIX in LICENSE)
3. Specify your jurisdiction in the copyright notice

**Cargo.toml:**
```toml
license = "HPL-1.0"
license-file = "LICENSE"
```

**package.json:**
```json
"license": "SEE LICENSE IN LICENSE"
```

**pyproject.toml:**
```toml
license = {file = "LICENSE"}
```

---

## Files

| File | Description |
|------|-------------|
| `LICENSE` | The complete Hyphaeic Public License, Version 1.0 |
| `NOTICE` | Attribution notice template |
| `README.md` | This document |

---

## License

This repository is licensed under [HPL-1.0](LICENSE).

---

## Contact

- **Repository**: [github.com/hyphaeic/hpl](https://github.com/hyphaeic/hpl)
- **Organization**: [Hyphaeic SPC](https://hyphaeic.com)

---

**With Love, Hyphaeic**
