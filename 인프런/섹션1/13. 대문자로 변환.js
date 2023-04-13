function solution(s) {
  let answer = '';
  for (let x of s) {
    let num = x.charCodeAt();
    if (65 <= num && num <= 90) answer += String.fromCharCode(num + 32);
    else answer += String.fromCharCode(num - 32);
  }
  return answer;
}

console.log(solution('StuDY'));
ß;
