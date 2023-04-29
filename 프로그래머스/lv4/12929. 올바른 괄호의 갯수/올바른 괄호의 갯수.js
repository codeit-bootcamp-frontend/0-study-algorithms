function solution(n) {
  var answer = 0;

  const dfs = (o, c) => {
    if (o + c === n * 2) {
      if (o === n && c === n) {
        answer++;
      }
      return;
    }

    if (o > c) dfs(o, c + 1);
    dfs(o + 1, c);
    return;
  };
  dfs(0, 0);
  return answer;
}