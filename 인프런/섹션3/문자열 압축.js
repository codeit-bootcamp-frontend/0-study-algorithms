function solution(s) {
  let answer = '';
  let count = 1;
  for (let i = 0; i < s.length; i++) {
    if (s[i] === s[i + 1]) {
      count++;
    } else {
      answer += s[i];
      if (count === 1) answer += '';
      else answer += count.toString();
      count = 1;
    }
  }
  return answer;
}

let str = 'KKHSSSSSSSE';
console.log(solution(str));
