# Homework

Having the conversion rates avaialble on this website: `http://www.floatrates.com/daily/mdl.json`

Use your code from one of your homeworks with the currency conversion programs, and make a flask application that will
do the following.

1. have a route /conversions/list - GET only, that will return all conversions
2. have a route /conversions/get/<currency> - GET only, that will return conversion rates for that conversion
3. have a route /convert - POST only, that will take the following JSON format as request data
    ```json
     {"from": "MDL","to": "eur", "amount": 1000}
     ```
   And will return the converted value

Bonus points:

1. Try to save all the requested conversions in a separate files (call it history.json)
