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

  reverse_lookup_initialized = 0
  reverse_dict = dict()

  @staticmethod
  def initialize_reverse_lookup():
    for n,i in enumerate(Colors.color_list):
      if i[1] in Colors.reverse_dict:
        print "color symbol %s-%s alrady present with value %s"%(i[1],i[0],Colors.reverse_dict[i[1]])
        sys.exit(1)
      Colors.reverse_dict[i[1]] = (i[0],n)
    Colors.reverse_lookup_initialized = 1

  @staticmethod
  def validate(color):
    if not Colors.reverse_lookup_initialized:
      Colors.initialize_reverse_lookup()
    if not color in Colors.reverse_dict:
      return -1
    return Colors.reverse_dict[color][1]

def make_a_guess(guess_size):
  guess=[]
  for i in range(guess_size):
    guess.append(random.randint(0,guess_size-1))
  return guess

def guess_to_str(guess):
  result=""
  for i in guess:
    result += Colors.color_list[i][1] + " "
  return result

def validated_guess(raw_str):
  raw_str = raw_str.strip()
  colors = raw_str.split()
  guess = []
  for i in colors:
    result = Colors.validate(i)
    if result == -1:
      print "color %s is not valid"%i
      return (0,[])
    guess.append(result)
  return (1,guess)

def get_a_input_guess():
  got = 0
  attempts = 1
  while not got:
    guess = raw_input("Enter a guess, separated by white spaces:")
    ok,result = validated_guess(guess)
    if ok:
      got = 1
    attempts += 1
    if attempts > 3:
      print ("Too many attempts")
      sys.exit(1)
  return result

def main():
  g = make_a_guess(6)
  print guess_to_str(g)
  g = get_a_input_guess()
  print "You gave: "+guess_to_str(g)

if __name__ == '__main__':
  main()

