FROM python:3.12-slim

WORKDIR /app

COPY ./requirements.txt .

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY ./src .

ENV PYTHONPATH=/app

CMD ["fastapi", "run", "main.py"]