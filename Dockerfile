ARG PYTHON_VERSION=3.9.16

FROM python:${PYTHON_VERSION} as api

ENV PYTHONUNBUFFERED=1 \
    PYTHONIOENCODING=UTF-8 \
    MANIFEST_FILE_PATH=manifest.json \
    SLACK_TRIGGER="off" \
    SLACK_EMOJI=":cwai:" \
    SLACK_CHANNEL="#cwai" \
    SLACK_USERNAME="cwai" \
    LOG_LEVEL="INFO" \
    LISTEN_ADDR="0.0.0.0" \
    LISTEN_PORT=8000

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN find . -name '*.pyc' -type f -delete && \
    pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

COPY . /app/

EXPOSE 8000

CMD ["python", "src/app.py"]
