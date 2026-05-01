# GDPR Production Bundle

This bundle contains the full implementation starting point for the GDPR skills architecture.

## Included

- `docs/gdpr-audit-skill-plan-vnext.md` — clean vNext plan
- `gdpr-shared/controls/control-catalog.json` — full 131-control r3 catalogue
- `gdpr-shared/profiles/stages/` — generated early/growth/enterprise profiles
- `gdpr-shared/profiles/roles/` — role output profiles
- `gdpr-shared/scripts/` — control engine, guard, condition evaluator, decision layer, router
- `gdpr-shared/watcher/` — normative-source watcher scaffold
- `gdpr-guide/`, `gdpr-auditor-public/`, `gdpr-auditor-app/` — skill skeletons

## Stage counts

```json
{
  "early": 24,
  "growth": 111,
  "enterprise": 131
}
```

## Validate

```bash
cd gdpr_production_bundle
PYTHONPATH=gdpr-shared/scripts python gdpr-shared/scripts/validate_catalog.py gdpr-shared/controls/control-catalog.json
```

## Catalogue SHA-256

`262a1bb6ae9c611af473a5c9d956da2a353b9f01be06c8dbfc26192b6a27192a`
