import json
import requests

from flask import Flask, request

app = Flask(__name__)


response = requests.get("http://www.floatrates.com/daily/mdl.json")
conversion_rates = json.loads(response.text)


@app.route('/conversions/list', methods=['GET'])
def get_all_conversions():
    return json.dumps(conversion_rates)


@app.route('/conversions/get/<string:from_currency>/<string:to_currency>', methods=['GET'])
def get_conversion(from_currency, to_currency):
    from_currency = from_currency.upper()
    to_currency = to_currency.upper()
    if from_currency in conversion_rates and to_currency in conversion_rates:
        conversion_rate = conversion_rates[to_currency]["rate"] / conversion_rates[from_currency]["rate"]
        return json.dumps({'conversion_rate': conversion_rate})
    else:
        return "Error: Invalid currency codes."


@app.route('/convert', methods=['POST'])
def convert():
    data = request.get_json()
    from_currency = data["from"].upper()
    to_currency = data["to"].upper()
    amount = data["amount"]
    if from_currency in conversion_rates and to_currency in conversion_rates:
        conversion_rate = conversion_rates[to_currency]["rate"] / conversion_rates[from_currency]["rate"]
        converted_amount = amount * conversion_rate
        # Save the conversion to history
        with open("history.json", "a") as file:
            file.write(json.dumps({
                "from": from_currency,
                "to": to_currency,
                "amount": amount,
                "converted_amount": converted_amount
            }) + "\n")
        return json.dumps({'converted_amount': converted_amount})
    else:
        return "Error: Invalid currency codes."


if __name__ == '__main__':
    app.run(debug=True)
