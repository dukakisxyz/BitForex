# BitForex
BitFOREX – Providing current and historical foreign exchange rates as published by the European Central Bank, in exchange for bitcoin.
The rates are updated daily around 4PM CET

To fetch the latest Forex Rates run:

21 buy http://[::]:9000/latest

Rates are quoted against the Euro by default. Quote against a different currency by setting the base parameter in your request.
For example:

21 buy http://[::]:9000/latest/USD

You can fetch historical data as shown below:

21 buy http://[::]:9000/get/2016-10-13

Note: The date must be in the specified format: YYYY-MM-DD, single digit days or months will return an error.

You can quote against a different currency while fetching historical data by setting the base parameter in your request as specified below:

21 buy http://[::]:9000/get/2016-10-13/usd

Happy BitForexing
