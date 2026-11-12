FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app
RUN useradd --create-home --uid 10001 appuser
COPY --chown=appuser:appuser scan.py .
USER appuser

ENTRYPOINT ["python", "scan.py"]
