using System;

namespace Queue
{
    class Node
    {
        public int value;
        public Node? next;

        public Node(int value)
        {
            this.value = value;
        }
    };

    class Queue
    {
        public int length = 0;
        private Node? head;
        private Node? tail;

        public void enque(int value)
        {
            Node node = new Node(value);
            length++;

            if (tail == null)
            {
                head = tail = node;
            }
            else
            {
                tail.next = node;
                tail = node;
            }
        }

        public int deque()
        {
            if (head == null) throw new Exception("Queue Empty");
            length--;
            int temp = head.value;
            head = head.next;

            if (length == 0)
            {
                tail = null;
            }

            return temp;
        }

        public int peek()
        {
            if (head == null) throw new Exception("Queue Empty");
            return head.value;
        }
    };

    class Program
    {
        public static void Main(string[] args)
        {
            Queue myQueue = new Queue();

            myQueue.enque(5);
            myQueue.enque(9);
            myQueue.enque(1);
            myQueue.enque(4);
            Console.WriteLine(myQueue.deque());
            Console.WriteLine(myQueue.length);
        }
    }
}




