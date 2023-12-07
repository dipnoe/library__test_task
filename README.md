# library__test_task
>Для запуска приложения рекомендуется использовать утилиту `make`

Данный проект является тестовым заданием.

## Установка и запуск
1. Склонируйте git-репозиторий
   ```bash
   git clone git@github.com:dipnoe/library__test_task.git
   ```
2. зайдите в корень проекта командой `cd <путь-до-дирректории-проекта>` 
3. Скопируйте файл `.env.dist` в файл `.env`:
    ```bash
    cp .env.dist .env
    ```

4. Настройте недостающие переменные окружения в файле `.env`.
> Необходимо заполнить доступы для работы с почтовым сервисом:
> EMAIL_HOST,
> EMAIL_PORT,
> EMAIL_HOST_USER
> EMAIL_HOST_PASSWORD

5. Запуск приложения с помощью `docker-compose` (используется утилита `make`)
    ```bash
   make docker-up
    ```
6. Проверка работоспособности приложения
> Проверить работоспосоность приложения можно с помощью подготовленной коллекции postman,
> для этого необходимо импортировать файл `postman/library_collection.json` в свой postman 
> ([Как импортировать коллекцию в postman](https://docs.rkeeper.ru/api/testirovanie-zaprosov-v-postman-87557103.html#id-%D0%A2%D0%B5%D1%81%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5%D0%B7%D0%B0%D0%BF%D1%80%D0%BE%D1%81%D0%BE%D0%B2%D0%B2Postman-%D0%98%D0%BC%D0%BF%D0%BE%D1%80%D1%82%D0%BA%D0%BE%D0%BB%D0%BB%D0%B5%D0%BA%D1%86%D0%B8%D0%B9)).
> Коллекция не требует дополнительной конфигурации, а так же, в запросах используется автоматическая
> подстановка случайных мок-значений для удобства. Первым делом следует выполнить запрос `Create Book`,
> чтобы другие запросы имели возможность работать с переменной `{{book_id}}`. В запросе `Create User` следует
> использовать реальный `email` вместо указанного в теле запроса.


### Команды для удобства работы с Docker

Для сборки и запуска проекта в Docker используйте команду:
```bash
make docker-up
```

Для остановки Docker-контейнеров:
```bash
make docker-down
```

Для ручного входа в контейнер django-приложения:
```bash
make docker-exec
```

Для создания суперпользователя:
```bash
make create-su
```

### Приложение доступно по адресу:
http://127.0.0.1:8001
