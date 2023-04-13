function solution(n, arr) {
  let answer = 0;
  let max = Number.MIN_SAFE_INTEGER;
  for (let x of arr) {
    let sum = 0;
    for (let num of x.toString()) {
      sum += +num;
    }
    if (sum >= max) {
      answer = Math.max(x, answer);
      max = sum;
    }
  }
  console.log(max);
  return answer;
}

let arr = [1019, 128, 460, 603, 40, 521, 137, 123];
console.log(solution(7, arr));
