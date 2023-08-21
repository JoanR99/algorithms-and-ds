using System;
namespace Stack
{
    class Node
    {
        public int value;
        public Node? prev;

        public Node(int value)
        {
            this.value = value;
        }
    };

    class Stack
    {
        public int length;
        public Node? head;

        public void push(int value)
        {
            Node newNode = new Node(value);
            length++;

            if (head == null)
            {
                head = newNode;
            }
            else
            {
                head.prev = newNode;
                head = newNode;
            }
        }

        public int pop()
        {
            if (head == null) throw new Exception("Popping from an empty stack");

            length = Math.Max(0, length - 1);

            int value = head.value;

            if (length == 0)
            {
                head = null;
            }
            else
            {
                head = head.prev;
            }

            return value;
        }

        public int peek()
        {
            if (head == null) throw new Exception("Popping from an empty stack");
            return head.value;
        }
    }
    class Program
    {
        public static void Main(string[] args)
        {
            Stack myStack = new Stack();

            myStack.push(5);
            myStack.push(9);
            myStack.push(1);
            myStack.push(4);
            Console.WriteLine(myStack.pop());
            Console.WriteLine(myStack.length);
        }
    }
}
