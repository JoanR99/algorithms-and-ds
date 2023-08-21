const firstArray = [0, 3, 4, 22, 31];
const secondArray = [4, 6, 13, 30];

const mergeArray = (firstArray: number[], secondArray: number[]): number[] => {
	if (!Array.isArray(firstArray) || !Array.isArray(secondArray)) {
		throw new Error('Parameters must be arrays');
	}
	const result: number[] = [];
	const finalLength = firstArray.length + secondArray.length - 2;
	let f = 0;
	let s = 0;

	for (let i = 0; i <= finalLength; i++) {
		if (f >= firstArray.length) {
			result.push(...secondArray.slice(s));
			break;
		} else if (s >= secondArray.length) {
			result.push(...firstArray.slice(f));
			break;
		} else if (firstArray[f] < secondArray[s]) {
			result.push(firstArray[f]);
			f++;
		} else {
			result.push(secondArray[s]);
			s++;
		}
	}

	return result;
};

console.log(mergeArray(firstArray, secondArray));
