from exchangeratesapi import Api
from termcolor import colored

ExchangeRateAPI = Api()


def get_latest_rate():
    res = ExchangeRateAPI.get_rates('USD')
    return res["rates"]["CNY"]


def display_rate():
    _latest = get_latest_rate()
    latest = colored(f"¥{_latest:.3f}", "magenta")
    print(f"$1 = {latest}")
