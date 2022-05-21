from tqdm import trange


class Node:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right

    def __lt__(self, other):
        return self.val <= other.val


def binary_add(a, b):
    if len(a) < len(b):
        a, b = b, a

    b = "0" * (len(a) - len(b)) + b

    carry = 0
    ret = ""
    for i in range(len(a) - 1, -1, -1):
        v = int(a[i]) + int(b[i]) + carry
        carry = v // 2
        ret = str(v % 2) + ret

    if carry:
        ret = "1" + ret

    return ret


def binary_sub(a, b):
    if len(a) < len(b):
        a, b = b, a

    b = "0" * (len(a) - len(b)) + b

    carry = 0
    ret = ""
    for i in range(len(a) - 1, -1, -1):
        v = int(a[i]) - int(b[i]) - carry
        if v < 0:
            v += 2
            carry = 1
        else:
            carry = 0
        ret = str(v) + ret

    return ret


def binary_multiply(a, b):
    if len(a) < len(b):
        a, b = b, a

    b = "0" * (len(a) - len(b)) + b

    ret = "0" * len(a)
    for i in trange(len(b) - 1, -1, -1):
        if b[i] == "1":
            ret = binary_add(ret, a)
        a = binary_add(a, a)
    return ret


def binary_to_decimal(a):
    return int(a, 2)


def decimal_to_binary(a):
    return bin(a)[2:]


def invert(a):
    return "".join(["1" if x == "0" else "0" for x in a])


def two_complement(a):
    a = invert(a)
    a = binary_add(a, "1")
    return a


def reverse_binary(a):
    return a[::-1]
