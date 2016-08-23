#include <iostream>
#include <vector>

using namespace std;

class DisjointSet {
    private:
        vector<int> parent, size;

        int root(int i) {
            if (i != parent[i])
                parent[i] = root(parent[i]);
            return parent[i];
        }

    public:
        DisjointSet(int length) {
            parent.reserve(length);
            size.reserve(length);
            for (int i = 0; i < length; i++) {
                parent.push_back(i);
                size.push_back(1);
            }
        }

        bool connected(int p, int q) {
            return root(p) == root(q);
        }

        void unite(int p, int q) {
            int x = root(p);
            int y = root(q);
            if (x == y) return;
            if (size[x] < size[y]) {
                parent[x] = y;
                size[y] += size[x];
            }
            else {
                parent[y] = x;
                size[x] += size[y];
            }
        }
};

int main() {
    DisjointSet ds(10);
    ds.unite(1, 2);
    ds.unite(3, 4);
    cout << ds.connected(1,4) << endl;
    ds.unite(2, 3);
    cout << ds.connected(1,4) << endl;

    return 0;
}
