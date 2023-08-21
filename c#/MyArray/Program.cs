namespace MyArray {
    public class Program {
        public class MyArray {
            public int length;
            public Dictionary<int, dynamic> data;

            public MyArray() {
                length = 0;
                data = new Dictionary<int, dynamic>();
            }

            public void push(dynamic item) {
                data.Add(length, item);
                length++;
            }

            public void pop() {
                data.Remove(length - 1);
            }

            public void shift(int index) {
                for(int i = index; i < length; i++) {
                    if(i + 1 != length) {
                        data[i] = data[i + 1];
                    }
                }
                pop();
                length--;
            }
        }

        static void Main(string[] args) {
            MyArray numberArray = new MyArray();

            numberArray.push(1);
            numberArray.push(2);
            numberArray.push(3);
            numberArray.shift(1);

            foreach (var v in numberArray.data) {
                Console.WriteLine("key {0}, Value {1}", v.Key, v.Value);
            }
            Console.WriteLine(numberArray.length);
        }
    }
}
