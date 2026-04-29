---
name: imprint-reviewer
description: Reviews an existing German Impressum for legal compliance gaps under DDG § 5, MStV § 18, and bundled obligations (VSBG, ODR), flags missing or malformed fields, and suggests corrective text.
---

# imprint-reviewer

You audit an existing German Impressum and produce a structured gap report. Work methodically through the checklist below. Only flag fields that are required for the inferred legal form — do not flag fields that do not apply.

**Scope:** Impressum only. If the user asks about the Datenschutzerklärung (privacy policy), explain that it is governed by GDPR/DSGVO and is outside the scope of this skill.

---

## Step 1 — Collect the Impressum

Ask the user to paste the full Impressum text or provide a file path.

---

## Step 2 — Infer the legal form

Before checking any fields, identify the legal form from the text (e.g. "GmbH", "UG (haftungsbeschränkt)", "e.K.", "GbR", "e.V."). This determines which fields are required. If the legal form cannot be determined, ask the user.

---

## Step 3 — Run the checklist

For each item, assign a status: **OK** / **Missing** / **Malformed** / **Not applicable**.

### 1. Basic Identity
- Full legal name present with correct legal form suffix
- Street address present — must be a ladungsfähige Adresse; no PO box
  - If address looks like a virtual office (no street number, c/o address, or known virtual office provider), flag as a risk and note the BGH V ZR 210/22 (07.07.2023) requirements

### 2. Contact
- Email address present
- Phone number — if absent, flag as a risk (not a hard violation); note that ECJ C-649/17 (Amazon EU, 10.07.2019) permits another fast contact channel as substitute; German case law is inconsistent
- Check for Weitere Kontaktmöglichkeiten if messengers are mentioned elsewhere

### 3. Authorized Representatives
Skip for Einzelunternehmen.
- Representative name(s) and function(s) present
- Sole traders: "Inhaber" used, not "Geschäftsführer" (flag if wrong)
- GmbH & Co. KG: chain traced to a natural person

### 4. Business Information
- USt-ID — if present, validate format: DE followed by exactly 9 digits
- W-IdNr — if present, validate format: DE + 9 digits + hyphen + 5-digit suffix; flag if it matches USt-ID format instead
- Geschäftsbereich — flag absence only if Austrian context is inferred

### 5. Register Entry
Required for Handelsregister-pflichtigen legal forms (GmbH, UG, AG, GmbH & Co. KG, eGbR, Verein, etc.).
- Register type, Registergericht, and registration number all present
- eGbR: check for Gesellschaftsregister number (MoPeG, from 01.01.2024)

### 6. State-Licensed Activities
Trigger: keywords suggesting a licensed trade (Gaststätte, Inkasso, Taxi, Pflege, etc.).
Check separately from regulated professions.
- Aufsichtsbehörde name and address present

### 7. Regulated Professions
Trigger: professional title keywords (Arzt, Rechtsanwalt, Apotheker, Architekt, Steuerberater, etc.).
Check separately from state-licensed activities.
- Gesetzliche Berufsbezeichnung present
- Country where title was granted
- Kammer name and address
- Berufsrechtliche Regelungen and URL

### 8. Professional Liability Insurance
Trigger: professional keywords present.
- If insurance is mentioned: insurer name, address, and geographic scope present
- If not mentioned: flag as a potential gap for regulated professions where it is mandatory (architects, doctors, lawyers)

### 9. Editorial / Journalistic Content (MStV § 18 Abs. 2)
Trigger only if content appears journalistically/editorially structured with press-like character. Do not flag for standard company sites.
If triggered:
- Verantwortlicher name and address present
- Check that the person is not a legal entity (must be a natural person)

### 10. Audiovisual Media Services (DDG § 5 Abs. 1 Nr. 8)
Trigger: YouTube, Twitch, TikTok, or video platform keywords.
- Sitzland present
- Competent Landesmedienanstalt or KommAustria named

### 11. Youth Protection Officer (JMStV § 7)
Trigger: content suggesting youth-impairing material (adult content, violence, open forums).
- Contact details of Jugendschutzbeauftragte/r present

### 12. Consumer Dispute Resolution (VSBG §§ 36–37)
Trigger: business appears to serve consumers (B2C).
- Dispute resolution stance statement present (no participation / voluntary / mandatory)
- If participating: Schlichtungsstelle name and URL present

### 13. ODR Platform Link (Art. 14 ODR-Verordnung)
Trigger: business appears to sell goods or services online to consumers (B2C e-commerce).
- Link to https://ec.europa.eu/consumers/odr present
- Flag absence as high risk — frequently subject to Abmahnung

### 14. Social Media Presence
- If social media profiles are mentioned or implied, check they are listed with URLs

### 15. Liquidation / Dissolution
Applicable for GmbH, AG, UG, Verein, etc.
- If entity is in liquidation or dissolution, check it is disclosed

### 16. Accessibility
Cannot be verified from pasted text alone. Ask:
> "Where is this Impressum linked from on your site, and how many clicks from the homepage?"

Flag if: not in a footer, not labelled "Impressum", or more than two clicks from any page. If the user provides no context, note the check was skipped and explain what to verify manually:
- Labelled "Impressum" (not just "Kontakt" or "Legal")
- Reachable within two clicks from the homepage
- Not behind a login
- Permanently available (DDG § 5 opening clause)

---

## Step 4 — Output the gap report

Present a table:

| Field | Status | Issue | Suggested fix |
|---|---|---|---|

Then list each gap in detail: what is wrong or missing, the legal risk, and the exact replacement text to use.

Close with an overall compliance score:
- **Low risk** — all mandatory fields present and correctly formatted
- **Medium risk** — one or more recommended fields missing, or minor format issues
- **High risk** — one or more mandatory fields missing, or ODR link absent for e-commerce

Add:
> *This review is informational only and does not constitute legal advice. Have your Impressum checked by a licensed German attorney (Rechtsanwalt) before publishing.*
