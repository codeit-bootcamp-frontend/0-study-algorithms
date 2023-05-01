function solution(n, roads, sources, destination) {
  const visited = new Array(n + 1).fill(Infinity);
  const connect = new Array(n + 1).fill(0).map((_) => []);
  // 모든 정점을 고려하지 않고, 가능한 경로만 담아서 bfs 진행
  roads.forEach(([from, to]) => {
    connect[from].push(to);
    connect[to].push(from);
  });

  // bfs
  const q = [destination];
  visited[destination] = 0;
  while (q.length) {
    const curr = q.shift();
    for (const next of connect[curr]) {
      // 정점 간 거리가 1로 고정되어 있으므로
      if (visited[curr] + 1 < visited[next]) {
        visited[next] = visited[curr] + 1;
        q.push(next);
      }
    }
  }
  return sources.map((source) =>
    visited[source] !== Infinity ? visited[source] : -1
  );
}