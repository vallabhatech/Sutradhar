# Changelog

All notable changes to Sutradhar are documented here.

## [Unreleased] — 2026-09-30

### Documentation
- Cleaned up the roadmap so completed foundation/authentication work is separated from planned intelligence features.
- Added the repository's MIT license file and linked it from the README.
- Established this changelog as the running project history.

### Engineering
- Reviewed the repository structure, Docker setup, CI workflows, backend dependency set, and frontend package configuration.
- Preserved the existing FastAPI + Next.js + PostgreSQL architecture while keeping future OCR, investigation, graph, and AI capabilities clearly scoped.

### Security
- Kept secrets out of source control through environment templates.
- Documented the need to replace development credentials and secrets before production use.
