class HashTable {
	private data: any[][];

	constructor(size: number) {
		this.data = new Array(size);
	}

	private _hash(key: string) {
		let hash = 0;
		for (let i = 0; i < key.length; i++) {
			hash = (hash + key.charCodeAt(i) * i) % this.data.length;
		}

		return hash;
	}

	set(key: string, value: any) {
		const address = this._hash(key);
		if (!this.data[address]) {
			this.data[address] = [];
		}
		this.data[address].push([key, value]);
	}

	get(key: string) {
		const address = this._hash(key);
		const currentBucket = this.data[address];

		if (currentBucket) {
			for (let i = 0; i < currentBucket.length; i++) {
				if (currentBucket[i][0] == key) {
					return currentBucket[i][1];
				}
			}
		}

		return undefined;
	}
}

const joan = new HashTable(20);
joan.set('name', 'Joan');
console.log(joan.get('name'));
