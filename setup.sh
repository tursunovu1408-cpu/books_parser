#!/bin/bash

echo "=== Установка проекта Books Parser ==="

# Создаём виртуальное окружение
python3 -m venv venv

# Активируем его
source venv/bin/activate

# Обновляем pip
pip install --upgrade pip

# Устанавливаем библиотеки
pip install -r requirements.txt

echo ""
echo "=== Установка завершена! ==="
echo "Чтобы запустить парсер, выполни:"
echo "source venv/bin/activate"
echo "python books_parser.py"