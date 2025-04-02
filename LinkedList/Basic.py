### [Recommend video](https://www.youtube.com/watch?v=KV6XW2Y7NAQ&ab_channel=Dr.Bean%EC%9D%98%EC%BD%94%EB%94%A9%EA%B5%90%EC%8B%A4)



class Node():
  def __init__(self, value = None):
    self.data = value
    self.next = None

class LinkedList():
  def __init__(self):
    self.head = Node() # first node in the LinkedList
  def insert(self, pos, value):
    newNode = Node(value)
    newNode.next = pos.next
    pos.next = newNode

  def delete(self,pos):
    pos.next = pos.next.next

  def delete_value(self, value):
    pos = self.head.next
    while pos != None:
      if pos.next != None and pos.next.data == value:
        self.delete(pos)
      pos = pos.next
        

  def Print(self):
    pos = self.head.next
    while pos != None:
      print(f'{pos.data} -->' ,end = ' ')
      pos = pos.next
