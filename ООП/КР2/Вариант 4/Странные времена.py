#!/usr/bin/env python3
# coding:utf-8
class OwnUniverse:
    def __init__(self, *args, name='Vasya'):
        self.comps = list(args)
        self.name = name

    def __truediv__(self, n):
        uni = []
        for i in range(n):
            arg = self.comps[i % len(self.comps)]
            name = self.name + str(i + 1)
            uni.append(OwnUniverse(arg, name=name))
        return uni

    def __iadd__(self, other):
        [self.comps.append(comp) for comp in other.comps if comp not in self.comps]
        return self

    def __call__(self, n):
        return [cmp for cmp in self.comps if len(cmp) % n == 0]

    def __repr__(self):
        return f"OwnUniverse(name: {self.name}, components: {', '.join(self.comps)})"

