function solution(s) {
  let str = new Set();
  for (let x of s) {
    str.add(x);
  }
  let answer = Array.from(str).join('');
  return answer;
}
console.log(solution('ksekkset'));

function solution(s) {
  let answer = '';
  for (let i = 0; i < s.length; i++) {
    if (s.indexOf(s[i]) === i) answer += s[i];
  }
  return answer;
}
console.log(solution('ksekkset'));
