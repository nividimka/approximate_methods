import math
import numpy as np


class Result(object):

    def __init__(self, v, r):
        self.acc = v
        self.rest = r


class simple_parser(object): variables = dict()

def set_variable(self, variable_name, variable_value): self.variables[variable_name] = variable_value


def get_variable(self, variable_name):
    if variable_name not in self.variables:
        print("Error: Try get incorrect variable '" + variable_name + "'")
        return 0
    else:
        return self.variables[variable_name]


    def parse(self, s):
        s = s.replace(" ", "")
        s = s.replace(",", ".")
        s = s.replace("\n", "")
        result = self.plus_minus(s)
        if len(result.rest) != 0:
            print("Error: can't full parse")
            print("rest: " + result.rest)
        else:
            return result.acc


    def plus_minus(self, s):
        current = self.mult_div(s)
        acc = current.acc
        while len(current.rest) > 0:
            if current.rest[0] != '+' and current.rest[0] != '-':
                break
            sign = current.rest[0]
            next = current.rest[1:]
            current = self.mult_div(next)
            if sign == '+':
                acc += current.acc
            else:
                acc -= current.acc
        return Result(acc, current.rest)


    def bracket(self, s):
        if len(s) != 0 and s[0] == "(":
            r = self.plus_minus(s[1:])
            if len(r.rest) != 0 and r.rest[0] == ")":
                r.rest = r.rest[1:]
            else:
                print("Error: not close bracket")
            return r
        return self.function_variable(s)


    def function_variable(self, s):
        f = ""
        i = 0
        while i < len(s) and (s[i].isalpha() or (s[i].isdigit() and i > 0)):
            f += s[i]
            i += 1
        if len(f) != 0:
            if len(s) > i and s[i] == '(':
                r = self.bracket(s[len(f):])
                return simple_parser.process_function(f, r)
            else:
                return Result(self.get_variable(f), s[len(f):])
        return self.num(s)


    def mult_div(self, s):
        current = self.bracket(s)
        acc = current.acc
        while True:
            if len(current.rest) == 0:
                return current
            sign = current.rest[0]
            if sign != '*' and sign != "/":
                return current
            next = current.rest[1:]
            right = self.bracket(next)
            if sign == '*':
                acc *= right.acc
            elif sign == '/':
                acc /= right.acc
            current = Result(acc, right.rest)

    @staticmethod
    def num(s):
        i = 0
        dot_cnt = 0
        negative = False
        if len(s) != 0 and s[0] == '-':
            negative = True
            s = s[1:]
        while i < len(s) and (s[i].isdigit() or s[i] == '.' or s[i] == ','):
            if s[i] == '.':
                dot_cnt += 1
            if (s[i] == '.') and dot_cnt > 1:
                raise Exception("not valid number '" + s.substring(0, i + 1) + "'")
            i += 1
        if i == 0:
            raise Exception("can't get valid number in '" + s + "'")
        f_part = float(s[:i])
        if negative:
            f_part = -f_part
        rest_part = s[i:]
        return Result(f_part, rest_part)

    @staticmethod
    def process_function(func, r):
        if func == "sin":
            return Result(np.sin(math.radians(r.acc)), r.rest)
        elif func == "cos":
            return Result(np.cos(math.radians(r.acc)), r.rest)
        elif func == "tan":
            return Result(np.tan(math.radians(r.acc)), r.rest)
        elif func == "exp":
            return Result(np.exp(r.acc), r.rest)
        else:
            print("function '" + func + "' is not defined")
        return r
