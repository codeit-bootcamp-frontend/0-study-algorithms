function solution(scores) {
  let answer = 1;
  const target = scores[0];

  scores.sort((a, b) => {
    if (a[0] !== b[0]) return b[0] - a[0];
    return a[1] - b[1];
  });

  let before = 0;
  for (const s of scores) {
    if (target[0] < s[0] && target[1] < s[1]) return -1;

    if (before <= s[1]) {
      if (target[0] + target[1] < s[0] + s[1]) answer++;
      before = s[1];
    }
  }
  return answer;
}