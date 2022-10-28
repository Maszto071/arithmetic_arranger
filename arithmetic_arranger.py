import re


def arithmetic_arranger(problems):
  arranged_problems= problems

  return arranged_problems

def split_list(problems):
  return [problem.split() for problem in problems]

def print_in_order(numbers):
  tmp_list = split_list(numbers)
  # tmp_list = [ele.append("----") for ele in tmp_list]
  for i in range(3):
    for x in tmp_list:
      # try:
      print(x[i], end="    ")
      # except IndexError:
      #   if i == 3:
      #     print(int(x[0]) + int(str(x[1]+x[2])), end="    ")
    print()


# def do_math():
#   pass

def print_results():
  pass

random_l = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]
empty_l =[]


def do_math(element):
  a, b = int(element[0]), int(element[2])
  if element[1] == '+':
    empty_l.append(a + b)
  elif element[1] == '-':
    empty_l.append(a - b)
  return empty_l


res = split_list(random_l)
for ele in res:
  do_math(ele)
