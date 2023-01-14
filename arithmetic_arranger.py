from typing import List
import regex


def arithmetic_arranger(problems):
    arranged_problems= problems
    return arranged_problems


def get_input(input:List[str]):
  return input

def get_empty_list():
  return [], []

random_l = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]

empty_l, empty_ls =[], []

def split_input(input):
  return [regex.split(r" ", ele) for ele in input]

for ele in random_l:
  empty_ls.append(regex.split(r" ", ele))

def do_math2(element):
  foo = []
  a, b = int(element[0]), int(element[2])
  if element[1] == '+':
    foo.append(a + b)
  elif element[1] == '-':
    foo.append(a - b)
  return foo


def merge_operators_results(math_list: list, split_list: list):
    for k, v in enumerate(math_list):
        split_list[k].append(math_list[k][0])
    return split_list


def do_math(element):
  a, b = int(element[0]), int(element[2])
  if element[1] == '+':
    empty_l.append(a + b)
  elif element[1] == '-':
    empty_l.append(a - b)
  return empty_l

def apply_math(split_input:List[str]):
  return [do_math2(x) for x in split_input]


[do_math(x) for x in empty_ls]

for i in range(len(empty_l)):
    empty_ls[i].append("    ----")
    empty_ls[i].append(empty_l[i])

TODO: "print in one line"
for i in range(5):
  for key, value in enumerate(empty_ls):
      print("{0:{align}8}".format(empty_ls[key][i],align='>'), end= " ")
  print("\n".lstrip())


input = get_input(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])
split = split_input(input)
math = apply_math(split)
calculation = merge_operators_results(math, split)
#TODO: join two lists: split, math, into one
#redundant line to be removed in foreseeable future
