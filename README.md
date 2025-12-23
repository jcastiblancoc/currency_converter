# Currency Converter

**Simple Python CLI Tool for Real-Time Currency Exchange Conversions**

A lightweight Python utility that demonstrates clean code practices and architecture patterns for building reusable CLI applications. Converts amounts between different currencies using live exchange rates from an external API.

## 🌟 Overview

- **Type**: Command-line application (CLI)
- **Language**: Python 3.8+
- **Purpose**: Real-time currency exchange conversions
- **Focus**: Clean code, modularity, error handling, and API integration
- **Use Case**: Demonstrate Python best practices and API consumption

## ✨ Features

- 💰 **Multi-Currency Support**: Convert between major currencies
- 🔄 **Live Exchange Rates**: Fetches real-time rates from external API
- 🌎 **Simple Interface**: Straightforward console-based interaction
- 😷 **Error Handling**: Graceful handling of API failures and invalid input
- 🧪 **Well-Tested**: Comprehensive unit tests
- 🌐 **Extensible**: Easy to add new currencies or data sources

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- pip
- Internet access (for live exchange rates)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/jcastiblancoc/currency_converter.git
   cd currency_converter
   ```

2. **Create virtual environment** (recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

### Usage

Run the application:

```bash
python main.py
```

Example interaction:
```
Enter amount: 100
Enter source currency (e.g., USD): USD
Enter target currency (e.g., EUR): EUR
100.00 USD = 92.50 EUR (Exchange rate: 0.9250)
```

## 🗍️ Code Example

```python
from currency_converter import CurrencyConverter

converter = CurrencyConverter()
amount = 100
result = converter.convert(amount, 'USD', 'EUR')
print(f"{amount} USD = {result} EUR")
```

## 🧪 Testing

Run the test suite:

```bash
pytest
```

With coverage report:

```bash
pytest --cov=src --cov-report=html
```

## 🛠️ Tech Stack

- **Language**: Python 3.8+
- **HTTP Client**: requests library
- **Testing**: pytest
- **Code Quality**: Black, Flake8
- **API Source**: Open Exchange Rates API (or similar)

## 📁 Project Structure

```
.
├── src/
│   ├── converter.py       # Main converter logic
│   ├── api_client.py      # API integration
│   └── utils.py          # Utility functions
├── tests/
│   ├── test_converter.py
│   └── test_api_client.py
├── main.py            # Entry point
├── requirements.txt
└── README.md
```

## 📚 Learning Outcomes

This project demonstrates:

- Clean code principles and modular design
- External API consumption and error handling
- Unit testing and TDD practices
- Python packaging and dependency management
- CLI application structure

## 🛠 Troubleshooting

**API Rate Limit Exceeded**
- Wait a few minutes before retrying
- Consider implementing request caching

**Currency Not Supported**
- Check the API documentation for supported currencies
- Verify the currency code (e.g., USD, EUR, GBP)

## 📄 License

MIT License - See LICENSE file for details

---

**Purpose**: Learning project showcasing Python best practices
