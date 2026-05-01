# compliant-skills

Claude Code skills for German Impressum compliance and GDPR guidance.

> **Important — please read before using:**
> These skills provide structured informational guidance only. They do not constitute legal advice. All compliance decisions, risk assessments, and actions taken based on skill output are the sole responsibility of the user. The skill output is a starting point for review — not a conclusion. Always have your Impressum and privacy programme reviewed by a qualified legal professional (Rechtsanwalt / DPO / privacy counsel) before relying on it for compliance purposes.

---

## Impressum Skills (German DDG § 5)

### imprint-creator
Guides you step-by-step through a structured interview and generates a ready-to-publish German Impressum. Branches on legal form to ask only the fields that apply to your business, covering DDG § 5, MStV § 18, VSBG, and ODR obligations.

### imprint-reviewer
Audits an existing Impressum against the full DDG § 5 checklist, infers your legal form to avoid false positives, and outputs a structured gap report with corrective text and an overall risk score.

## GDPR Skills

### gdpr-guide
Advisory implementation guide for engineers, product managers, and DPOs. Works through legal basis, consent, data model, DSR workflows, and governance in a structured interview. Produces informational checklists — no pass/fail findings or compliance claims.

### gdpr-auditor-public
Audits a public-facing website or repository for GDPR compliance gaps across transparency, consent, data subject rights, and security. Produces control findings and a prioritised remediation report.

### gdpr-auditor-app
Authenticated GDPR audit of a live application using test credentials. Covers public surface, authenticated flows, and document intake. Includes an optional legal review packet formatted for counsel or DPO review.

---

## Install

```bash
# All skills
npx skills add NojNo/compliant-skills

# Impressum skills only
npx skills add NojNo/compliant-skills/tree/main/skills/imprint-creator
npx skills add NojNo/compliant-skills/tree/main/skills/imprint-reviewer

# GDPR skills
npx skills add NojNo/compliant-skills/tree/main/skills/gdpr-guide
npx skills add NojNo/compliant-skills/tree/main/skills/gdpr-auditor-public
npx skills add NojNo/compliant-skills/tree/main/skills/gdpr-auditor-app
```
