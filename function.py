
"""
   `syntax:
   def function_name( parameters ):
        function_suite
        return [expression]
"""

#   examples


def sum_two_elements(i, j):
    k = i + j
    return k


def print_me(string_to_print):
    print string_to_print
    return


"""
    Note that 
    1. there are no function prototypes
    2. the parameters do not carry a type identifier along with them
    3. the return statement in e.g 2 returns nothing and is redundant
       thus we can omit that line
    4. the function must be defined in the code before its use
"""

x = 20
y = 30
z = sum_two_elements(x, y)
print_me('the sum is')
print x, '+', y, '=', z
