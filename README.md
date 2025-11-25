# My-Zootopia

A web application that generates animal information cards by fetching data from an external API.

## Description

My-Zootopia is a Python-based web generator that creates HTML pages displaying detailed information about animals. It fetches real-time data from the API Ninjas animals API and formats it into beautiful, responsive HTML cards.

## Features

- **Dynamic Animal Data**: Fetches animal information from API Ninjas
- **Responsive HTML Cards**: Displays animal data in a clean, card-based layout
- **Error Handling**: Shows user-friendly messages when animals are not found
- **Environment Configuration**: Secure API key management using environment variables

## Project Structure

```
My-Zootopia/
├── animals_web_generator.py    # Main application logic
├── data_fetcher.py             # API integration module
├── animals.html               # Generated HTML output
├── animals_template.html      # HTML template for rendering
├── animals_data.json          # Local animal data cache
├── requirements.txt           # Python dependencies
├── .env                       # Environment variables (API key)
├── .gitignore                 # Git ignore file
└── README.md                  # This file
```

## Installation

1. Clone or download this repository
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Setup

1. **Get API Key**: Sign up at [API Ninjas](https://api-ninjas.com/) to get your free API key for the animals endpoint.

2. **Configure Environment**: Create a `.env` file in the project root with your API key:
   ```
   API_KEY="your_api_key_here"
   ```

## Usage

The main functionality is in `animals_web_generator.py`. The application:

1. Fetches animal data based on user input using the `load_data_from_api()` function
2. Serializes the data into HTML format using `serialize_animal()`
3. Generates a complete HTML page with animal information cards
To use this project, run the following command - `python animals_web_generator.py`

### Key Functions

- `return_data_based_on_user_input(user_input)`: Main function that processes user requests
- `serialize_animal(animal)`: Converts animal data to HTML card format
- `load_data_from_api(user_input)`: Fetches data from the API (in `data_fetcher.py`)

## Dependencies

- **requests**: For making HTTP requests to the API
- **python-dotenv**: For loading environment variables from `.env` file

## API Integration

The application uses the API Ninjas Animals API:
- Endpoint: `https://api.api-ninjas.com/v1/animals`
- Authentication: API key via `X-Api-Key` header
- Returns: JSON data with animal characteristics including diet, location, type, slogan, color, and skin type

## Error Handling

- If an animal is not found, displays a user-friendly message
- Gracefully handles missing data fields in API responses
- Environment variables are loaded securely with fallback handling

## Contributing

Feel free to contribute improvements, bug fixes, or new features to this project.

## License

This project is open source and available under the MIT License.
