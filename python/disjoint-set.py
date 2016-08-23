class DisjointSet(object):
    def __init__(self, length):
        self.parent = [i for i in range(length)]
        self.size = [1 for i in range(length)]

    def root(self, i):
        if i != self.parent[i]:
            self.parent[i] = self.root(self.parent[i])
        return self.parent[i]

    def connected(self, p, q):
        return self.root(p) == self.root(q)

    def union(self, p, q):
        x = self.root(p)
        y = self.root(q)
        if x == y:
            return
        if self.size[x] < self.size[y]:
            self.parent[x] = y
            self.size[y] += self.size[x]
        else:
            self.parent[y] = x
            self.size[x] += self.size[y]
        return

# The depth of any node x is at most logN, because its depth is increased by
# one only when the size of its tree is smaller, therefore the new tree at least
# doubles in size. However, the tree can only double at most logN times.

ds = DisjointSet(10)
ds.union(1, 2)
ds.union(3, 4)
print ds.connected(1,4)
ds.union(2, 3)
print ds.connected(1,4)
