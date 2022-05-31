# Generate Parentheses - Given an integer n, generate all valid combinations of n pairs of parentheses
# Brother what lmao
# if n = 3, => ["((()))", "(()())", "(())()", "()(())", "()()()"]
# if n = 2, => ["(())", "()()"]
# if n = 1, => ["()"]
# Mathematical formula is something like 2^(n-1)
# if n = 4, => *theoretically 8* ["(((())))", "(()()())", "((()()))", "(((())))", "()()()()", "()((()))", "(()(()))",
#                                 "()()(())"]
# I think this is right :/

# Video Clarification - A combination that contains 1 type of parentheses is valid if every opening parenthesis, and
# it doesn't have a closing parenthesis without having an unused opening parenthesis before it.

# Initial thoughts: I have no idea....
# Post Video Thoughts: Case scenarios for this are when each thing in a list needs to be both started and finished
#                       for it to be considered a completed list (eg. to do lists, ticket orders, etc.)
#                       For this kind of thing make sure to use stacks.
# Video thoughts 1) Use a stack
import math
def is_valid(combination):
    stack = []
    for par in combination:
        if par == '(':
            stack.append(par)
        else:
            # Validity Condition 1 - not trying to pop from an empty stack (otherwise we found a closing parenthesis
            # without an opening one in front of it
            if len(stack) == 0:
                return False
            else:
                stack.pop()
    # Validity Condition 2 - Stack must be empty at the end (otherwise we have an open parenthesis that did not close
    return len(stack) == 0

def generate(n):
    def rec(n, diff, comb, combs):
        if diff < 0 or diff > n:
            return
        elif n == 0:
            if diff == 0:
                combs.append(''.join(comb))
        else:
            comb.append('(')
            rec(n-1, diff+1, comb, combs)
            comb.pop()
            comb.append(')')
            rec(n-1, diff-1, comb, combs)
            comb.pop()
    combs = []
    # 2*n because n represents pairs, but combination length will be 2*n since length is measuring units, not pairs
    rec(2*n, 0, [], combs)
    print(len(combs)," total pairs")
    return combs

if __name__ == '__main__':
    n = int(input("Please input n: "))
    print(generate(n))
