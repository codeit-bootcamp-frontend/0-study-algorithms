function solution(n, k, card) {
  let answer = [];
  let set = new Set();
  let len = card.length;
  for (let i = 0; i < len - 2; i++) {
    for (let j = i + 1; j < len - 1; j++) {
      for (let k = j + 1; k < len; k++) {
        set.add(card[i] + card[j] + card[k]);
      }
    }
  }
  let arr = Array.from(set);
  arr.sort((a, b) => b - a);
  console.log(arr);
  return arr[k - 1];
}

let arr = [13, 15, 34, 23, 45, 65, 33, 11, 26, 42];
console.log(solution(10, 3, arr));
