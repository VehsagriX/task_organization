# Используем Python 3.12 как базовый образ
FROM python:3.12-slim

# Устанавливаем рабочую директорию в контейнере
WORKDIR /app


ENV PYTHONUNBUFFERED=1

COPY requirements.txt .

# Устанавливаем зависимости из requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Копируем все файлы в контейнер

COPY . .



# Открываем порт для приложения
EXPOSE 8000

# Команда для выполнения миграций и запуска FastAPI
CMD ["sh", "-c", "alembic upgrade head && uvicorn src.main:app --host 127.0.0.1 --port 8000"]