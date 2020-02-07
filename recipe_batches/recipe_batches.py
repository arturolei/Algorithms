#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  # The amount of each ingredient determines the number of batches possible
  #let's keep track per ingredient; minimum number = 
  num_batch_possible = []
  for key in recipe.keys():
    if key in ingredients.keys(): #make sure we have ingredient
      batches_possible = ingredients[key] // recipe[key]
    else:
      return 0 #If the recipe has an ingredient that's not in our pantry, we can't make any
    num_batch_possible.append(batches_possible)

  return min(num_batch_possible)


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))