#!/usr/bin/python

from __future__ import print_function

import random
import sys
import readline


class Colors:
  color_list = [
    ("red",    'R'),  # 0
    ("purple", 'P'),  # 1
    ("yellow", 'Y'),  # 2
    ("green",  'G'),  # 3
    ("white",  'W'),  # 4
    ("brown",  'B'),  # 5
    ("magenta",'M'),  # 6
    ("cyan",   'C'),  # 7
    ("violet", 'V'),  # 8
    ("indigo", 'I'),  # 9
    ("Last-Non-color-Count", "?") ]

  @staticmethod
  def max_color():
    return len(Colors.color_list) - 1

  reverse_lookup_initialized = 0
  reverse_dict = dict()

  @staticmethod
  def initialize_reverse_lookup():
    for n,i in enumerate(Colors.color_list):
      if i[1] in Colors.reverse_dict:
        print("color symbol %s-%s alrady present with value %s"%(i[1],i[0],Colors.reverse_dict[i[1]]))
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

def make_a_guess(guess_size, color_size):
  guess=[]
  for i in range(guess_size):
    guess.append(random.randint(0,color_size-1))
  return guess

def guess_to_str(guess):
  result=""
  for i in guess:
    result += Colors.color_list[i][1] + " "
  return result

def validate_guess(raw_str, expected_size):
  raw_str = raw_str.strip()
  colors = raw_str.split()
  guess = []
  count = 0
  for i in colors:
    result = Colors.validate(i)
    if result == -1:
      print("color %s is not valid"%i)
      return (0,[])
    guess.append(result)
    count += 1
  if not count == expected_size:
    print("input was only of len %d, but expected %d"%(count,expected_size))
    return (0,[])
  return (1,guess)

def get_a_input_guess(expected_size):
  got = 0
  attempts = 1
  while not got:
    guess = input("Enter a guess of size %d, separated by white spaces:"%expected_size)
    ok,result = validate_guess(guess, expected_size)
    if ok:
      got = 1
    attempts += 1
    if attempts > 3:
      print("Too many attempts")
      sys.exit(1)
  return result

def compare_guesses(lhs, rhs):
  l = len(lhs)
  if l != len(rhs):
    print("Lengths are not same - %d, %d"%(l,len(rhs)))
    return -1
  # lets find the same ones by comparison
  # and count colors in either side for remaining.
  left_colors=[0]*Colors.max_color()
  right_colors=[0]*Colors.max_color()
  rights = 0
  color_okies = 0
  for (i,j) in zip(lhs,rhs):
    if i == j:
      rights += 1
    else:
      left_colors[i] += 1
      right_colors[j] += 1
  for (i,j) in zip(left_colors,right_colors):
    color_okies += min(i,j)
  return (rights,color_okies)

def play_a_game(current_guess_size, current_color_size):
  if current_color_size > Colors.max_color():
    print("sorry.. we support only %d number of colors. input was %d"%(Colors.max_color(),current_color_size))
    sys.exit(1)
  if current_guess_size >= current_color_size:
    print("guess size(%d) should be lesser than color size(%d)"%(current_guess_size, current_color_size))
    sys.exit(1)
  if current_guess_size < 4:
    print("guess size(%d) should be minimum of 4"%(current_guess_size))
    sys.exit(1)
  print("Allowed colors are: %s"%(guess_to_str(range(0,current_color_size))))
  mine = make_a_guess(current_guess_size, current_color_size)
  guess_file="/tmp/current_guess"
  try:
    f=open(guess_file,"w")
    print("Guess is %s"%guess_to_str(mine), file=f)
    f.close()
  except Exception as e:
    print("Some trouble in printing guess into %s:%s"%(guess_file,str(e)))
  attempts = 0
  while True:
    g = get_a_input_guess(current_guess_size)
    attempts += 1
    (rights, color_okies) = compare_guesses(mine, g)
    if rights == current_guess_size:
      print("You got it!")
      break
    else:
      print("Rights: %d, color matches: %d. Attempts so far: %d\n"%(rights,color_okies,attempts))

def get_color_size(color_size):
  c = int(color_size)
  if c < 6 or c > Colors.max_color():
    print("Choose color size between 6 and %d"%Colors.max_color())
    sys.exit(1)
  return c

if __name__ == '__main__':
  if len(sys.argv) == 1:
    color_size = 6
    guess_size = 4
  elif len(sys.argv) == 2:
    color_size = get_color_size(sys.argv[1])
    guess_size = color_size - 2
  else:
    color_size = get_color_size(sys.argv[1])
    guess_size = int(sys.argv[2])
  play_a_game(guess_size, color_size)
