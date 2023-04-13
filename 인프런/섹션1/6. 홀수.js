function solution(arr) {
  let sum = 0;
  let min = Number.MAX_SAFE_INTEGER;
  for (let x of arr) {
    if (x % 2) {
      sum += x;
      if (min > x) min = x;
    }
  }
  let answer = [];
  answer.push(sum);
  answer.push(min);
  return answer;
}

arr = [12, 77, 38, 41, 53, 92, 85];
console.log(solution(arr));
