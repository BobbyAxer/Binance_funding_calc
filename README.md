## Project Documentation
# Introduction
This code retrieves the funding rate data from Binance futures API, and calculates the average funding rate for different time periods for all coins traded on Binance Futures. The results are stored in an excel file, with a sheet named "Funding_management". The top 15 symbols with the highest and lowest average funding rate for the last 7 days and the highest and lowest for the last period printed.

## Requirements
Code worked for me on python 3.8.9
- Requests
- JSON
- Openpyxl
- Pandas
- dotenv
- asyncio
- aiohttp

## Environment Variables

This code uses the os and dotenv libraries to access environment variables that store the API key and secret. To run the code, create a file named .env in the same directory as the code and set the API key and secret as follows:

API_B=your_api_key

SECRET_B=your_api_secret


## Usage

1. Clone the repository

git clone https://github.com/BobbyAxer/Binance_funding_calc.git


2. Navigate to the project directory

cd Binance_funding_calc
 


3. Install the required packages

pip install -r requirements.txt


4. Open the .env file and set the API key and secret as described in the Environment Variables section above

nano .env

ctrl+o(mac version) to save
ctrl+x to exit

5. Run the code

python3 main.py


5. The results will be stored in an excel file named funding.xlsx.

![A screenshot of the print](https://github.com/Samar4eg/Binance_funding_calc/blob/main/print%20example.png)

![A screenshot of funding excel file](https://github.com/Samar4eg/Binance_funding_calc/blob/main/funding%20example.png)

