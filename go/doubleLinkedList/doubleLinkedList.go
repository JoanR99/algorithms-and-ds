package main

import "fmt"

type Node struct {
	value any
	next  *Node
	prev  *Node
}

var head *Node = nil
var tail *Node = nil
var length int = 0

func prepend(value any) {
	newNode := &Node{value: value}
	length += 1

	if head == nil {
		head = newNode
		tail = newNode
		return
	}

	newNode.next = head
	head.prev = newNode
	head = newNode
}

func append(value any) {
	newNode := &Node{value: value}
	length += 1

	if tail == nil {
		head = newNode
		tail = newNode
		return
	}

	tail.next = newNode
	newNode.prev = tail
	tail = newNode
}

func getAt(index int) *Node {
	current := head

	for i := 0; current != nil && i < index; i++ {
		current = current.next
	}

	return current
}

func insertAt(index int, value any) {
	if index == length {
		append(value)
	} else if index == 0 {
		prepend(value)
	}

	length += 1
	current := getAt(index)
	newNode := &Node{value: value}

	newNode.next = current
	newNode.prev = current.prev
	current.prev.next = newNode
	current.prev = newNode

}

func get(index int) any {
	return getAt(index).value
}

func removeNode(node *Node) any {
	length -= 1

	if length == 0 {
		out := head.value
		head = nil
		tail = nil
		return out
	}

	if node.prev != nil {
		node.prev.next = node.next
	}

	if node.next != nil {
		node.next.prev = node.prev
	}

	if node == head {
		head = node.next
	}

	if node == tail {
		tail = node.prev
	}

	node.next = nil
	node.prev = nil

	return node.value
}

func removeAt(index int) any {
	node := getAt(index)

	if node == nil {
		return nil
	}

	return removeNode(node)
}

func remove(item any) any {
	current := head

	for i := 0; current != nil && i < length; i++ {
		if current.value == item {
			break
		}

		current = current.next
	}

	if current == nil {
		return nil
	}

	return removeNode(current)
}

func main() {
	append(5)
	prepend(4)
	fmt.Println(head.value)
	fmt.Println(get(1))
}
