# Проект "Онлайн Кинотеатр"

## Сервис Notifications

Репозиторий для сервиса уведомлений, который обеспечивает API для приема событий по созданию уведомлений, воркер для отправки уведомлений через SMTP и другие каналы, а также шедулер для отправки отложенных уведомлений пользователям в удобное для них время.

## Содержание:

- [Django Admin Panel](https://github.com/kaedeMirai/new_admin_panel_sprint_1) - **Панель администратора для управления контентом: Удобный и интуитивно понятный интерфейс для управления фильмами, сеансами и другим контентом вашего кинотеатра.**
- [ETL](https://github.com/kaedeMirai/admin_panel_sprint_3) - **Перенос данных из PostgreSQL в ElasticSearch для реализации полнотекстового поиска.**
- [Auth](https://github.com/kaedeMirai/Auth_sprint_1-2) - **Аутентификация и авторизация пользователей на сайте с системой ролей.**
- [UGC](https://github.com/kaedeMirai/ugc_sprint_1) - **Сервис для удобного хранения аналитической информации и UGC.**
- [UGC +](https://github.com/kaedeMirai/ugc_sprint_2) - **Улучшение функционала UGC внедрением CI/CD процессов и настройкой системы логирования Setnry и ELK.**
- [Notification service](https://github.com/kaedeMirai/notifications_sprint_1) - **Отправка уведомлений пользователям о важных событиях и акциях в кинотеатре.**
- [Watch Together service]() - **Позволяет пользователям смотреть фильмы совместно в реальном времени, обеспечивая синхронизацию видео и чата.**

## Где найти код?
1. [10 sprint](https://github.com/kaedeMirai/notifications_sprint_1) - здесь хранится код заданий 10 спринта

## Ссылка на документацию api

Документация API сервиса уведомлений

1. http://0.0.0.0:8338/api/openapi

Документация API для генерации тестовых данных

2. http://0.0.0.0:8555/api/openapi

## Инструкция по запуску проекта
1. Склонировать репозиторий:

   ```
   git clone https://github.com/kaedeMirai/notifications_sprint_1
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