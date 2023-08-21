package main

import "fmt"

type Node struct {
	value int
	next  *Node
}

var head *Node = nil
var tail *Node = nil
var length int = 0

func enqueue(value int) {
	var newNode *Node = &Node{value: value}
	if head == tail {
		head = newNode
		tail = newNode
		return
	}

	tail.next = newNode
	tail = newNode
	length += 1
}

func dequeue() int {
	if head == nil {
		return -1
	}

	var temp *Node = head
	value := temp.value

	if head == tail {
		head = nil
		tail = nil
	} else {
		head = head.next
	}

	temp = nil

	length -= 1
	return value
}

func main() {
	enqueue(5)
	fmt.Println(head.value)
}
