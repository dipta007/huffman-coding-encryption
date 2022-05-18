class Node:
  def __init__(self, val=0, left=None, right=None) -> None:
    self.val = val
    self.left = left
    self.right = right
  
  def __lt__(self, other):
    return self.val <= other.val
