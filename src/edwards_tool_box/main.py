from edwards_tool_box.finance.rate import get_latest_rate
import math
from uniplot import plot


if __name__ == '__main__':
    # one_dollar_to_cny = get_latest_rate()
    # print(f"1 USD = {one_dollar_to_cny:.3f} CNY")
    x = [math.sin(i / 20) + i / 300 for i in range(600)]
    plot(x, title="SPOT Stock History 30 Days")
