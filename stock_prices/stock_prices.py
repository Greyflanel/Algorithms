#!/usr/bin/python

import argparse

def find_max_profit(prices):
  maximum_profit = False
  while maximum_profit == False and len(prices) >= 1:
    max_price = max(prices)
    min_price = min(prices)
    min_index = prices.index(min_price)
    max_index = prices.index(max_price)
    max_profit = 0
    if max_index > min_index:
      max_profit = max_price - min_price
      maximum_profit = True
      return max_profit
    if max_index < min_index and max_index != 0:
      min_price = min(prices[:max_index])
      max_price = prices[max_index]
      max_profit = max_price - min_price
      maximum_profit = True
      return max_profit
    if max_index < min_index and max_index == 0:
      max_index = prices.index(max(prices[max_index + 1:len(prices)]))
      max_price = prices[max_index]
      min_price = min(prices[:max_index])
      max_profit = max_price - min_price
      maximum_profit = True
      return max_profit
    elif max_index < min_index:
      max_index = prices.index(max(prices[max_index + 1:len(prices)]))
      max_price = prices[max_index]
      max_profit = max_price - min_price
      maximum_profit = True
      return max_profit
  


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))