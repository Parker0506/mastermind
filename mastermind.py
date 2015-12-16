#!/usr/bin/python

class Colors:
  color_list = [
    ("red",    'R'),  # 0
    ("purple", 'P'),  # 1
    ("yellow", 'Y'),  # 2
    ("green",  'G'),  # 3
    ("white",  'W'),  # 4
    ("brown",  'B'),  # 5
    ("Last-Non-color-Count", "?") ]

def main():
    print Colors.color_list

if __name__ == '__main__':
    main()

