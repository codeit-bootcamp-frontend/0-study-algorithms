function solution(a, edges) {
  const tree = new Array(a.length).fill().map((_) => []);
  for (const [u, v] of edges) {
    tree[u].push(v);
    tree[v].push(u);
  }

  const stack = [[0, -1]];
  const visit = new Array(a.length).fill(false);

  let answer = 0n; // BigInt(0)
  while (stack.length) {
    const [start, parent] = stack.pop();

    if (visit[start]) {
      a[parent] += a[start];
      answer += BigInt(Math.abs(a[start]));
      continue;
    }

    stack.push([start, parent]);
    visit[start] = true;

    for (const next of tree[start]) {
      if (!visit[next]) {
        stack.push([next, start]);
      }
    }
  }

  return a[0] ? -1 : answer;
}