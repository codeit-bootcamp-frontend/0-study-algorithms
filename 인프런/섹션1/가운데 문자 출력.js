function solution(s) {
  let mid = parseInt(s.length / 2);
  console.log(mid);
  if (s.length % 2) return s.substring(mid, mid + 1);
  else return s.substring(mid - 1, mid + 1);
}
console.log(solution('wook'));

function solution(s) {
  let mid = parseInt(s.length / 2);
  return s.length % 2 ? s.substr(mid, 1) : s.substr(mid - 1, 2);
}
console.log(solution('wook'));
