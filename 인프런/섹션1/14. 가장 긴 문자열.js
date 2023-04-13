function solution(s) {
  let max = Number.MIN_SAFE_INTEGER;
  let idx = 0;
  for (let i = 0; i < s.length; i++) {
    if (s[i].length > max) {
      max = s[i].length;
      idx = i;
    }
  }
  return s[idx];
}
let str = ['teacher', 'time', 'student', 'beautiful', 'good'];
console.log(solution(str));
