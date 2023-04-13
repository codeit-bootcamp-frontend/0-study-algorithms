function solution(a, b, c) {
  let sum = a + b + c;
  let max;
  if (a > b) {
    max = a;
  } else {
    max = b;
  }
  if (max < c) max = c;
  return sum > 2 * max ? true : false;
}

console.log(solution(17, 33, 17));

// 개쉬움
