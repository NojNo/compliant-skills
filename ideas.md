# Compliant Imprint Skills — Launch Plan

## Overview

Two Claude Code skills published to a public GitHub repo and discoverable via skills.sh:

1. **imprint-creator** — guides the user through generating a legally compliant German Impressum
2. **imprint-reviewer** — audits an existing Impressum for legal gaps

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

Skills live under `skills/` so users can install each one individually:

```bash
npx skills add <github-user>/compliant-skills/tree/main/skills/imprint-creator
npx skills add <github-user>/compliant-skills/tree/main/skills/imprint-reviewer
```

Or install both at once:

```bash
npx skills add <github-user>/compliant-skills
```

---

## Skill 1: imprint-creator

**Purpose:** Interview the user and produce a ready-to-publish German Impressum that satisfies DDG § 5 requirements.

### SKILL.md frontmatter

```yaml
---
name: imprint-creator
description: Guides step-by-step through creating a legally compliant German Impressum (Impressumspflicht) for a new business, covering DDG § 5, VAT ID, trade register, and editorial responsibility.
---
```

### Instruction content to include

- Explain the legal basis: Digitale-Dienste-Gesetz (DDG) § 5 for all commercial digital services; MStV § 18 for editorial/journalistic content.
- Ask the user a structured set of questions:
  1. Legal form of the business (Einzelunternehmen, GbR, UG, GmbH, AG, etc.)
  2. Full legal name of the owner / company name
  3. Physical street address (no PO box — legally required)
  4. Email address enabling rapid electronic contact and direct communication (DDG § 5 Abs. 1 Nr. 2)
  5. Phone number (strongly recommended; some courts require it for "direct communication")
  6. Umsatzsteuer-ID (VAT ID) if registered — format: DE + 9 digits
  7. Wirtschafts-Identifikationsnummer if no VAT ID applies
  8. Handelsregisternummer + Registergericht if applicable (GmbH, UG, AG require this)
  9. Vertretungsberechtigter (authorized representative) for companies
  10. Aufsichtsbehörde (supervisory authority) if operating in regulated industries (e.g., financial services, healthcare)
  11. Berufskammer membership, official professional title, and applicable professional regulations if applicable
  12. Is the company currently in liquidation or dissolution? (must be disclosed per DDG § 5)
  13. Is this an audiovisual media service? If yes: country of establishment + competent regulatory authority
  14. Verantwortlicher i.S.d. § 18 Abs. 2 MStV if publishing journalistic/editorial content
- After gathering answers, output the Impressum in structured German legal text.
- Flag any fields the user left blank that are legally required.
- Remind user this is a starting point and legal review is recommended for edge cases.

---

## Skill 2: imprint-reviewer

**Purpose:** Audit a pasted or linked Impressum against the German legal checklist and output a gap report.

### SKILL.md frontmatter

```yaml
---
name: imprint-reviewer
description: Reviews an existing German Impressum for legal compliance gaps under DDG § 5 and MStV § 18, flags missing or malformed fields, and suggests corrective text.
---
```

### Instruction content to include

- Ask the user to paste the full Impressum text (or provide a file path).
- Check for the presence and validity of each required field per DDG § 5:
  - Full name / company name
  - Street address (no PO box)
  - Email enabling rapid electronic contact (DDG § 5 Abs. 1 Nr. 2)
  - Phone number
  - VAT ID (DE + 9 digits) or Wirtschafts-Identifikationsnummer
  - Handelsregister entry if business type requires it
  - Representative name for registered companies
  - Supervisory authority for regulated professions
  - Professional chamber, title, and regulations if applicable
  - Liquidation/dissolution status if applicable
  - Country of establishment + regulatory authority for audiovisual providers
  - Editorial responsibility clause (MStV § 18) if applicable
- Check accessibility: is the Impressum "leicht erkennbar und unmittelbar erreichbar" (DDG § 5 Abs. 1 opening clause)? Flag if it is buried or hard to find.
- Output a structured gap report:
  - Status per field: OK / Missing / Malformed
  - For each gap: explanation of the legal risk and suggested replacement text
- Conclude with an overall compliance score (low / medium / high risk).

---

## Steps to Launch on skills.sh

### 1. Build the skills locally

- Create the repo structure above.
- Write both SKILL.md files with the frontmatter and instructions documented here.
- Test each skill locally:
  ```bash
  npx skills add ./skills/imprint-creator
  npx skills add ./skills/imprint-reviewer
  ```
- Invoke each skill in Claude Code and validate the output quality.

### 2. Publish to GitHub

- Create a public GitHub repository named `compliant-skills`.
- Push the repo.
- Confirm both skills install cleanly via:
  ```bash
  npx skills add <github-user>/compliant-skills
  ```

### 3. Appear on skills.sh

- skills.sh discovers skills automatically via install telemetry — no manual submission needed.
- Drive early installs to get onto the trending/leaderboard lists:
  - Share the install command in relevant communities (indie hackers, German startup Slack groups, legal-tech forums).
  - Post a short writeup explaining the TMG compliance angle.

### 4. Write a clear README.md

- One-paragraph description of each skill.
- Install command front and center.
- Legal disclaimer: output is a starting point, not legal advice.

---

## Legal Disclaimer to Include in Both Skills

> This skill provides informational guidance based on public German law (Digitale-Dienste-Gesetz DDG § 5, Medienstaatsvertrag MStV § 18). It does not constitute legal advice. Have your Impressum reviewed by a licensed German attorney (Rechtsanwalt) for your specific business situation.

---

## Sources

- [skills.sh — Open Agent Skills Directory](https://www.skills.sh)
- [vercel-labs/skills on GitHub](https://github.com/vercel-labs/skills)
- [skills.sh FAQ](https://skills.sh/docs/faq)
- [Extend Claude with skills — Claude Code Docs](https://code.claude.com/docs/en/skills)
- [How to create custom Skills — Claude Help Center](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills)
