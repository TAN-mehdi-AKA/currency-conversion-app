from requests import get
from pprint import PrettyPrinter 

base_url = "https://api.freecurrencyapi.com/"
api_key = "enter you api key in here"

printer = PrettyPrinter() 

def get_currencies():
    endpoint = f"v1/currencies?apikey={api_key}"
    url = base_url + endpoint
    data = get(url).json()

    data = data.get('data',{})
  
    data = list(data.items())
    data.sort()


    printer.pprint(data)
    return data

def print_currencies(currencies):
    for name,currency in currencies:
        cname = currency['name']
        code = currency['code']
        symbol = currency.get('symbol','')

        print(f"{code} - {cname} - {symbol} \n")
        




def exchange_rate(currency1,currency2):
    endpoint = f"v1/latest?apikey={api_key}&currencies=&base_currency={currency1}"
    url = base_url + endpoint
    data = get(url).json()

    data = data.get('data',{})

    data = list(data.items())
    data.sort()

    for curr in data:
        if curr[0] == currency2:
            rate = curr[1]
            currency = curr[0]
        else:
            continue
    # the following line is what I used to check if the rate being return is the one I want
    print(f"{currency1}'s rate to convert to {currency2} is => {currency}={rate}")
    return rate



def convert(currency1,currency2,amount):
    rate = exchange_rate(currency1,currency2)
    if rate is None:
        return 

    try:
        amount = float(amount)
    except:
        print("Invalid amount.")

    converted_result = amount * rate

    print(f"{currency1} to {currency2} = {converted_result}")
    return converted_result



def main():
    currencies = get_currencies()

    print("Welcome to the currency converter!")
    print("List : lists the different currencies")
    print("Convert : convert from one currency to another")
    print("Rate : get the exchange rate of two currencies\n  ")

    while True:
        command = input('Enter a cammand (q to exit) :').lower()

        if command == 'q':
            break
        elif command == 'list':
            print_currencies(currencies) 
        elif command == 'convert':
            currency1 = input("Enter a base currency : ").upper()
            amount = float(input(f"Enter an amount in {currency1} : "))
            currency2 = input("Enter a currency to convert to : ").upper()
            convert(currency1,currency2,amount)
        elif command == 'rate':
            currency1 = input("Enter a base currency : ").upper()
            currency2 = input("Enter a currency to convert to : ").upper()
            exchange_rate(currency1,currency2)
        else:
            print("Unrecognized command!")

main()
####testing the functions 
#currencies = get_currencies()
#print_currencies(currencies)
#exchange_rate("EUR","USD")




 





