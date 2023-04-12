function solution(arr) {
  let min = Number.MAX_SAFE_INTEGER;
  for (let x of arr) {
    if (x < min) {
      min = x;
    }
  }
  return min;
}

let arr = [5, 7, 1, 3, 2, 9, 11];
console.log(solution(arr));
