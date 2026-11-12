# IaC Secret Scanner

A local Python scanner for identifying potential exposed secrets in infrastructure-as-code and configuration files. It produces structured JSON output and can be used as a lightweight CI gate.

<p align="center">
  <a href="https://tzayadet.github.io/Escaner-IaC/"><img src="https://img.shields.io/badge/SHOWCASE-OPEN-00a86b?style=flat-square" alt="Showcase"></a>
  <a href="https://github.com/tzayadet/Escaner-IaC"><img src="https://img.shields.io/badge/SOURCE-GITHUB-161b22?style=flat-square&logo=github" alt="Source"></a>
</p>

[![Tests](https://github.com/tzayadet/Escaner-IaC/actions/workflows/tests.yml/badge.svg)](https://github.com/tzayadet/Escaner-IaC/actions/workflows/tests.yml) · [![Container build](https://github.com/tzayadet/Escaner-IaC/actions/workflows/container-build.yml/badge.svg)](https://github.com/tzayadet/Escaner-IaC/actions/workflows/container-build.yml)

## What it does

- Detects common AWS access-key prefixes such as `AKIA` and `ASIA`.
- Identifies private-key headers and password/secret assignments.
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

## Showcase

The public page uses illustrative findings only. Actual scanning runs locally from the CLI; the browser page does not inspect repositories or files.

## Detection limits

Detection is pattern-based. False positives and false negatives are possible; the scanner does not validate credentials or semantically interpret Terraform. It does not modify scanned files.

If a real credential is exposed, revoke or rotate it. Only scan repositories and files you are authorized to assess.

## Deployment

The Pages workflow publishes `docs/`. GitHub Pages must be configured to use GitHub Actions, and the repository variable `ENABLE_PAGES=true` must be set before deployment.

## License

See [LICENSE](LICENSE) for the repository's licensing terms.
