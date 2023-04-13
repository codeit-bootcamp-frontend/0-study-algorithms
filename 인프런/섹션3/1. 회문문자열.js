function solution(s) {
  let str = s.toLowerCase();
  for (let i = 0; i < parseInt(s.length / 2); i++) {
    if (str[i] !== str[s.length - 1 - i]) {
      return false;
    }
    return true;
  }
}

let str = 'ksoqa';
console.log(solution(str));

function solution(s) {
  return s === s.split('').reverse().join('') ? true : false;
}

let str = 'ksoac';
console.log(solution(str));
