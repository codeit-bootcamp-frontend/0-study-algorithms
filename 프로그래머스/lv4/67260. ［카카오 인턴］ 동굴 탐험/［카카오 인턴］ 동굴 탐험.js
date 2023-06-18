function solution(n, path, order) {
  var edge = Array.from({ length: n }, () => []);
  var need = Array(n);
  var visited = Array(n).fill(false);

  for (const o of order) need[o[1]] = o[0];

  if (need[0]) return false;

  for (const p of path) {
    edge[p[0]].push(p[1]);
    edge[p[1]].push(p[0]);
  }

  const q = [0];
  const tracked = new Array(n).fill(-1);
  var cnt = 1;
  visited[0] = true;

  while (q.length) {
    const curr = q.shift();

    for (const next of edge[curr]) {
      const needtovisit = need[next];
      if (needtovisit && !visited[needtovisit]) {
        tracked[needtovisit] = next;
        continue;
      }

      if (visited[next]) continue;

      if (tracked[next] !== -1) {
        cnt++;
        visited[tracked[next]] = true;
        q.push(tracked[next]);
      }

      visited[next] = true;
      cnt++;
      q.push(next);
    }
  }

  return cnt === n ? true : false;
}