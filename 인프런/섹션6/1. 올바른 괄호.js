function solution(s) {
  const arr = s.split('');
  const answer = [];
  for (let x of arr) {
    if (x === '(') answer.push('(');
    else {
      if (answer.length === 0) return;
      answer.pop();
    }
  }
  return answer.length === 0 ? 'YES' : 'NO';
}

let a = '(())()';
console.log(solution(a));
