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

**Purpose:** Interview the user and produce a ready-to-publish German Impressum that satisfies TMG § 5 and DDSG requirements.

### SKILL.md frontmatter

```yaml
---
name: imprint-creator
description: Guides step-by-step through creating a legally compliant German Impressum (Impressumspflicht) for a new business, covering TMG § 5, VAT ID, trade register, and editorial responsibility.
---
```

### Instruction content to include

- Explain the legal basis: Telemediengesetz (TMG) § 5 for commercial websites; RStV § 55 for editorial/journalistic content.
- Ask the user a structured set of questions:
  1. Legal form of the business (Einzelunternehmen, GbR, UG, GmbH, AG, etc.)
  2. Full legal name of the owner / company name
  3. Physical street address (no PO box — legally required)
  4. Email address (must be reachable within 24 hours per TMG)
  5. Phone number (strongly recommended; some courts require it)
  6. Umsatzsteuer-ID (VAT ID) if registered — format: DE + 9 digits
  7. Handelsregisternummer + Registergericht if applicable (GmbH, UG, AG require this)
  8. Vertretungsberechtigter (authorized representative) for companies
  9. Aufsichtsbehörde (supervisory authority) if operating in regulated industries (e.g., financial services, healthcare)
  10. Berufshaftpflicht / professional body membership if applicable
  11. Verantwortlicher i.S.d. § 55 Abs. 2 RStV if publishing journalistic content
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
description: Reviews an existing German Impressum for legal compliance gaps under TMG § 5 and RStV § 55, flags missing or malformed fields, and suggests corrective text.
---
```

### Instruction content to include

- Ask the user to paste the full Impressum text (or provide a file path).
- Check for the presence and validity of each required field:
  - Full name / company name
  - Street address (no PO box)
  - Reachable email
  - Phone number
  - VAT ID format (DE + 9 digits) if mentioned
  - Handelsregister entry if business type requires it
  - Representative name for registered companies
  - Supervisory authority for regulated professions
  - Editorial responsibility clause if applicable
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

> This skill provides informational guidance based on public German law (TMG § 5, RStV § 55). It does not constitute legal advice. Have your Impressum reviewed by a licensed German attorney (Rechtsanwalt) for your specific business situation.

---

## Sources

- [skills.sh — Open Agent Skills Directory](https://www.skills.sh)
- [vercel-labs/skills on GitHub](https://github.com/vercel-labs/skills)
- [skills.sh FAQ](https://skills.sh/docs/faq)
- [Extend Claude with skills — Claude Code Docs](https://code.claude.com/docs/en/skills)
- [How to create custom Skills — Claude Help Center](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills)
