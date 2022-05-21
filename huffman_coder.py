import heapq
from collections import Counter

from utility import Node


def get_freqency(s):
    # 1.1.1.1 get frequency
    freq = Counter(s)
    return freq


def get_huffman_tree(st):
    # 1.1.1 get frequency
    freq = get_freqency(st)
    # 1.1.2 build heap from frequency
    heap = []
    for key in freq:
        nw = Node(ord(key))
        heapq.heappush(heap, (freq[key], nw))

    # 1.1.3 build huffman tree
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)

        nw = Node(left[1].val + right[1].val, left[1], right[1])
        heapq.heappush(heap, (left[0] + right[0], nw))
    return heapq.heappop(heap)[1]


def get_huffman_code(root, code=""):
    # 1.2.1 get huffman code by tree traverse
    if root.left is None and root.right is None:
        return {root.val: code}
    d = {}
    if root.left:
        d.update(get_huffman_code(root.left, code + "0"))
    if root.right:
        d.update(get_huffman_code(root.right, code + "1"))
    return d


def serialize(root):
    # 1.4.1 serialize the tree by pre-order traversal
    if root is None:
        return "|"
    return str(root.val) + "," + serialize(root.left) + "," + serialize(root.right)


def compress(st, mp):
    # 1.3.1 compress the string using huffman code in dictionary
    ret = ""
    for v in st:
        ret += mp[ord(v)]
    return ret


def dummy_tree():
    root = Node(0)
    root.left = Node(1)
    root.right = Node(2)
    root.left.left = Node(3)
    root.left.right = Node(4)
    root.right.left = Node(5)
    root.right.right = Node(6)
    return root


def huffman_encode(st):
    # 1.1 get huffman tree
    root = get_huffman_tree(st)
    # 1.2 get huffman code
    mp = get_huffman_code(root)
    # root = dummy_tree()
    # 1.3 compress the string
    enc = compress(st, mp)
    # 1.4 serialize the tree for storage
    loopup = serialize(root)
    return enc, loopup


if __name__ == "__main__":
    st = "aaaabcd"
    print(huffman_encode(st))
