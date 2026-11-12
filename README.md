# IaC Secret Scanner

Escáner estático ligero para localizar patrones habituales de secretos expuestos en archivos de infraestructura como código y configuración.

[![Python tests](https://github.com/tzayadet/Escaner-IaC/actions/workflows/tests.yml/badge.svg)](https://github.com/tzayadet/Escaner-IaC/actions/workflows/tests.yml) · [![Container build](https://github.com/tzayadet/Escaner-IaC/actions/workflows/container-build.yml/badge.svg)](https://github.com/tzayadet/Escaner-IaC/actions/workflows/container-build.yml)

## Qué comprueba

- Identificadores AWS con prefijos `AKIA` y `ASIA`.
- Cabeceras de claves privadas.
- Asignaciones de contraseñas o secretos en texto.

Extensiones: Terraform, YAML, JSON, shell, TOML, INI y archivos `.env`.

## Requisitos

Python 3.11+. No requiere dependencias externas.

## Uso

```bash
python iac_secret_scanner.py .
python iac_secret_scanner.py /ruta/al/repositorio
```

La salida es JSON. Devuelve código de salida `1` si encuentra coincidencias y `0` si no detecta patrones. Omite enlaces simbólicos y no sigue rutas que salgan del directorio seleccionado.

## Docker

```bash
docker build -t iac-scanner .
docker run --rm -v "$PWD:/workspace:ro" iac-scanner /workspace
```

## Limitaciones

Es un detector heurístico basado en expresiones regulares. Puede generar falsos positivos y negativos; no valida credenciales ni analiza semánticamente Terraform. No modifica los archivos. Si detectas una credencial real, rótala y elimina su exposición del historial cuando proceda.

Utilízalo únicamente en repositorios que tengas autorización para analizar.

## Licencia

Consulta [LICENSE](LICENSE).


## Demo y documentación visual

Showcase estático preparado en `docs/` con un informe ficticio. GitHub Pages aún no está habilitado para este repositorio; la demo no debe considerarse publicada. Cuando se active Pages en **Settings → Pages → Build and deployment → Source → GitHub Actions**, configura la variable `ENABLE_PAGES=true` en **Settings → Secrets and variables → Actions → Variables**.

La demo no analiza archivos ni envía información. El escáner real es una herramienta CLI local basada en patrones heurísticos.
