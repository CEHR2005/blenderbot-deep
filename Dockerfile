# Используйте официальный образ Python
FROM python:3.8-slim-buster

# Установите рабочую директорию в /app
WORKDIR /app

# Скопируйте текущую директорию в рабочую директорию /app
COPY . /app

# Установите необходимые библиотеки
RUN pip install --no-cache-dir transformers torch
