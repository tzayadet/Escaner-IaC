# Escáner IaC

Escáner estático ligero para localizar patrones habituales de secretos expuestos en archivos de infraestructura como código y configuración.

## Qué comprueba

- Identificadores AWS con prefijos `AKIA` y `ASIA`.
- Cabeceras de claves privadas.
- Asignaciones de contraseñas o secretos en texto.

Extensiones: Terraform, YAML, JSON, shell, TOML, INI y archivos `.env`.

## Requisitos

Python 3.11+. No requiere dependencias externas.

## Uso

```bash
python scan.py .
python scan.py /ruta/al/repositorio
```

La salida es JSON. Devuelve código de salida `1` si encuentra coincidencias y `0` si no detecta patrones.

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

Showcase estático con un informe ficticio: https://tzayadet.github.io/Escaner-IaC/

La demo no analiza archivos ni envía información. El escáner real es una herramienta CLI local basada en patrones heurísticos.
