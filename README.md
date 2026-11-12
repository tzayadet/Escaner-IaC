<p align="center">
  <img src="https://img.shields.io/badge/SECURITY_ENGINEERING-IAC_SECRET_SCANNER-101010?style=for-the-badge&labelColor=050805&color=00FF41" alt="IaC Secret Scanner"/>
  <img src="https://img.shields.io/badge/PYTHON-STATIC_ANALYSIS-101010?style=for-the-badge&logo=python&logoColor=00FF41" alt="Python static analysis"/>
</p>

# IaC Secret Scanner

Escáner estático en Python para localizar posibles secretos expuestos en archivos de infraestructura como código y configuración. Analiza archivos localmente y genera un informe JSON; no envía el contenido a ningún servidor.

<p align="center">
  <a href="https://tzayadet.github.io/Escaner-IaC/"><strong>LIVE SHOWCASE ↗</strong></a> ·
  <a href="https://github.com/tzayadet/Escaner-IaC"><strong>SOURCE CODE</strong></a>
</p>

[![Tests](https://github.com/tzayadet/Escaner-IaC/actions/workflows/tests.yml/badge.svg)](https://github.com/tzayadet/Escaner-IaC/actions/workflows/tests.yml) · [![Docker](https://github.com/tzayadet/Escaner-IaC/actions/workflows/container-build.yml/badge.svg)](https://github.com/tzayadet/Escaner-IaC/actions/workflows/container-build.yml)

> El showcase contiene un informe ficticio. El análisis real se ejecuta desde la CLI.

## What it does

- Detecta identificadores AWS con prefijos habituales `AKIA` y `ASIA`.
- Localiza cabeceras de claves privadas.
- Busca asignaciones de contraseñas y secretos en texto.
- Analiza Terraform, YAML, JSON, shell, TOML, INI y archivos `.env`.
- Devuelve resultados estructurados en JSON y códigos de salida útiles para CI.

## Quick start

**Requirements:** Python 3.11+. No external Python dependencies.

```bash
python iac_secret_scanner.py .
python iac_secret_scanner.py /path/to/repository
```

**Docker**

```bash
docker build -t iac-secret-scanner .
docker run --rm -v "$PWD:/workspace:ro" iac-secret-scanner /workspace
```

El proceso devuelve código de salida `1` si encuentra coincidencias y `0` si no detecta patrones.

## Project layout

| Path | Purpose |
|---|---|
| `iac_secret_scanner.py` | Motor de análisis estático |
| `docs/` | Showcase con resultados de ejemplo |
| `tests/` | Pruebas automatizadas |
| `.github/workflows/` | CI, build de contenedor y Pages |

## Detection limits

La detección se basa en patrones y expresiones regulares. Puede producir falsos positivos y negativos; no valida credenciales ni interpreta semánticamente Terraform. No modifica los archivos analizados.

Si aparece una credencial real, revócala o rótala. Ejecuta el escáner únicamente sobre repositorios que tengas autorización para revisar.

## Deployment

GitHub Pages publica el contenido de `docs/` mediante `.github/workflows/pages.yml`. Requiere configurar Pages con GitHub Actions y establecer la variable `ENABLE_PAGES=true`.

## License

See [LICENSE](LICENSE).
