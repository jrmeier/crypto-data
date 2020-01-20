# Crypto Data
This is for storing minute by minute trading data, in a way that's accurate but cheap.

Pull requests are welcome! If you make any improvements, please share!

# Goals
- No database
- Fast 
- Accurate

# Features
- raw data for a ticker for every minute
- build trading data files with the available indicators built-in (consumption comes from different projects)

# Install

`git clone git@github.com:jrmeier/crypto-data.git
cd ./crypto-data
python -m venv .crypto-data
pip install -r requirements.txt
`
The next thing you'll want to do is set up your cron jobs to run on every minute for `minute_cron.py` and daily for `daily_cron.py`. In these files, you'll need to set the location to save your daily csvs and the zipped files in their respective files.

# Usage
This pulls data from a the binance api, but it could easily be adapted for any others. It's set up to only save the most important data that's consumed by [fast_trade](https://github.com/jrmeier/fast_trade), which does the backtesting. These files are set up to save the date, close, open, high, low, volume.

Example file:

`
date,close,open,high,low,volume
1579392120515,0.00242400,0.00252600,0.00254600,0.00241200,4900945.00000000
1579392181801,0.00242600,0.00252600,0.00254600,0.00241200,4903422.00000000
1579392241780,0.00242900,0.00252600,0.00254600,0.00241200,4906109.00000000
1579392287466,0.00242900,0.00252600,0.00254600,0.00241200,4906109.00000000
1579392360006,0.00242900,0.00252600,0.00254600,0.00241200,4905470.00000000
1579392402581,0.00242900,0.00252600,0.00254600,0.00241200,4905470.00000000
1579392464108,0.00242900,0.00252400,0.00254600,0.00241200,4904420.00000000
1579392525682,0.00242900,0.00252000,0.00254600,0.00241200,4903820.00000000
`
