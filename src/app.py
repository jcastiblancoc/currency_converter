from currency_api import get_currency_list, get_exchange_rates, get_custom_exchange_rates
from datetime import datetime
import json

HISTORICAL = []

def show_menu():
    print("\nCurrency Converter Menu")
    print("1. Show list of currencies")
    print("2. Show exchange rates")
    print("3. Set base and target currencies")
    print("4. Convert currency")
    print("5. View conversion history")
    print("6. Exit")

def main():
    while True:
        show_menu()
        choice = input("Choose an option: ")

        if choice == '1':
            currencies = get_currency_list()
            for code, name in currencies.items():
                print(f"{code}: {name}")
            input("Press Enter to back to the menu")

        if choice == '2':
            print('The base currency is in USD if you need in base other currency type them, else press enter.\n')
            currency = input(('add the currency: '))
            exchanges = get_exchange_rates(currency.upper())

            if exchanges:
                for code, rate in exchanges.items():
                    print(f"{code}: {rate}")
            else:
                print('The base currency is not correct. Please verify your input.')

        elif choice == '3':
            base_currency = input("Enter the base currency code: ").upper()
            target_currency = input("Enter the target currency code, if more than one separate it by coma: ").upper()
            currencies = get_custom_exchange_rates(base_currency, target_currency)

            if currencies:
                for currency, rate in currencies.items():
                    print(f"{currency}: {rate}")
            else:
                print('Please verify your inputs.')

        elif choice == '4':
            amount = float(input('set amount to exchange: '))
            base_currency = input("Enter the base currency code: ").upper()
            target_currency = input("Enter the target currency code: ").upper()
            rates = get_custom_exchange_rates(base_currency, target_currency)

            if target_currency in rates:
                rate = float(rates[target_currency])
                total = amount * rate
                print(f"{amount} {base_currency} is equal to {total} {target_currency}")
                HISTORICAL.append({
                    'Base Currency':base_currency,
                    'Target Currency': target_currency,
                    'Rate': rate,
                    'Total': total,
                    'Date': datetime.now().strftime('%Y-%m-%d')})
            else:
                print("Failed to retrieve exchange rate.")

        elif choice == '5':
            print(json.dumps(HISTORICAL, indent=4))

        elif choice == '6':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()