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

// str.replace(regexp|substr, newSubstr|function) 형식으로 첫번째 파라미터에 정규표현식을 넣을 수도 있다
// 리턴값으로는 어떤 패턴에 일치하는 일부 또는 모든 부분이 교체된 새로운 문자열
