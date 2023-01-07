import re

import regex


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




def sign_check(s:str):
   return regex.findall("\\+|-",s)


def test_sign(s:str):
  if "".join(s) == '-':
    print('subtraction')
  elif "".join(s) == '+':
    print('sum')

# res = split_list(random_l)
# for ele in res:
#   do_math(ele)
#


# foo = regex.split(r"( \+ \d*| \- \d*)",random_l[0])
# for ele in foo:
#   print("{0:{align}16}".format(ele, align='>'))

# =================== 11.11.2022 happy independence day Poland!
empty_ls = []
for ele in random_l:
  empty_ls.append(regex.split(r" ", ele))

# for i in range(3):
#   for key, value in enumerate(empty_ls):
#       print("{0:{align}4}".format(empty_ls[key][i],fill='x',align='>'), end= " ")
#   print("\n")

def do_math(element):
  a, b = int(element[0]), int(element[2])
  if element[1] == '+':
    empty_l.append(a + b)
  elif element[1] == '-':
    empty_l.append(a - b)
  return empty_l


[do_math(x) for x in empty_ls]

for i in range(len(empty_l)):
    empty_ls[i].append("    ----")
    empty_ls[i].append(empty_l[i])

TODO: "print in one line"
for i in range(5):
  for key, value in enumerate(empty_ls):
      print("{0:{align}8}".format(empty_ls[key][i],align='>'), end= " ")
  print("\n".lstrip())



foo = sign_check(random_l[0])
bar = sign_check(random_l[1])

# test_sign(foo)
# test_sign(bar)
