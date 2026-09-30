# Changelog

All notable changes to Sutradhar are documented here.

## 2026-09-30 — Repository modernization

### Documentation
- `ef40094` — refreshed roadmap and licensing documentation.
- `806df5b` — added the MIT license.
- `2b77726` — added this changelog.
- `8cd54e2` — documented local environment setup for Docker development.

### Security
- `ea8c765` — added scheduled and push/PR CodeQL analysis for Python and JavaScript/TypeScript.
- `fe81a47` — moved Docker Compose database credentials and application secrets to environment configuration.
- `9a8cc53` — aligned the backend environment template with the secure configuration model.

### CI/CD
- `eb795a3` — restricted workflow permissions and added a frontend production build check.
- `0d53bfa` — changed container publishing to run only for version tags and use read-only repository permissions.

### Infrastructure
- `3b8bd0f` — documented the Compose environment variables.
- Removed the obsolete Compose `version` declaration.
- Updated the PostgreSQL healthcheck to use the configured database identity.

## 2026-05-30
- `dd18189` — previous project file update.

## 2026-03-18
- `bd91f44` — initial repository commit.
