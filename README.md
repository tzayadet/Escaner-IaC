<p align="center">
  <img src="https://img.shields.io/badge/SECURITY-IaC_SECRET_SCANNER-101010?style=for-the-badge&labelColor=050805&color=00FF41" alt="IaC Secret Scanner"/>
  <img src="https://img.shields.io/badge/PYTHON-STATIC_ANALYSIS-101010?style=for-the-badge&labelColor=050805&logo=python&logoColor=00FF41" alt="Python static analysis"/>
</p>

# IaC Secret Scanner

A lightweight Python scanner for common exposed-secret patterns in infrastructure-as-code and configuration files. It produces JSON findings and CI-friendly exit codes, without uploading scanned content.

<p align="center">
  <a href="https://tzayadet.github.io/Escaner-IaC/"><strong>LIVE DEMO ↗</strong></a> ·
  <a href="https://github.com/tzayadet/Escaner-IaC"><strong>SOURCE CODE</strong></a>
</p>

[![Tests](https://github.com/tzayadet/Escaner-IaC/actions/workflows/tests.yml/badge.svg)](https://github.com/tzayadet/Escaner-IaC/actions/workflows/tests.yml) · [![Container build](https://github.com/tzayadet/Escaner-IaC/actions/workflows/container-build.yml/badge.svg)](https://github.com/tzayadet/Escaner-IaC/actions/workflows/container-build.yml) · [![Pages](https://github.com/tzayadet/Escaner-IaC/actions/workflows/pages.yml/badge.svg)](https://github.com/tzayadet/Escaner-IaC/actions/workflows/pages.yml)

## Overview

- Detects common AWS access-key, GitHub token, Google API key and Slack token patterns.
- Identifies private-key headers and password/secret assignments.
- Scans Terraform, YAML, JSON, shell, TOML, INI and `.env` files.
- Skips dependency directories, symbolic links and files larger than 5 MB.
- Emits relative file paths and structured JSON findings.
- Returns exit code `1` when matches are found and `0` when none are detected.

## Run locally

**Requirements:** Python 3.11+. No third-party Python packages are required.

```bash
python iac_secret_scanner.py .
python iac_secret_scanner.py /path/to/repository
```

## Docker

```bash
docker build -t iac-secret-scanner .
docker run --rm -v "$PWD:/workspace:ro" iac-secret-scanner /workspace
```

Mounting the target directory read-only is recommended.

## Project structure

| Path | Purpose |
|---|---|
| `iac_secret_scanner.py` | Static scanning engine and CLI |
| `docs/` | Showcase with synthetic findings |
| `tests/` | Automated regression tests |
| `.github/workflows/` | Test, container and Pages automation |

## Showcase

The [showcase source](docs/index.html) uses illustrative findings only. It does not inspect repositories or files in the browser. The showcase is published separately from the local tool. It is a static demonstration and does not execute the application.

## Validation

Run the tests with:

```bash
python -m unittest discover -s tests -v
```

GitHub Actions runs the unit tests and builds the container image.

## Detection limits

Detection is pattern-based. False positives and false negatives are possible; the scanner does not validate credentials, parse Terraform semantics or replace dedicated secret-scanning products. It does not modify scanned files. A match is an indicator for review, not proof that a credential is active.

If a real credential is exposed, revoke or rotate it. Only scan repositories and files you are authorised to assess.

## License

See [LICENSE](LICENSE).
