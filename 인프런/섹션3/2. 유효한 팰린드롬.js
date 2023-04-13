function solution(s) {
  s = s.toLowerCase().replace(/[^a-z]/g, '');
  return s === s.split('').reverse().join('') ? 'YES' : 'NO';
}

let str = 'found7, time: study; Yduts; emit, 7Dnuof';
console.log(solution(str));
