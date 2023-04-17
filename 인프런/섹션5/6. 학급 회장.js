function solution(s) {
  let answer = '';
  let vote = new Map();
  for (let x of s) {
    if (!vote.has(x)) vote.set(x, 1);
    else vote.set(x, vote.get(x) + 1);
  }
  let max = Number.MIN_SAFE_INTEGER;
  for (let [key, value] of vote) {
    if (value > max) {
      answer = key;
    }
  }
  return answer;
}

let str = 'BACBACCACCBDEDE';
console.log(solution(str));
