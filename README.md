# compliant-skills

Two Claude Code skills for creating and reviewing a legally compliant German Impressum (DDG § 5).

> **Legal disclaimer:** These skills provide informational guidance based on public German law. They do not constitute legal advice and are not a substitute for review by a licensed German attorney (Rechtsanwalt).

## Skills

### imprint-creator
Guides you step-by-step through a structured interview and generates a ready-to-publish German Impressum. Branches on legal form to ask only the fields that apply to your business, covering DDG § 5, MStV § 18, VSBG, and ODR obligations.

### imprint-reviewer
Audits an existing Impressum against the full DDG § 5 checklist, infers your legal form to avoid false positives, and outputs a structured gap report with corrective text and an overall risk score.

## Install

```bash
# Both skills
npx skills add NojNo/compliant-skills

# Individually
npx skills add NojNo/compliant-skills/tree/main/skills/imprint-creator
npx skills add NojNo/compliant-skills/tree/main/skills/imprint-reviewer
```

