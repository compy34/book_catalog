# 1. Базовий образ Python
FROM python:3.11-slim

# 2. Робоча директорія всередині контейнера
WORKDIR /app

# 3. Копіюємо список залежностей і встановлюємо їх
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Копіюємо весь код проєкту в контейнер
COPY . .

# 5. Відкриваємо порт 5000 для доступу
EXPOSE 5000

# 6. Команда запуску застосунку
CMD ["python", "app.py"]