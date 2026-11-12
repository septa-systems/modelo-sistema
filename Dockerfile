# Mesma imagem no local, no teste e na produção (docs/AMBIENTES.md)
FROM python:3.15-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

WORKDIR /app

ARG REQUISITOS=requirements.txt
COPY requirements.txt requirements-dev.txt ./
RUN pip install -r ${REQUISITOS}

COPY . .

# Não roda como root
RUN useradd --create-home app && chown -R app /app
USER app

EXPOSE 8000

# Produção: gera o CSS, junta os arquivos estáticos, aplica migrations e sobe o gunicorn
CMD ["sh", "-c", "python manage.py tailwind build && python manage.py collectstatic --noinput && python manage.py migrate --noinput && gunicorn config.wsgi --bind 0.0.0.0:${PORT:-8000} --workers 3"]
