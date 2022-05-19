import math
import os
import random
import re
import sys


#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    arr.sort()
    number_of_ele = [len(arr[0:arr.index(0)]), arr.count(0)]
    arr.reverse()
    number_of_ele.insert(0, len(arr[0:arr.index(0)]))
    neg_reg = re.compile('^-?[1-9]\d*(\.\d+)?$')
    pos_reg = re.compile('^[1-9]\d*(\.\d+)?$')
    ele = [filter(neg_reg.match, arr), arr.count(0), filter(pos_reg.match, arr)]
    print(ele)
    output = ["{:.6f}".format(x / n) for x in number_of_ele]
    print(*output, sep="\n")

    neg_ele = [x for x in arr if x < 0]
    pos_ele = [x for x in arr if x > 0]
    output = ["{:.6f}".format(len(pos_ele) / n), "{:.6f}".format(len(neg_ele) / n), "{:.6f}".format(arr.count(0) / n)]
    print(*output, sep="\n")


def miniMaxSum(arr):
    # Write your code here
    output = [sum(arr) - x for x in arr]
    print(min(output), max(output), sep="  ")


miniMaxSum([1, 2, 3, 4, 5])

if __name__ == '__main__':
    # n = int(input().strip())
    # if n % 2 != 0 or n in range(6, 21):
    #     print("Weird")
    # else:
    #     if n in [2, 4] or n > 20:
    #         print("Not Weird")
    # x = int(input())
    # y = int(input())
    # z = int(input())
    # n = int(input())
    # print([[a, b, c] for a in range(x + 1) for b in range(y + 1) for c in range(z + 1) if a + b + c != n])
    # n = int(input("input"))
    # import pdb
    # pdb.set_trace()
    # arr = list(set(map(int, input("list").split())))
    # arr.sort()
    # print(arr)
    # # print(arr[-2])

    # n, m = map(int, input().split())

    # top cone
    # for i in range(1, n, 2):
    #     print((".|." * i).center(m, '-'))
    #
    # # center
    # print(("WELCOME").center(m, '-'))
    #
    # # lower cone
    # for i in range(n - 2, 0, -2):
    #     print((".|." * i).center(m, '-'))

    # for i in range(1, n + 1):
    #     print('{:>12d} {:>12o} {:>12X} {:>12b}'.format(i, i, i, i))
    # n = 10
    # letters = list(map(chr, range(96 + n, 96, -1))) + list(map(chr, range(98, 96 + n + 1)))
    # for i in range(0, n - 1):
    #     print("-".join(letters[:i] + letters[i::-1]).center(len(letters) * 2 - 1, "-"))
    #
    # for i in range(n - 1, -1, -1):
    #     print("-".join(letters[:i] + letters[i::-1]).center(len(letters) * 2 - 1, "-"))
    string = "BANANA"


    def minion_game(string):
        # your code goes here
        # winner = {"Kelvin": 0, "Stuart": 0}
        # for i in range(0, len(string)):
        #     for j in range(i + 1, len(string) + 1):
        #         w = "".join(string[i:j])
        #         if w.startswith(('A', 'E', 'I', 'O', 'U')):
        #             winner["Kelvin"] += 1
        #         else:
        #             winner["Stuart"] += 1
        # if winner["Kelvin"] == winner['Stuart']:
        #     print("Draw")
        # else:
        #     print(*max(winner.items(), key=lambda x: x[1]))
        vowels = ['A', 'E', 'I', 'O', 'U']
        vs = 0
        cs = 0
        for i, s in enumerate(string):
            if s in (vowels):
                vs += len(s) - i
            else:
                cs += len(s) - i
        print(vs, cs)


    minion_game(string)


def factorial(n):
    # Write your code here
    return n * factorial(n - 1) if n > 1 else 1


print(factorial(3))

arr = [[1, 1, 1, 0, 0, 0],
       [0, 1, 0, 0, 0, 0],
       [1, 1, 1, 0, 0, 0],
       [0, 0, 2, 4, 4, 0],
       [0, 0, 0, 2, 0, 0],
       [0, 0, 1, 2, 4, 0]]
output = []

for i in range(len(arr)):
    for j in range(len(arr) - 2):
        try:
            print(f"{j} : {arr[i][j:j + 3], arr[i + 1][j + 1], arr[i + 2][j:j + 3]}", sep="/n")
            print(sum(arr[i][j:j + 3]) + arr[i + 1][j + 1] + sum(arr[i + 2][j:j + 3]))
            output.append(sum(arr[i][j:j + 3]) + arr[i + 1][j + 1] + sum(arr[i + 2][j:j + 3]))
        except IndexError:
            pass
print(max(output))
