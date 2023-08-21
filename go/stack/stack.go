package main

import "fmt"

type Node struct {
	value int
	prev  *Node
}

var head *Node = nil
var length int = 0

func push(value int) {
	var newNode *Node = &Node{value: value}
	length += 1

	if head == nil {
		head = newNode
	} else {
		newNode.prev = head
		head = newNode
	}
}

func pop() int {
	if head == nil {
		return -1
	}
	length = max(0, length-1)

	if length == 0 {
		var temp *Node = head
		value := temp.value
		head = nil
		return value
	}

	var temp *Node = head
	value := temp.value
	head = head.prev
	return value
}

func peek() int {
	return head.value
}

func main() {
	push(5)
	push(3)
	push(7)
	push(9)
	pop()
	fmt.Println(head.value)
	fmt.Println(length)
}
