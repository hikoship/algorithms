class Mergesort(object):
    def __init__(self, array):
        self.array = array[:]
        self.aux = [0] * len(array)
        self.sort(0, len(array) - 1)

    def sort(self, left, right):
        if left >= right:
            return
        mid = left + (right - left) / 2
        self.sort(left, mid)
        self.sort(mid + 1, right)
        self.merge(left, right)

    def merge(self, left, right):
        for i in range(left, right + 1):
            self.aux[i] = self.array[i]
        mid = left + (right - left) / 2
        p = left
        q = mid + 1
        for i in range(left, right + 1):
            if p > mid:
                self.array[i] = self.aux[q]
                q += 1
            elif q > right:
                self.array[i] = self.aux[p]
                p += 1
            elif self.aux[p] < self.aux[q]:
                self.array[i] = self.aux[p]
                p += 1
            else:
                self.array[i] = self.aux[q]
                q += 1

ms = Mergesort([4,9,8,6,2,1,6,7,2,3])
print ms.array
