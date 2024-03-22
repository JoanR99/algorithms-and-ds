from typing import Optional

class Node:
    def __init__(self, value):
        self.value = value
        self.prev: Optional[Node] = None
        self.next: Optional[Node] = None
        
class Double_Linked_List:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.length = 0
        
    def __get_at(self, index):
        current = self.head
        for _n in range(index):
            if current == None:
                break
            current = current.next
            
        return current
    
    def __remove_node(self, node: Node):
        self.length -= 1
        if self.length == 0 and self.head:
            out = self.head.value
            self.head = self.tail = None
            return out
        
        if node.prev:
            node.prev.next = node.next
            
        if node.next:
            node.next.prev = node.prev
            
        if node == self.head:
            self.head = node.next
            
        if node == self.tail:
            self.tail = node.prev
            
        node.prev = node.next = None
        
        return node.value
        
    def prepend(self, item):
        new_node = Node(item)
        self.length += 1
        
        if self.head is None:
            self.head = self.tail = new_node
            
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node
        
    def append(self, item):
        new_node = Node(item)
        self.length += 1
        
        if self.tail is None:
            self.head = self.tail = new_node
            
        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node
            
    def insert_at(self, item, index):
        if index > self.length:
            raise IndexError
        
        if index == self.length:
            self.append(item)
            return 
        elif index == 0:
            self.prepend(item)
            return
        
        self.length += 1
        
        current = self.__get_at(index)
        node = Node(item)
        
        node.next = current
        if current:
            node.prev = current.prev
            current.prev = node
        
        if node.prev:
            node.prev.next = node
            
    def remove(self, item):
        current = self.head
  
        for _n in range(self.length):
            if current and current.value == item:
                break
            if current:
                current = current.next
                
        if (current == None):
            return
		
  
        self.__remove_node(current)
	
    def get(self, idx):
        node = self.__get_at(idx)
        if node:
            return node.value
        else:
            return None
    
	
    def removeAt(self, idx):
        node = self.__get_at(idx)

        if (node == None):
            return None
        
        return self.__remove_node(node);
	
 
my_doble_linked_list = Double_Linked_List()
my_doble_linked_list.append(1);
my_doble_linked_list.append(2);
my_doble_linked_list.append(3);
my_doble_linked_list.removeAt(1);
print(my_doble_linked_list.get(0));
print(my_doble_linked_list.get(1));
