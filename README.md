# QR Code API

A simple and fast QR Code Generator API built with Django REST Framework.

## Features

- Generate QR codes from any text or URL
- Returns PNG image
- Fast and lightweight
- Easy to integrate with websites and Telegram bots

## Installation

```bash
git clone https://github.com/abdumalik-najmiddinov/qr-code-api.git
cd qr-code-api
pip install -r requirements.txt
```

## Run

```bash
python manage.py runserver
```

## Endpoint

```http
GET /qr/?text=Hello
```

## Example Request

```http
http://127.0.0.1:8000/qr/?text=https://github.com
```

## Response

Returns a PNG QR code image.

## Tech Stack

- Python
- Django
- Django REST Framework
- qrcode
- Pillow

## Author

Abdumalik Najmiddinov

## License

MIT License
