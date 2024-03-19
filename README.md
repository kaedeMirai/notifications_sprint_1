# Проектная работа 10 спринта

## Где найти код?
1. [10 sprint](https://github.com/Munewxar/notifications_sprint_1) - здесь хранится код заданий 10 спринта

## Ссылка на документацию api

Документация API сервиса уведомлений

1. http://0.0.0.0:8338/api/openapi

Документация API для генерации тестовых данных

2. http://0.0.0.0:8555/api/openapi

## Инструкция по запуску проекта
1. Склонировать репозиторий:

   ```
   git clone https://github.com/Munewxar/notifications_sprint_1
   ```
2. Скопировать .env.example в .env (либо переименовать .env.example) и заполнить их в следующих директориях:

    /notifications_service/api_service/
   
    /notifications_service/worker/

4. В командной строке запустить проект:

    ```
    make api_build
    make mock_data_api_build
    make worker_build

    make run
    ```
