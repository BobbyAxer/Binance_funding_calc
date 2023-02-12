# Project Documentation
Introduction
This code retrieves the funding rate data from Binance futures API, and calculates the average funding rate for different time periods. The results are stored in an excel file, with a sheet named "Funding_management". The top 15 symbols with the highest and lowest average funding rate for the last 7 days, last funding rate, and 1 day, 3 days, 7 days, 30 days, and 90 days are also displayed.

Requirements
Requests
JSON
Openpyxl
Pandas
dotenv
asyncio
aiohttp
