# FastAPI Wallet Information Service

Этот проект предоставляет API для получения информации о кошельке на блокчейне Tron, включая данные о балансе, энергии и пропускной способности (bandwidth). Все запросы сохраняются в базе данных SQLite для дальнейшего анализа.

- **FastAPI** — для создания API.
- **SQLAlchemy** — для работы с базой данных.
- **Tronpy** — для взаимодействия с блокчейном Tron.
- **Pydantic** — для валидации данных.
- **pytest** — для тестирования.

## 📦 Установка

Для начала работы с проектом, клонируй репозиторий и установи зависимости:

```bash
git clone https://github.com/daniillamonov/test.git
```

```bash
pip install -r requirements.txt
```
В файл .env.example добавьте TRON_API_KEY и переименуйте его в .env

### База данных

Этот проект использует **SQLite** для хранения запросов. База данных будет автоматически создана при запуске сервера.

## Запуск проекта

Чтобы запустить сервер FastAPI:

```bash
uvicorn app.main:app --reload
```

API работает на адресе `http://127.0.0.1:8000`.

## 📑 API Endpoints

### `POST /wallets/add`

Запрос для получения информации о кошельке.

**Тело запроса:**

```json
{
  "address": "TXYZ123..."
}
```

**Ответ:**

```json
{
  "address": "TXYZ123...",
  "bandwidth": 600,
  "energy": 200,
  "balance": 0.5
}
```

### `GET /wallets`

Получить список всех запросов о кошельках из базы данных.

**Параметры запроса:**

- `skip` (по умолчанию: 0) — сколько записей пропустить.
- `limit` (по умолчанию: 10) — максимальное количество записей на странице.

**Ответ:**

```json
[
  {
    "address": "TXYZ123...",
    "bandwidth": 100,
    "energy": 200,
    "balance": 0.5,
    "timestamp": "2025-04-08T12:34:56.789012"
  },
  ...
]
```