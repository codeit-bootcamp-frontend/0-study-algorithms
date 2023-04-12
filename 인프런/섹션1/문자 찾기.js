function solution(s, t) {
  let answer = 0;
  for (let x of s) {
    if (x === t) answer++;
  }
  return answer;
}

let str = 'COMPUTERPROGRAMMING';
console.log(solution(str, 'R'));

function solution(s, t) {
  return s.split(t).length - 1;
}

let str = 'COMPUTERPROGRAMMING';
console.log(solution(str, 'R'));
// split() 메소드는 구분자를 이용하여 문자열을 배열로 바꾸는 메소드
