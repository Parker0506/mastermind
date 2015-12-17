#!/usr/bin/python

import random

class Colors:
  color_list = [
    ("red",    'R'),  # 0
    ("purple", 'P'),  # 1
    ("yellow", 'Y'),  # 2
    ("green",  'G'),  # 3
    ("white",  'W'),  # 4
    ("brown",  'B'),  # 5
    ("Last-Non-color-Count", "?") ]

def make_a_guess(guess_size):
  guess=[]
  for i in range(guess_size):
    guess.append(random.randint(0,guess_size-1))
  return guess

def main():
  print Colors.color_list
  g = make_a_guess(6)
  print g

if __name__ == '__main__':
  main()

