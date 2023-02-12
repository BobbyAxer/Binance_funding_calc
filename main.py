import requests
import json
import openpyxl
import pandas as pd
from dotenv import load_dotenv
load_dotenv()
import os
import time
import asyncio
import aiohttp
api_key_binance = os.environ.get('API_B')
api_secret_binance = os.environ.get('SECRET_B')

async def get_binance_futures_tickers():
    url = 'https://fapi.binance.com/fapi/v1/ticker/24hr'
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.json()
    futures_tickers = [ticker['symbol'] for ticker in data if 'USDT' in ticker['symbol']]
    return futures_tickers

async def get_data(symbol, period, limit):
    endpoint = 'https://fapi.binance.com/fapi/v1/fundingRate'
    headers = {
        'X-MBX-APIKEY': api_key_binance
    }
    params = {
        'symbol': symbol,
        'period': period,
        'limit': limit
    }
    async with aiohttp.ClientSession() as session:
        async with session.get(endpoint, headers=headers, params=params) as response:
            data = await response.json()
    return data

async def main():
    start = time.time()
    tickers = await get_binance_futures_tickers()
    print(tickers)
    data = []

    tasks = []
    for symbol in tickers:
        task = asyncio.ensure_future(get_data(symbol, '1h', 300))
        tasks.append(task)

    responses = await asyncio.gather(*tasks)
    for symbol_data in responses:
        print(symbol_data)
        for row in symbol_data:
            # row["symbol"] = symbol
            data.append(row)


    df = pd.DataFrame(data)
    # print(df)
    df["fundingTime"] = pd.to_datetime(df["fundingTime"], unit='ms')
    df = df.set_index("fundingTime")
    df["fundingRate"] = df["fundingRate"].astype(float)
    print(df)
    avg_funding_rates = round(df.groupby("symbol")["fundingRate"].mean() * 365 * 3 * 100, 2)
    thirteen_days = round(df.groupby("symbol").apply(lambda x: x.tail(90)["fundingRate"].mean() * 365 * 3 * 100), 2)
    # Get the last funding rate for each symbol
    last_funding_rates = round(df.groupby("symbol")["fundingRate"].last() * 365 * 3 * 100, 2)
    seven_days = round(df.groupby("symbol").apply(lambda x: x.tail(22)["fundingRate"].mean() * 365 * 3 * 100), 2)
    # print(seven_days)
    three_days = round(df.groupby("symbol").apply(lambda x: x.tail(10)["fundingRate"].mean() * 365 * 3 * 100), 2)
    # Concatenate the two results into a single dataframe
    one_day = round(df.groupby("symbol").apply(lambda x: x.tail(3)["fundingRate"].mean() * 365 * 3 * 100), 2)
    result = pd.concat([avg_funding_rates, thirteen_days, seven_days, three_days, one_day, last_funding_rates], axis=1)
    result.columns = ["90 days", '30 days', '7 days', '3 days', '1day', "last_funding_rate"]
    result.to_excel('funding.xlsx', sheet_name='Funding_management')
    # Print the result
    print(result)
    # Print the top 5 symbols with the highest average funding rate
    print("Top 15 symbols with highest 7 days funding rate:")
    print(result.nlargest(15, "7 days"))
    print("Top 15 symbols with lowest 7 days funding rate:")
    print(result.nsmallest(15, "7 days"))
    print("Top 15 symbols with highest last funding rate:")
    print(result.nlargest(15, "last_funding_rate"))
    print("Top 15 symbols with lowest last funding rate:")
    print(result.nsmallest(15, "last_funding_rate"))
    print(f' done in {time.time() - start} seconds')

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()

