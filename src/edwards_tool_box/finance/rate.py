from exchangeratesapi import Api

ExchangeRateAPI = Api()


def get_latest_rate():
    res = ExchangeRateAPI.get_rates('USD')
    return res["rates"]["CNY"]
