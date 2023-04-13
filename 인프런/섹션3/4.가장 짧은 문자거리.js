function solution(s, t) {
  let answer = Array.from({ length: s.length }, () => 1);
  let right = 1;
  for (let i = 0; i < s.length; i++) {
    if (s[i] === t) {
      answer[i] = 0;
      right = 1;
    } else {
      answer[i] = right;
      right++;
    }
  }
  let rightArr = [...answer];

  let left = 1;
  for (let i = s.length - 1; i >= 0; i--) {
    if (s[i] === t) {
      answer[i] = 0;
      left = 1;
    } else {
      answer[i] = Math.min(left, rightArr[i]);
      left++;
    }
  }

  return answer;
}

let str = 'teachermode';
console.log(solution(str, 'e'));
