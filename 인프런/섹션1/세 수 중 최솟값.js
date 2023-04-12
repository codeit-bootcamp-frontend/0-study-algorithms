function solution(a, b, c) {
  let answer = a > b ? b : a;
  return answer > c ? c : answer;
}

console.log(solution(2, 5, 1));

// 개쉬움
