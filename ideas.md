# Compliant Imprint Skills — Launch Plan

## Overview

Two Claude Code skills published to a public GitHub repo and discoverable via skills.sh:

1. **imprint-creator** — guides the user through generating a legally compliant German Impressum
2. **imprint-reviewer** — audits an existing Impressum for legal gaps

**Field reference:** [`mandatory.md`](./mandatory.md) is the canonical source for all required fields, legal triggers, formats, and citations. Both skills must stay in sync with it.

---

## Repository Structure

```
compliant-skills/
├── skills/
│   ├── imprint-creator/
│   │   └── SKILL.md
│   └── imprint-reviewer/
│       └── SKILL.md
└── README.md
```

```bash
npx skills add NojNo/compliant-skills/tree/main/skills/imprint-creator
npx skills add NojNo/compliant-skills/tree/main/skills/imprint-reviewer
# or both at once:
npx skills add NojNo/compliant-skills
```

---

## Skill 1: imprint-creator

**Purpose:** Interview the user and produce a ready-to-publish German Impressum.

**Scope:** Impressum only. The Datenschutzerklärung (GDPR/DSGVO) is a separate document outside this skill's scope.

### SKILL.md frontmatter

```yaml
---
name: imprint-creator
description: Guides step-by-step through creating a legally compliant German Impressum for a new business, covering DDG § 5, MStV § 18, VAT ID, trade register, editorial responsibility, and consumer dispute resolution.
---
```

### Instruction approach

1. **Branch on legal form first** — determines which downstream fields apply. An Einzelunternehmen has no Handelsregisternummer or Vertretungsberechtigter; asking for them anyway makes the interview feel robotic.
2. **Work through mandatory.md sections 1–14 in order**, skipping fields not applicable to the stated legal form.
3. Also collect: ODR platform link (Art. 14 ODR-Verordnung) for B2C e-commerce, and Consumer Dispute Resolution stance (VSBG §§ 36–37) — both are outside DDG § 5 but commonly bundled and frequently subject to Abmahnung when missing.
4. Output the Impressum in structured German legal text. Flag any mandatory field that was left blank.
5. Remind the user this is a starting point and legal review by a Rechtsanwalt is recommended.

---

## Skill 2: imprint-reviewer

**Purpose:** Audit a pasted Impressum against the German legal checklist and output a gap report.

**Scope:** Impressum only. The Datenschutzerklärung (GDPR/DSGVO) is out of scope — note this if the user asks.

### SKILL.md frontmatter

```yaml
---
name: imprint-reviewer
description: Reviews an existing German Impressum for legal compliance gaps under DDG § 5, MStV § 18, and bundled obligations (VSBG, ODR), flags missing or malformed fields, and suggests corrective text.
---
```

### Instruction approach

1. **Infer the legal form from the text** before checking fields. Only flag fields required for the inferred form — do not flag fields that don't apply (status: Not applicable).
2. **Check against all mandatory.md sections** plus the two bundled obligations: ODR link (B2C e-commerce) and VSBG consumer dispute resolution stance.
3. **Accessibility check** cannot be verified from pasted text alone. Ask: "Where is this Impressum linked from on your site, and how many clicks from the homepage?" Flag if not in footer, not labelled "Impressum", or more than two clicks from any page. If no context is given, note the check was skipped.
4. Output a structured gap report: status per field (OK / Missing / Malformed / Not applicable), legal risk explanation, and suggested replacement text for each gap.
5. Conclude with an overall compliance score: low / medium / high risk.

---

## Steps to Launch on skills.sh

1. **Build locally** — write both SKILL.md files; test with `npx skills add ./skills/imprint-creator` and validate output quality in Claude Code.
2. **Publish** — repo is live at https://github.com/NojNo/compliant-skills; confirm installs with `npx skills add NojNo/compliant-skills`.
3. **Appear on skills.sh** — discovered automatically via install telemetry; drive early installs through German startup communities, legal-tech forums, and indie hacker channels to reach the trending board. Lead with the DDG compliance angle.
4. **Write README.md** — one-paragraph description per skill, install command front and centre, legal disclaimer.

---

## Legal Disclaimer to Include in Both Skills

> This skill provides informational guidance based on public German law (DDG § 5, MStV § 18 Abs. 2, VSBG §§ 36–37, ODR-Verordnung Art. 14). It does not constitute legal advice. Have your Impressum reviewed by a licensed German attorney (Rechtsanwalt) for your specific business situation.

---

## Sources

- [Mandatory Impressum Fields](./mandatory.md) — canonical field reference with legal citations
- [vercel-labs/skills on GitHub](https://github.com/vercel-labs/skills)
- [skills.sh FAQ](https://skills.sh/docs/faq)
- [Extend Claude with skills — Claude Code Docs](https://code.claude.com/docs/en/skills)
- [How to create custom Skills — Claude Help Center](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills)
