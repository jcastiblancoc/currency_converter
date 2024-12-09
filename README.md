# Currency Converter

This is a simple Python application for converting currencies using live exchange rates fetched from an external API. The application runs in the console and provides a straightforward way to convert amounts between different currencies.

## Features

- Converts amounts between various currencies.
- Fetches real-time exchange rates via an external API.
- Simple console-based interface.

## Prerequisites

- Python 3.8+ installed.
- Internet access to retrieve live exchange rates.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/jcastiblancoc/currency_converter.git
   cd currency_converter
Set up a virtual environment (optional, but recommended):

python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
Install dependencies:

pip install -r requirements.txt
Usage
Run the application:

python currency_converter.py
The application will prompt you to enter:

The currency you want to convert from (e.g., USD).
The currency you want to convert to (e.g., EUR).
The amount you want to convert.
The converted amount will be displayed based on the latest exchange rates.

Example Interaction

Enter base currency (e.g., USD): USD
Enter target currency (e.g., EUR): EUR
Enter amount: 100
Converted amount: 94.32 EUR

#Project Structure

currency_converter/
├──app                       # Main script for currency conversion logic
├── currency_converter.py    # Helpers file
├── requirements.txt         # Required Python packages
├── README.md                # Project documentation
API Integration
The application fetches exchange rates using an external API. The API endpoint is set in the currency_converter.py file. You can update the URL if needed:

python

API_URL = "https://api.exchangerate-api.com/v4/latest/"
If you'd like to use a different API, replace the endpoint accordingly in the code.

Development
You can contribute to the development by following these steps:

Fork the repository.
Create a new branch:
bash

git checkout -b feature/your-feature-name
Make your changes, commit them, and push:
bash

git push origin feature/your-feature-name
Open a pull request.
License
This project is licensed under the MIT License. See the LICENSE file for details.

Resources
Python Documentation
ExchangeRate-API

This version of the `README.md` assumes a simple Python app for currency conversion
