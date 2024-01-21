# API Календаря

Этот API предоставляет простой интерфейс для управления событиями в календаре. Он включает операции CRUD (создание, чтение, обновление, удаление) и предоставляет ограничения на максимальную длину заголовка и текста, а также запрещает добавление более одного события в день.

## Модель данных

Событие представлено следующими атрибутами:

**ID:** Уникальный идентификатор события.

**Дата:** Дата события в формате ГГГГ-ММ-ДД.

**Заголовок:** Краткое описание события, максимальная длина 30 символов.

**Текст:** Дополнительная информация о событии, максимальная длина 200 символов.

## Ограничения

Максимальная длина заголовка: 30 символов.

Максимальная длина текста: 200 символов.

Нельзя добавить больше одного события в день.

## API Интерфейс

Все эндпоинты API доступны по адресу /api/v1/calendar/.

**Добавление события (POST /api/v1/calendar/add_event):**

- Формат данных: "ГГГГ-ММ-ДД|заголовок|текст".

- Возвращает уникальный идентификатор нового события.

**Список событий (GET /api/v1/calendar/list_events):**

- Возвращает список всех событий.

**Чтение события (GET /api/v1/calendar/read_event/{event_id}):**

- Параметр event_id: Уникальный идентификатор события.
- Возвращает детали конкретного события.

**Обновление события (PUT /api/v1/calendar/update_event/{event_id}):**

- Параметр event_id: Уникальный идентификатор события.
- Формат данных: "ГГГГ-ММ-ДД|заголовок|текст".
- Возвращает подтверждение об успешном обновлении.

**Удаление события (DELETE /api/v1/calendar/delete_event/{event_id}):**

- Параметр event_id: Уникальный идентификатор события.
- Возвращает подтверждение об успешном удалении.

# Пример использования

## Установить библиотеки из файла requerements.txt
```
pip install -r requirements.txt
```
## запуск приложения

```
$ flask --app api.py run
```


## cURL тестирование

### добавление новой заметки
```
curl http://127.0.0.1:5000/api/v1/calendar/ -X POST -d "2024-01-21|title|text"
```

### получение всего списка заметок
```
curl http://127.0.0.1:5000/api/v1/calendar/
```

### получение заметки по идентификатору / ID == 1
```
curl http://127.0.0.1:5000/api/v1/calendar/1/
```

### обновление текста заметки по идентификатору / ID == 1 /  новый текст == "new text"
```
curl http://127.0.0.1:5000/api/v1/calendar/1/ -X PUT -d "2024-01-22|title|new text"
```

### удаление заметки по идентификатору / ID == 1
```
curl http://127.0.0.1:5000/api/v1/calendar/1/ -X DELETE
```


## пример исполнения команд с выводом

```
$ curl http://127.0.0.1:5000/api/v1/calendar/ -X POST -d "2024-01-21|title|text"
new id: 1

$ curl http://127.0.0.1:5000/api/v1/calendar/
1|title|text

$ curl http://127.0.0.1:5000/api/v1/calendar/1/
1|title|text

$ curl http://127.0.0.1:5000/api/v1/calendar/1/ -X PUT -d "2024-01-22|title|new text"
updated

$ curl http://127.0.0.1:5000/api/v1/calendar/1/
1|title|new text

$ curl http://127.0.0.1:5000/api/v1/calendar/1/ -X PUT -d "2024-01-21|title|looooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooong text"
failed to UPDATE with: Text length > MAX: 200

$ curl http://127.0.0.1:5000/api/v1/calendar/1/ -X PUT -d "2024-01-21|loooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooong title|text"
failed to UPDATE with: title lenght > MAX: 30

$ curl http://127.0.0.1:5000/api/v1/calendar/1/ -X DELETE
deleted

$ curl http://127.0.0.1:5000/api/v1/calendar/
-- пусто --

$ curl http://127.0.0.1:5000/api/v1/calendar/ -X POST -d "2024-01-21|title|text"
new id: 2

$ curl http://127.0.0.1:5000/api/v1/calendar/ -X POST -d "2024-01-21|title|text"
failed to CREATE with: Another event already exists on the date: b'2024-01-21
```
