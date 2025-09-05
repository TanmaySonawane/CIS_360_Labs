# Tanmay Sonawane CIS 360 Lab 07
# 11/06/24

class Node:
    def __init__(self, value):
        self.value = value
        self.size = 1
        self.depth = 0
        self.parent = self

class UnionFind:
    @staticmethod
    def makeSet(x):
        return Node(x)

    @staticmethod
    def find(x):
        # Find the root of the set containing x, updating depth
        R = x
        x.depth = 0
        while R.parent != R:
            R = R.parent
            x.depth += 1
        return R
    
    @staticmethod
    def union(x, y):
        rootX = UnionFind.find(x)
        rootY = UnionFind.find(y)
        if rootX != rootY:
            rootX.parent = rootY
            rootY.size += rootX.size
            
    @staticmethod
    def find2(x):
        if x.parent != x:
            x.parent = UnionFind.find2(x.parent)
        return x.parent
    
    @staticmethod
    def union2(x, y):
        rootX = UnionFind.find2(x)
        rootY = UnionFind.find2(y)
        
        if rootX != rootY:
            if rootX.size < rootY.size:
                rootX.parent = rootY
                rootY.size += rootX.size
            else:
                rootY.parent = rootX
                rootX.size += rootY.size

# Test
array = [UnionFind.makeSet(i) for i in range(50)]
array2 = [UnionFind.makeSet(i) for i in range(50)]

for i in range(45):
    UnionFind.union(UnionFind.find(array[i]), UnionFind.find(array[i + 5]))

print("Results for union without optimizations:")
for node in array:
    root = UnionFind.find(node)
    print(f"{node.value} ({root.value}, {node.depth})")
    
for i in range(45):
    UnionFind.union2(UnionFind.find2(array2[i]), UnionFind.find2(array2[i + 5]))
    
print("\nResults for union with union-by-size and path compression:")
for node in array2:
    root = UnionFind.find2(node)
    depth = 0
    temp = node
    # Calculate the depth after path compression
    while temp != root:
        temp = temp.parent
        depth += 1
    print(f"{node.value} ({root.value}, {depth})")