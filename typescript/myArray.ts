class MyArray {
	public length: number;
	private data: Record<number, any>;

	constructor() {
		this.length = 0;
		this.data = {};
	}

	public push(item: any) {
		this.data[this.length] = item;
		this.length++;
		return this.length;
	}

	public pop() {
		const removedItem = this.data[this.length - 1];
		delete this.data[this.length - 1];
		this.length--;
		return removedItem;
	}

	public delete(index: number) {
		const removedItem = this.data[index];
		this.shift(index);
		return removedItem;
	}

	public shift(index: number) {
		for (let i = index; i < this.length; i++) {
			this.data[i] = this.data[i + 1];
		}
		delete this.data[this.length - 1];
		this.length--;
	}
}

const numberArray = new MyArray();
numberArray.push(1);
numberArray.push(2);
numberArray.push(3);
numberArray.delete(1);
console.log(numberArray);
