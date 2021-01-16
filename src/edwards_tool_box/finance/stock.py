import warnings
from datetime import datetime
from datetime import timedelta

import uniplot
import yfinance as yf
from termcolor import colored

from edwards_tool_box.constants import GLOBAL_CONFIG

warnings.simplefilter("ignore")

START_DATE = datetime.strptime("2019-11-01", "%Y-%m-%d")
EXERCISE_AMOUNT = GLOBAL_CONFIG["finance"]["stock"]["amounts_to_exercise"]


def fetch_latest_SPOT_history():
    return yf.Ticker("SPOT").history(period="max")


def get_spotify_latest_stock_price():
    SPOT = fetch_latest_SPOT_history()
    LATEST_DATE = SPOT.index.max()
    latest = SPOT.loc[LATEST_DATE]
    return latest["High"], latest["Low"], latest["Close"]


def get_exercise_profit(amount):
    SPOT = fetch_latest_SPOT_history()
    latest_h, latest_low, latest_close = get_spotify_latest_stock_price()
    granted_price = SPOT.loc[START_DATE]["Close"]
    return amount * (latest_close - granted_price) * 0.57


def plot_spot_back_30_days():
    SPOT = fetch_latest_SPOT_history()
    LATEST_DATE = SPOT.index.max()
    SPOT_BACK_30_DAYS = SPOT.loc[LATEST_DATE - timedelta(days=30):]
    uniplot.plot(SPOT_BACK_30_DAYS["Close"], title="SPOT Stock History 30 Days")


def display_spot():
    plot_spot_back_30_days()
    _high, _low, _close = get_spotify_latest_stock_price()
    high = colored(f"{_high:.3f}", "green")
    low = colored(f"{_low:.3f}", "red")
    close = f"{_close:.3f}"
    print(f"H:{high}\nL:{low}\nC:{close}")
    profit = colored(f"${get_exercise_profit(EXERCISE_AMOUNT):.0f}", "cyan")
    print(
        f"{profit} estimated profit will be gained by exercising {EXERCISE_AMOUNT} of stock options.")


if __name__ == '__main__':
    display_spot()
