# Используем базовый образ Python
FROM python:3.12-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем requirements.txt и устанавливаем зависимости
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем все файлы проекта
COPY . .

# Указываем порт, который будет использоваться контейнером
EXPOSE 5000

# Запускаем сервер gRPC и Flask-приложение
CMD ["sh", "-c", "python grpc_server.py & gunicorn -w 4 -b 0.0.0.0:5000 wsgi:app"]
