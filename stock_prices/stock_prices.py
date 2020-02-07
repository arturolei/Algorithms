#!/usr/bin/python

import argparse

def find_max_profit(prices):
    max_profit = None
    # value is each individual price, prices is the array of prices
    for index, value in enumerate(prices):
        # i + 1 is required in case there are only losses all day.  Otherwise it will return 0 instead of the min loss
        for j in range(index + 1, len(prices)):
            buy_sell = prices[j] - value
            # finds the biggest difference between any of the stock prices in the array and assigns it to max_profit
            if max_profit == None or buy_sell > max_profit:
                max_profit = buy_sell
    return max_profit


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))