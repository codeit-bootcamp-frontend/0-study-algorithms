function solution(s) {
  let answer = '';
  const stack = [];
  for (let x of s) {
    if (x === '(') stack.push('(');
    if (!stack.length) answer += x;
    else if (x === ')') stack.pop();
  }
  return answer;
}

let str = '(A(BC)D)EF(G(H)(IJ)K)LM(N)';
console.log(solution(str));
