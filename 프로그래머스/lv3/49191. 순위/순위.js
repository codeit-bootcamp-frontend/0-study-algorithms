function solution(n, results) {
  var answer = 0;

  const g = Array.from({ length: n }, (_, i) => {
    return Array.from({ length: n }, (_, j) => (i == j ? 0 : false));
  });

  results.forEach(([a, b]) => {
    g[a - 1][b - 1] = 1;
    g[b - 1][a - 1] = -1;
  });

  for (let m = 0; m < n; m++) {
    for (let i = 0; i < n; i++) {
      for (let j = 0; j < n; j++) {
        if (g[i][m] == 1 && g[m][j] == 1) {
          g[i][j] = 1;
        }
        if (g[i][m] == -1 && g[m][j] == -1) {
          g[i][j] = -1;
        }
      }
    }
  }

  for (let i = 0; i < n; i++) {
    let flag = false;
    for (let j = 0; j < n; j++) {
      if (g[i][j] === false) {
        flag = true;
        break;
      }
    }
    answer = !flag ? answer + 1 : answer;
  }

  return answer;
}