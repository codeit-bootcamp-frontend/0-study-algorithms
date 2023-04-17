function solution(m, arr) {
  let answer = 0;
  let sum = 0;
  let headIdx = 0;
  for (let tailIdx = 0; tailIdx < arr.length; tailIdx++) {
    sum += arr[tailIdx];
    while (sum > m) {
      sum -= arr[headIdx++];
    }
    answer += tailIdx - headIdx + 1;
  }
  return answer;
}

let a = [1, 3, 1, 2, 3];
console.log(solution(5, a));
