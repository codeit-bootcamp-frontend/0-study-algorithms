function solution(arr) {
  let total = 0;
  let cnt = 1;
  for (let x of arr) {
    if (x === 1) {
      total += cnt;
      cnt++;
    } else cnt = 1;
  }
  return total;
}

let arr = [1, 0, 1, 1, 1, 0, 0, 1, 1, 0];
console.log(solution(arr));
