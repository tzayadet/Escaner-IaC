# IaC Secret Scanner

A local Python scanner for identifying potential exposed secrets in infrastructure-as-code and configuration files. It produces structured JSON output and CI-friendly exit codes.

<p align="center">
  <a href="https://github.com/tzayadet/Escaner-IaC/blob/main/docs/index.html"><img src="https://img.shields.io/badge/SHOWCASE-SOURCE-00a86b?style=flat-square" alt="Showcase source"></a>
  <a href="https://github.com/tzayadet/Escaner-IaC"><img src="https://img.shields.io/badge/SOURCE-GITHUB-161b22?style=flat-square&logo=github" alt="Source"></a>
</p>

[![Tests](https://github.com/tzayadet/Escaner-IaC/actions/workflows/tests.yml/badge.svg)](https://github.com/tzayadet/Escaner-IaC/actions/workflows/tests.yml) · [![Container build](https://github.com/tzayadet/Escaner-IaC/actions/workflows/container-build.yml/badge.svg)](https://github.com/tzayadet/Escaner-IaC/actions/workflows/container-build.yml)

## Features

- Detects common AWS access-key prefixes such as `AKIA` and `ASIA`.
- Identifies GitHub personal-access-token patterns, Google API keys and Slack tokens.
- Identifies private-key headers and password/secret assignments.
- Skips individual files larger than 5 MB to keep local scans bounded.
- Scans Terraform, YAML, JSON, shell, TOML, INI and `.env` files.
- Produces structured JSON findings and CI-friendly exit codes.
- Analyses files locally without uploading their contents.

## Run locally

**Requirements:** Python 3.11 or later. No third-party Python dependencies are required.

```bash
python iac_secret_scanner.py .
python iac_secret_scanner.py /path/to/repository
```

## Docker

```bash
docker build -t iac-secret-scanner .
docker run --rm -v "$PWD:/workspace:ro" iac-secret-scanner /workspace
```

The scanner exits with code `1` when matches are found and `0` when no patterns are detected.

## Project structure

| Path | Purpose |
|---|---|
| `iac_secret_scanner.py` | Static scanning engine |
| `docs/` | Showcase with synthetic findings |
| `tests/` | Automated tests |
| `.github/workflows/` | CI, container build and Pages workflow |

## Detection limits

Detection is pattern-based. False positives and false negatives are possible; the scanner does not validate credentials or semantically interpret Terraform. It does not modify scanned files.

If a real credential is exposed, revoke or rotate it. Only scan repositories and files you are authorised to assess.

## Showcase and deployment

The [live showcase](https://tzayadet.github.io/Escaner-IaC/) uses illustrative findings only. It does not inspect repositories or files in the browser.

## License

See [LICENSE](LICENSE) for the repository's licensing terms.
