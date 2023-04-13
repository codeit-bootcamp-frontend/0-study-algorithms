function solution(s) {
  let answer = '';
  for (let x of s) {
    if (x == 'A') answer += '#';
    else answer += x;
  }
  return answer;
}

let str = 'BANANA';
console.log(solution(str));

function solution(s) {
  return s.replace(/A/g, '#');
}

let str = 'BANANA';
console.log(solution(str));

// ㅇ// 리턴값으로는 어떤 패턴에 일치하는 일부 또는 모든 부분이 교체된 새로운 문자열
