# Number Classification API

An API that takes a number and returns interesting mathematical properties about it, along with a fun fact.

## Features

- Determines if a number is prime
- Determines if a number is perfect
- Identifies Armstrong numbers
- Calculates digit sum
- Provides fun mathematical facts
- Returns odd/even property

## API Endpoint

GET `/api/classify-number?number=371`

Replace the number if you like

### Success Response (200 OK)

```json
{
    "number": 371,
    "is_prime": false,
    "is_perfect": false,
    "properties": ["armstrong", "odd"],
    "digit_sum": 11,
    "fun_fact": "371 is an Armstrong number..."
}
```

### Error Response (400 Bad Request)

```json
{
    "number": "alphabets",
    "error": true
}
```

## Setup and Installation

1. Clone the repository
2. Install requirements: `pip install -r requirements.txt`
3. Run migrations: `python manage.py migrate`
4. Start server: `python manage.py runserver`

## Testing

Run tests with: `python manage.py test`

## Deployment

The API is deployed at: []

## Technologies Used

- Python
- Django
- Django REST Framework
- Numbers API for fun facts