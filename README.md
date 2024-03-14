# Discord Status Unresolved/ongoing issue scrapper.

This Flask application scrapes incident titles, descriptions, and timestamps from the Discord Status website and serves them in JSON format via an API endpoint.

## Prerequisites

Before running the application, ensure you have the following installed:

- Python 3.x
- Flask
- Requests
- BeautifulSoup4

You can install the dependencies using pip:

```bash
pip install flask requests beautifulsoup4
```

## Usage

1. Clone this repository:

```bash
git clone https://github.com/PRATIKK0709/Discord_Status
```

2. Navigate to the project directory:

```bash
cd Discord_Status
```

3. Run the Flask application:

```bash
python app.py
```

The application will start running on `http://127.0.0.1:5000/`.

## API Endpoint

### GET /incidents

This endpoint returns a JSON object containing incident titles, descriptions, and timestamps scraped from the Discord Status website.

Example response:

```json
[
  {
    "description": "We are seeing recovery and will continue monitoring the system",
    "timestamp": "Mar 14, 2024 - 12:18 PDT",
    "title": "Media unable to load"
  }
]
```


