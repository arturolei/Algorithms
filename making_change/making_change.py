#!/usr/bin/python

import sys

def making_change(amount, denominations): 
  cache = [1 for i in range(amount + 1)]                          
  if amount < 0: #Negative money
    return 0                                        
  elif amount < 5: #if it's less than 5 cents, there's only way to do it!
    return 1                                        
  else:
    for coin in denominations[1:]: # cycle through denominations   

      for higher_amount in range(coin, amount + 1): 
        difference = higher_amount - coin           
        cache[higher_amount] += cache[difference]   

    return cache[amount]                        


if __name__ == "__main__":
  # Test our your implementation from the command line
  # with `python making_change.py [amount]` with different amounts
  if len(sys.argv) > 1:
    denominations = [1, 5, 10, 25, 50]
    amount = int(sys.argv[1])
    print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
  else:
    print("Usage: making_change.py [amount]")