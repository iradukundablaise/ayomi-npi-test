
FROM python:3.9

WORKDIR /app

COPY ./app/backend/requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY ./app/backend /app

CMD ["fastapi", "run", "main.py", "--port", "8080"]