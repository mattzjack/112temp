s0 = set()
s1 = set()
x = None
len(s0)
x in s0
x not in s0
s0.isdisjoint(s1)
s0.issubset(s1)
s0 <= s1
s0 < s1
s1.issuperset(s0)
s1 >= s0
s1 > s0
s0.union(s1)
s0 | s1
s0.intersection(s1)
s0 & s1
s0.difference(s1)
s0 - s1
s0.symmetric_difference(s1)
s0 ^ s1
s0.copy()
s0.update(s1)
s0 |= s1
s0.intersection_update(s1)
s0 &= s1
s0.difference_update(s1)
s0 -= s1
s0.symmetric_difference_update(s1)
s0 ^= s1
s0.add(x)
s0.remove(x)
s0.discard(x)
s0.pop()
s0.clear()

d = dict()
len(d)
k = 0
d[k] = x
d[k]
del d[k]
k in d
k not in d
iter(d)
d.clear()
d.copy()
newD = dict.fromkeys(['k0', 'k1'], 123)
d.get(k0, None)
for (k, v) in d.items():
    for k in d.keys():
        for v in d.values():
            x = d.pop(k, -1)
d.popitem()
x = d.setdefault(k, 0)
d.update(newD)
