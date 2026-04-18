# 1-mashq
from collections import OrderedDict

cache = OrderedDict()

def get(k):
    if k not in cache:
        return -1
    cache.move_to_end(k)
    return cache[k]

def put(k,v):
    if k in cache:
        cache.move_to_end(k)
    cache[k]=v
    if len(cache)>2:
        cache.popitem(last=False)
# 2-mashq
from itertools import permutations

nums = list(map(int, input().split()))
print(list(permutations(nums)))
# 3-mashq
from itertools import combinations

nums = list(map(int, input().split()))
print(list(combinations(nums,2)))
# 4-mashq
def power(a,b):
    if b==0:
        return 1
    if b%2==0:
        t = power(a,b//2)
        return t*t
    return a*power(a,b-1)

a,b = map(int,input().split())
print(power(a,b))
# 5-mashq
n = int(input())
col = set()
diag1 = set()
diag2 = set()

def solve(r):
    if r == n:
        return 1
    count = 0
    for c in range(n):
        if c in col or r+c in diag1 or r-c in diag2:
            continue
        col.add(c); diag1.add(r+c); diag2.add(r-c)
        count += solve(r+1)
        col.remove(c); diag1.remove(r+c); diag2.remove(r-c)
    return count

print(solve(0))
