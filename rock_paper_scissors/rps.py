#!/usr/bin/python

import sys
#Itertools has the product() which is basically the cross-product 
import itertools

#Here are the possible outcomes
rps_outcomes = ["rock", "paper", "scissors"]

def rock_paper_scissors(n):
  #this is a list of tuples
  result = list(itertools.product(rps_outcomes, repeat=n))
  # print(result)
  # we need to turn each list of tuples into real lists
  return [list(outcome) for outcome in result]


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')