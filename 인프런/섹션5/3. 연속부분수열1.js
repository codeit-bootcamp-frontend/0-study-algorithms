function solution(m, arr) {
  let answer = 0;
  let sum = 0;
  let headIndex = 0;
  for (let tailIndex = 0; tailIndex < arr.length; tailIndex++) {
    sum += arr[tailIndex];
    if (sum === m) answer++;
    while (sum >= m) {
      sum -= arr[headIndex++];
      if (sum === m) answer++;
    }
  }
  return answer;
}

let a = [1, 2, 1, 3, 1, 1, 1, 2];
console.log(solution(6, a));
