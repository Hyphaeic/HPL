# Hyphaeic Public License (HPL-1.0)

## What This Is

HPL-1.0 is Apache 2.0 with a legal landmine. It's an experiment in using open source licensing as a weapon against surveillance capitalism and information suppression—designed to create latent legal exposure for entities that hoover up open source code without reading the fine print.

For small teams, indie devs, open hardware projects, and researchers, it should function like a more protective Apache 2.0. For Big Tech platforms with opaque content moderation, surveillance companies, data brokers, and their enablers, it's intended to be radioactive: code that compliance teams flag as high-risk, and that creates real legal exposure if they use it anyway.

Whether all of this actually works in court remains to be seen. What follows is the theory.

---

## How This Is Designed to Work

HPL-1.0 adds a new section to Apache 2.0: **Conditions on Information Sovereignty** (Section 4). This section creates binding conditions that prohibit use by operators of surveillance infrastructure, suppression infrastructure (including financial deplatforming), data brokers, and entities providing targeted support to any of the above. It is protected by a poison pill in section 10 such that if a judge invalidates section 4, the entire license is void ab initio, as if it was never issued. Then the license becomes a commercial royalty license, payable at the specific commercial license rate set by the licensor.

The strategic objective is to seed the open source ecosystem with code that will inevitably get incorporated into larger codebases—code that creates latent legal exposure for entities enabling digital surveillance and suppression. When they use it without reading carefully, they've theoretically consented to terms that can be weaponized against them. Before trial, Section 4.3 allows you to invoke an independent audit of the violator's moderation systems. They've waived trade secret protection over the existence, methodology, and error rates of these systems (though not source code or model weights). The auditor can publish findings. This is the exposure mechanism—their internal suppression apparatus could become public record through the courts. This is the social benefit prong of the HPL.

### For Licensors: Intended Protections

**Zero financial risk (in theory).** The license attempts to cap licensor liability at $0. If you bring a claim in good faith and lose, the structure is designed so you owe nothing. Whether courts will honor this in all circumstances is untested.

**Fee shifting on wins.** If you prevail in enforcement, the violator has agreed to pay your attorneys' fees and costs. With solid evidence and aligned counsel, enforcement could be $0 in, $0 out—or better, they subsidize the effort.

**No enforcement obligation.** You're not required to monitor for violations or pursue enforcement. Failure to enforce one violation shouldn't waive your right to enforce others. You can ignore violations for years and still act when strategically advantageous.

**Collective action provisions.** The license contemplates multiple licensors coordinating enforcement, sharing evidence, and pooling resources. You can also assign enforcement rights to digital rights organizations or legal defense collectives—keep your copyright, let others handle litigation.

### For Licensors: What You Can Seek

**Injunctive relief.** The primary remedy is a court order compelling the violator to stop using your code. They've pre-consented to injunctions without bond, which is intended to remove a procedural barrier that normally protects defendants. Courts may or may not honor this consent.

**Public audit and discovery.** Before trial, Section 4.3 allows you to invoke an independent audit of the violator's moderation systems, with preset auditors of your choosing. They've waived trade secret protection over the existence, methodology, and error rates of these systems (though not source code or model weights). The auditor can publish findings. 

**Commercial royalty conversion.** If a court declines to issue an injunction, the license converts from royalty-free to commercial. The violator would owe the Commercial Royalty Amount (default: $10,000/month, customizable via NOTICE file) retroactively from the date of first violation, continuing monthly until the code is provably removed from their systems. The framing here matters: this isn't structured as damages, but as what the license would have cost without the ethical exchange. Courts are generally more comfortable with "you didn't pay, now you owe the price" than with penalty clauses.

**What you explicitly cannot seek:** Compensatory or statutory damages beyond the commercial royalty and legal fees. This is intentional. The spirit of this license is deterrence and exposure, not extraction. You're seeking compliance and transparency, not a payday. This framing may strengthen the licensor's position—it's harder to accuse someone of running a shakedown scheme when money isn't the goal.

### Why This Structure Might Work

**The trap is in the consent.** By exercising rights under HPL, users agree to:
- Audit by an independent party selected from the licensor's pre-approved list
- Waiver of trade secret claims over moderation systems
- Litigation in the licensor's home jurisdiction, not theirs
- Injunctive relief without bond
- Retroactive commercial royalties if they fight and lose on injunction
- Fee shifting if they lose entirely

Most open source licenses create obligations. HPL attempts to create *exposure*.

**The discovery mechanism is early and intended to be public.** Section 4.3 allows audit invocation upon a prima facie showing of violation—credible evidence, not proof beyond doubt. The audit is designed to happen before formal litigation, conducted by auditors the licensor has pre-approved (or selected from qualified professionals). The auditor reviews moderation logs, policy enforcement records, and aggregate statistics on content restrictions. They can publish a compliance determination. The goal: internal suppression apparatus—what content was removed, why, how decisions were made, whether enforcement was neutral—enters the public record. For platforms that rely on opacity to avoid accountability, this exposure may be the real punishment.

**Jurisdiction selection attempts to invert the power dynamic.** Disputes are to be adjudicated in the Licensor's Jurisdiction—your home turf, not theirs. In theory, a solo developer in rural Washington could force a Delaware corporation to litigate in Jefferson County. Big Tech's usual advantage—unlimited legal resources deployed in friendly forums—might be neutralized when they're fighting on your ground. How courts treat forum selection clauses in this context remains to be seen.

**The poison pill aims to prevent fallback.** Section 10 makes Section 4 compliance the sole consideration for the license. If a court finds Section 4 unenforceable, the intent is that the entire license is void—not just the ethical restrictions, but the grant of rights itself. Violators shouldn't be able to argue "your restrictions are invalid, so I get Apache 2.0 for free." They get nothing. All prior use becomes retroactive copyright infringement. Whether courts will enforce this "all or nothing" structure is genuinely uncertain.

**Compliance teams should flag this.** Even if some provisions face legal challenges, the primary function is signaling. Enterprise OSPO teams scan for license risks. HPL's audit consent, trade secret waiver, jurisdiction selection, and retroactive royalty provisions should trigger review. Legal will likely say "high risk, avoid." That's the deterrent working before any lawsuit is filed. And if they ignore the flag? They've walked into exactly the trap you laid.

### What Gets Exposed

Section 4.3 specifically targets:
- Content moderation logs and policy enforcement records
- Documentation of moderation policies and their implementation
- Aggregate statistics on enforcement actions by category
- Records of financial service denials and stated justifications
- The existence, methodology, and error rates of moderation systems

Explicitly **not** exposed: source code, model weights, or proprietary algorithms. The target is evidence of suppression patterns, not implementation details.

### The Intended Enforcement Flow

1. **Detection:** You discover (or are informed) that a violating entity is using HPL-licensed code
2. **Prima facie showing:** You compile credible evidence of Section 4 violation (statistical analysis, internal documents, complaint patterns, public statements)
3. **Audit invocation:** You provide written notice invoking Section 4.3
4. **Auditor selection:** 30 days to agree jointly; if deadlocked, you select from your pre-approved list or petition the court
5. **Audit:** 60 days to complete; auditor reviews records, publishes determination
6. **Enforcement decision:** Based on findings, seek injunction, license termination, and/or commercial royalty conversion
7. **Litigation:** In your jurisdiction, with fee shifting if you prevail

The audit phase is designed to happen before formal litigation. It's intended to create public exposure regardless of whether you ultimately go to court.

### Why Royalty Conversion Instead of Damages

Traditional damages face two problems in this context:

**The penalty problem.** Liquidated damages clauses are vulnerable to being struck down as unenforceable penalties. Courts ask: "Is this amount a reasonable estimate of actual harm, or is it punishment?" For a free license, that's a hard question to answer convincingly.

**The eBay problem.** Since *eBay v. MercExchange* (2006), courts don't automatically grant injunctions for IP violations. You need to show irreparable harm. If you're seeking money, courts may say "damages are adequate remedy" and deny the injunction you actually want.

Commercial royalty conversion attempts to solve both:

- **It's framed as price, not penalty.** The license was free because of the ethical exchange. Violate the ethics, lose the discount. $10k/month (or whatever you set) is positioned as what a commercial license for this software would cost. Courts understand pricing.

- **It's a fallback, not the goal.** By explicitly seeking injunction first and only invoking royalties if injunction is denied, you demonstrate that your primary interest is stopping the behavior, not collecting money. This framing may actually *help* the irreparable harm argument.

- **It accrues until removal.** Unlike one-time damages, monthly royalties continue until the code is provably removed. This creates ongoing pressure to actually comply rather than just pay and continue.

Whether this reframing survives judicial scrutiny remains untested.

---

## Who This Is For

| You | What HPL Intends to Give You |
|-----|-------------------|
| **Solo developers** | Use it, ship it, sell it. No restrictions. |
| **Micro-entities (≤5 people, ≤$1M)** | Full safe harbor. Do whatever you want. |
| **Small teams (<100 people, <$50M)** | Full safe harbor. Moderate your community however you want. |
| **Medium companies (<500 people, <$250M)** | Light requirements: publish a transparency report, provide appeals. |
| **Open hardware projects** | Your FPGA firmware, PCB layouts, robot code—all protected. |
| **Researchers & academics** | Your work stays in the commons. |
| **Defense contractors** | Build weapons systems—just not domestic surveillance. |

**The tiered safe harbor**: The smaller you are, the fewer requirements apply. Surveillance is never safe-harbored.

---

## Who This Is Not For

| Them | What HPL Intends to Deny Them |
|------|---------------------|
| **Platforms that censor lawful speech without transparency** | Can't use your code |
| **Surveillance companies building tools to track civilians** | Can't use your code |
| **Data brokers selling personal information** | Can't use your code |
| **Cloud providers hosting censorship/surveillance infrastructure** | Can't use your code to do it |
| **Big Tech with viewpoint-based "trust and safety"** | Can't use your code |
| **Police tech vendors** | No safe harbor, no exceptions |
| **Payment processors that deplatform for political reasons** | Can't use your code |
| **Any company with >10% revenue from surveillance/suppression** | No safe harbor regardless of size |

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
| Develop defense/military applications against lawful combatants | Sell personal data to third parties (data brokerage) |
| Are an individual, researcher, or hobbyist | Provide cloud/API services to censorship or surveillance operators |
| Build hardware, firmware, FPGA designs, robotics | Are a dominant platform with viewpoint-based content policies |
| Process payments neutrally based on financial risk | Build any system with law enforcement integration |
| | Deplatform creators for political reasons (financial suppression) |
| | Derive >10% of revenue from surveillance, suppression, or data brokerage |

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
- **Suppression Infrastructure**: Systems that censor lawful expression without transparency, including financial deplatforming
- **Surveillance Infrastructure**: Systems that monitor civilian populations without consent
- **Data Brokerage**: Selling personal data to third parties
- **Law Enforcement Integration**: Systems designed to feed data to government/police

It also prohibits providing **Targeted Support** (custom tools, knowing assistance) to such operators.

---

## The Safe Harbor Tiers

Section 4.5 creates tiered safe harbors based on organization size.

### Tier 0: Individuals and Micro-Entities

**If you have:**
- 5 or fewer employees
- Less than $1M annual revenue
- No Material Business Activity in surveillance/suppression

**Then:** You're exempt from Suppression Infrastructure and Dominant Position rules. Moderate however you want.

### Tier 1: Small Organizations

**If you have:**
- Fewer than 100 employees
- Less than $50M annual revenue
- No Dominant Position
- No Material Business Activity in surveillance/suppression

**Then:** Same exemptions as Tier 0. You're building a community, not a public utility.

### Tier 2: Medium Organizations

**If you have:**
- Fewer than 500 employees
- Less than $250M annual revenue
- No Dominant Position
- No Material Business Activity in surveillance/suppression

**Then:** You must:
- Publish an annual transparency report on content restrictions
- Provide an appeals process for moderation decisions

That's it. No full neutrality audit unless there's credible evidence of violation.

### Tier Transitions

Cross a threshold? You have **12 months** to comply with the new tier's requirements. The calculation uses trailing 12-month averages—no gaming by firing people on December 31st.

### The Material Business Activity Exclusion

You get **NO safe harbor at any tier** if ANY of these apply:

| Test | Threshold | What It's Designed to Catch |
|------|-----------|-----------------|
| **Revenue Test** | >10% from surveillance/suppression/data brokerage | Palantir, Clearview, data brokers |
| **Marketing Test** | Actively markets surveillance, law enforcement intelligence, or content suppression | Ring, police tech vendors |
| **Integration Test** | Products designed to integrate with law enforcement as standard feature | Flock Safety, fusion center feeders |

A 10-person startup building facial recognition for police fails the Marketing Test. No safe harbor.

### No Safe Harbor for Surveillance

There is **never** a safe harbor for Surveillance Infrastructure, regardless of company size, revenue, or any other factor. Period.

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

A system becomes "Suppression Infrastructure" if it restricts lawful expression (including economic participation) and **fails ANY** of these requirements:

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

### Economic Participation = Financial Services

Suppression Infrastructure includes **financial deplatforming**:
- Payment processors denying service for political reasons
- Banks closing accounts based on viewpoint
- Crowdfunding platforms removing campaigns for lawful speech
- Ad networks demonetizing based on content

Denial based on documented financial risk factors (credit history, fraud, chargebacks) applied uniformly is fine. Denial based on "we don't like your politics" is Suppression Infrastructure.

### What Is "Lawful Expression"?

Content that is legal **where the user is physically located**—not where your servers are, not where your HQ is.

| Content Type | Status |
|--------------|--------|
| Illegal where user is located | Not protected—remove freely |
| Legal where user is but illegal elsewhere | Protected for that user |
| Legal but platform disagrees | Protected—viewpoint-based removal prohibited |

**Universal exclusions** (NEVER Lawful Expression regardless of jurisdiction):
- CSAM (child sexual abuse material)
- True Threats (serious expressions of intent to commit violence against specific individuals)
- Direct incitement to imminent lawless action (Brandenburg standard)

Platforms may rely on reasonable location indicators (IP, registration info, user-provided data). Good-faith reliance on location indicators should protect platforms from users who lie about where they are.

---

## For the Lawyers: Surveillance Infrastructure

Systems targeting noncombatant populations that:
- Collect personal data without explicit, informed, revocable consent for each distinct use case
- Enable correlation of identity across contexts without user initiation
- Provide government/law enforcement/intelligence access without a public, individualized judicial order

**"Noncombatant"** means civilians. A state calling protesters "terrorists" doesn't make them legitimate targets.

---

## For the Lawyers: Data Brokerage

The commercial sale, licensing, or exchange of:
- Personally identifiable information
- Behavioral profiles
- Biometric data

To third parties, where the data subject didn't provide that data directly to the buyer for a disclosed purpose.

**Not Data Brokerage:** Anonymized aggregate analytics that can't be re-identified.

**Is Data Brokerage:** Anything that can be linked to identified or identifiable people.

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
| Platform removes illegal content (CSAM, threats) | Not "lawful expression" |
| Platform removes spam | Behavior-based, not viewpoint-based |
| Bank denies service due to fraud history | Neutral financial risk criteria |

## Examples: Prohibited

| Scenario | Why |
|----------|-----|
| Big Tech platform with opaque content moderation | Fails transparency requirements |
| Platform removes "hate speech" (lawful content) | Viewpoint-based restriction |
| Platform labels content "misinformation" | Platform claiming authority over truth |
| Stripe/PayPal deplatforming for politics | Financial suppression |
| Clearview AI or similar facial recognition | Surveillance infrastructure |
| Data broker selling location data | Data Brokerage, no safe harbor |
| Startup building license plate readers for police | Material Business Activity exclusion |
| Cloud provider building custom surveillance tools | Targeted Support |
| "Smart city" sensors with police access | Civilian surveillance |
| Defense system with FBI data integration | LEI exclusion applies |
| Company with 15% revenue from "trust & safety" products | Fails Revenue Test, no safe harbor |

---

## Enforcement Provisions

| Provision | Intended Effect |
|-----------|--------|
| **Retroactive termination** | Violation voids the license *ab initio*—all past use becomes infringement |
| **Audit consent** | Violators agree to independent technical audits |
| **Trade secret waiver** | Can't hide behind "proprietary moderation systems" |
| **Injunctive relief without bond** | Licensor can seek immediate court orders |
| **Commercial royalty conversion** | If injunction denied: license converts to commercial terms (default $10k/month, customizable) |
| **One-way fee shifting** | If Licensor wins, violator pays attorneys' fees |
| **Jurisdiction selection** | Disputes in Licensor's home jurisdiction |
| **Deadlock resolution** | If parties can't agree on auditor, Licensor selects from pre-approved list or petitions court |

---

## Commercial Royalty Conversion

The royalty-free license is contingent on ethical compliance. Violate Section 4, and the license is designed to convert to commercial terms.

**Default rate:** $10,000 USD per month, retroactive from first violation.

**Customizable via NOTICE file:**

| Project Type | Suggested Range |
|--------------|-----------------|
| Small utility library | $1,000 - $10,000/month |
| Significant component | $10,000 - $50,000/month |
| Core infrastructure | $50,000 - $250,000/month |
| Foundational platform | $250,000 - $1,000,000/month |
| Industry-standard tool | $1,000,000+/month |

A foundational library with $500k/month royalty creates $6M/year exposure. Retroactive over 3 years of infringement: $18M. That's not "cost of doing business"—that's potentially existential.

The amount should be defensible as "reasonable commercial value." Consider what a proprietary license would cost for similar software.

---

## Licensor Protections

| Provision | Intended Effect |
|-----------|--------|
| **No enforcement obligation** | You don't have to police violations |
| **Zero liability** | You shouldn't be liable for enforcement decisions |
| **Good faith standard** | Designed to prevent vexatious enforcement |
| **Damages waiver** | Seeking compliance, not extraction |
| **Collective action** | Coordinate with other licensors |
| **Assignment** | Hand off enforcement to digital rights orgs |

---

## Enforcement Coordination

### Registry

Licensors can register HPL-licensed works with a public registry. This facilitates:
- Discovery of HPL code in violating products
- Coordination among affected licensors
- Collective enforcement actions

### Assignment of Rights

Don't want to litigate yourself? Assign enforcement rights to:
- Digital rights organizations (EFF, Access Now, etc.)
- Legal defense collectives
- Other licensors with resources

You keep copyright. They handle enforcement.

### Collective Action

Multiple licensors whose code ends up in the same violating product can:
- Share evidence
- Pool resources
- Coordinate legal strategy
- Split costs

Death by a thousand cuts becomes death by a thousand licensors acting together.

---

## Essential Consideration

Section 4 compliance is the sole consideration for the license. If a court finds Section 4 unenforceable, the intent is that the entire license is void. You don't fall back to Apache 2.0—you lose all rights.

This is designed to prevent the attack: "Your restrictions are unenforceable, so I get permissive licensing for free."

---

## Affirmative Obligations

Upon first commercial deployment of HPL-licensed code, you must:

1. **Publish a dated statement** acknowledging the license terms at a public URL
2. **Notify the Licensor** within 30 days at the address in the NOTICE file

Failure to comply doesn't automatically terminate the license, but it may be evidence of bad faith in any enforcement proceeding.

---

## FAQ

**I'm a solo dev / small team. Do I need to worry about any of this?**

No. The safe harbor is designed to cover you completely for content moderation. Just don't build surveillance tools for police or sell user data.

**What's the difference between Tier 0 and Tier 1?**

Practically nothing. Tier 0 (≤5 people, ≤$1M) and Tier 1 (<100 people, <$50M) have the same exemptions. The tiers matter when you grow into Tier 2 or beyond.

**What happens when my startup crosses $50M?**

You have 12 months to comply with Tier 2 requirements (transparency report + appeals process). If you cross $250M or 500 employees, you have 12 months to reach full compliance.

**Is this OSI-approved?**

No. Section 4 discriminates based on use case, which violates the Open Source Definition. We're fine with that.

**Can I use this for my hardware project?**

Yes. HPL works for any copyrightable work: software, firmware, documentation, HDL code, PCB designs.

**Does using HPL code make my project HPL-licensed?**

No. HPL is not copyleft. The restrictions are on *who* can use it, not what license derivatives carry.

**What about AI training?**

If your AI system would itself constitute Suppression or Surveillance Infrastructure, you can't use HPL code in it. Otherwise, standard copyright principles apply.

**Can the military use this?**

Yes, for defense applications targeting lawful combatants. No, for domestic surveillance or anything with Law Enforcement Integration.

**We have transparent content moderation. Are we compliant?**

Transparency is necessary but not sufficient. If you're removing lawful content based on viewpoint, you're operating Suppression Infrastructure regardless of transparency.

**What about payment processors?**

If you deny financial services based on the lawful content of expression rather than neutral financial risk criteria, you're operating Suppression Infrastructure. Stripe deplatforming creators for politics? Suppression. Stripe declining accounts with 40% chargeback rates? Fine.

**What if we sell some surveillance products but also do other things?**

If surveillance, data brokerage, or suppression tools generate >10% of your revenue, you fail the Material Business Activity test. No safe harbor regardless of size.

**What if a court strikes down Section 4?**

The intent is that the entire license is void. This is designed to prevent the "restrictions are unenforceable so I get Apache 2.0" attack.

**Can I set the commercial royalty higher than $10k/month?**

Yes. Specify the amount in your NOTICE file. Foundational projects might set $100k, $500k, or even $1M/month. The amount should be defensible as reasonable commercial value.

**Is this enforceable?**

Honestly? Some provisions may face challenges, and we won't know until it's tested. The primary function is signaling: compliance teams should flag this as high-risk regardless of ultimate enforceability. And if they ignore the flag? They've walked into a trap with audit consent, fee shifting, and retroactive royalties. Whether that trap holds up in court is the experiment.

---

## Using HPL-1.0

1. Copy `LICENSE` to your repository root
2. Create a `NOTICE` file with your parameters (see LICENSE Appendix B)
3. Add the boilerplate notice to source files (see LICENSE Appendix A)

### NOTICE File Parameters

| Parameter | Default | What It Does |
|-----------|---------|--------------|
| **Licensor Jurisdiction** | Washington, USA | Where disputes are litigated |
| **Contact Address** | (required) | Where deployment notices go |
| **Commercial Royalty Amount** | $10,000/month | Royalty if injunction denied |
| **Pre-Approved Auditors** | (optional) | Auditors you can select unilaterally |

### Package Manager Examples

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
| `NOTICE` | Attribution notice and licensor parameters (create from template in LICENSE) |
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
