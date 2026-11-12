# IaC Secret Scanner

Escáner estático en Python para localizar posibles secretos expuestos en archivos de infraestructura como código y configuración.

[![Tests](https://github.com/tzayadet/Escaner-IaC/actions/workflows/tests.yml/badge.svg)](https://github.com/tzayadet/Escaner-IaC/actions/workflows/tests.yml) · [![Docker](https://github.com/tzayadet/Escaner-IaC/actions/workflows/container-build.yml/badge.svg)](https://github.com/tzayadet/Escaner-IaC/actions/workflows/container-build.yml)

**Demo:** [ver showcase](docs/index.html) · **Código:** [iac_secret_scanner.py](iac_secret_scanner.py)

> La demo muestra un informe ficticio. El análisis real se ejecuta localmente y no envía archivos ni resultados a ningún servidor.

## Qué detecta

- Identificadores AWS con prefijos habituales `AKIA` y `ASIA`.
- Cabeceras de claves privadas.
- Asignaciones de contraseñas y secretos en texto.
- Archivos Terraform, YAML, JSON, shell, TOML, INI y `.env`.

## Requisitos y uso

Python 3.11 o superior. No requiere paquetes externos.

```bash
python iac_secret_scanner.py .
python iac_secret_scanner.py /ruta/al/repositorio
```

La salida es JSON. Devuelve código de salida `1` si encuentra coincidencias y `0` si no detecta patrones.

Con Docker:

```bash
docker build -t iac-secret-scanner .
docker run --rm -v "$PWD:/workspace:ro" iac-secret-scanner /workspace
```

## Limitaciones

El análisis se basa en patrones y expresiones regulares. Puede producir falsos positivos y negativos; no valida credenciales ni interpreta semánticamente Terraform. No modifica los archivos analizados.

Si aparece una credencial real, debe revocarse o rotarse. Ejecuta el escáner únicamente sobre repositorios que tengas autorización para revisar.

## Estado de la demo

El showcase estático se encuentra en `docs/`. La publicación de GitHub Pages sigue pendiente de activar en **Settings → Pages** y de configurar la variable de Actions `ENABLE_PAGES=true`.

## Licencia

Consulta [LICENSE](LICENSE).
