from typing import List
import regex


def arithmetic_arranger(problems):
    arranged_problems= problems
    return arranged_problems


def get_input(input:List[str]):
  return input

def get_empty_list():
  return [], []


def split_input(input):
  return [regex.split(r" ", ele) for ele in input]


def do_math2(element):
  foo = []
  a, b = int(element[0]), int(element[2])
  if element[1] == '+':
    foo.append(a + b)
  elif element[1] == '-':
    foo.append(a - b)
  return foo


def add_sign(split_list:list):
    for i in range(len(split_list)):
        split_list[i].append("    ----")
    return split_list

def merge_operators_results(math_list: list, split_list: list):
    for k, v in enumerate(math_list):
        split_list[k].append(math_list[k][0])
    return split_list


def apply_math(split_input:List[str]):
  return [do_math2(x) for x in split_input]


def print_results(problems):
    for i in range(5):
        for key, value in enumerate(problems):
            print("{0:{align}8}".format(problems[key][i],align='>'), end= " ")
        print("\n".lstrip())


problems = get_input(["100 + 100", "3801 - 2", "45 + 43", "123 + 49"])
split = split_input(problems)
math = apply_math(split)
dashes = add_sign(split)
calculation = merge_operators_results(math, dashes)
print_results(calculation)
