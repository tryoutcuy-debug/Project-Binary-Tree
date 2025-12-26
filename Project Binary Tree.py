# Kelas Node untuk setiap simpul (node) pohon
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None   # anak kiri
        self.right = None  # anak kanan

# Kelas Binary Search Tree
class BinarySearchTree:
    def __init__(self):
        self.root = None  # akar pohon

    # Fungsi untuk menambah data ke dalam pohon
    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(self.root, data)

    def _insert(self, current, data):
        if data < current.data:
            if current.left is None:
                current.left = Node(data)
            else:
                self._insert(current.left, data)
        elif data > current.data:
            if current.right is None:
                current.right = Node(data)
            else:
                self._insert(current.right, data)
        else:
            print(f"Data {data} sudah ada di pohon.")

    # Fungsi untuk mencari data
    def search(self, value):
        return self._search(self.root, value)

    def _search(self, current, value):
        if current is None:
            return False
        if value == current.data:
            return True
        elif value < current.data:
            return self._search(current.left, value)
        else:
            return self._search(current.right, value)

    # Fungsi untuk menampilkan isi pohon (Inorder Traversal)
    def inorder(self):
        print("Inorder traversal:", end=" ")
        self._inorder(self.root)
        print()

    def _inorder(self, node):
        if node:
            self._inorder(node.left)
            print(node.data, end=" ")
            self._inorder(node.right)

# Membuat objek pohon
bst = BinarySearchTree()

# Menambahkan data
data_list = [123, 111, 135, 109, 120, 140, 130]
for d in data_list:
    bst.insert(d)

# Menampilkan isi pohon
bst.inorder()

# Mencari data tertentu
nim_cari = 159
if bst.search(nim_cari):
    print(f"Data {nim_cari} ditemukan di pohon")
else:
    print(f"Data {nim_cari} tidak ditemukan")