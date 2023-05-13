function solution(a) {
  let ans = 0;

  a.reduce((acc, cur) => {
    acc[cur] ? acc[cur][1]++ : (acc[cur] = [cur, 1]);
    return acc;
  }, [])
    .filter((el) => el)
    .sort((a, b) => b[1] - a[1])
    .map(([elem, count]) => {
      if (ans >= count) return;

      let cnt = 0;
      for (let i = 0; i < a.length; i++) {
        if (a[i + 1] === undefined) continue;
        if (a[i] === a[i + 1]) continue;
        if (a[i] !== elem && a[i + 1] !== elem) continue;

        cnt++;
        i++;
      }
      ans = Math.max(ans, cnt);
    });

  return ans * 2;
}