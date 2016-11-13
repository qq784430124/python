from functools import reduce
import string
def str2float(s):
    n = s.find('.')
    if n == - 1:
        return s
    return (reduce(lambda x, y: x * 10 + y, map(lambda x: int(x), iter(s[:n]))) +
            reduce(lambda x, y: x * 10 + y, map(lambda x: int(x), iter(s[n + 1:]))) * 10 ** (n - (len(s) - 1)))
print(str2float('123.456'))