# Project Documentation
Introduction
This code retrieves the funding rate data from Binance futures API, and calculates the average funding rate for different time periods. The results are stored in an excel file, with a sheet named "Funding_management". The top 15 symbols with the highest and lowest average funding rate for the last 7 days, last funding rate, and 1 day, 3 days, 7 days, 30 days, and 90 days are also displayed.

# Requirements

-Requests
-JSON
-Openpyxl
-Pandas
-dotenv
-asyncio
-aiohttp

# Environment Variables
This code uses the os and dotenv libraries to access environment variables that store the API key and secret. To run the code, create a file named .env in the same directory as the code and set the API key and secret as follows:

API_B=your_api_key
SECRET_B=your_api_secret

# Usage
1.Clone the repository

2. Install the required packages by running pip install -r requirements.txt in your terminal
 
3. Set up the environment variables in the .env file as described above

4. Run the code by executing python main.py

5. The results will be stored in an excel file named funding.xlsx

# Installation Tutorial

1.Clone the repository:
git clone 
2. Navigate to the project directory:
cd binance-futures-funding-rate
3.Create a virtual environment and activate it:
python -m venv env
source env/bin/activate
4.Install the required packages:
pip install -r requirements.txt
5. Create the .env file and set the API key and secret as described above
6. Run the code:
python3 main.py
7.The results will be stored in an excel file named funding.xlsx.

