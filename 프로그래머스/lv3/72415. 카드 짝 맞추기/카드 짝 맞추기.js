const solution = (board, r, c) => {
  // 출처 : https://www.youtube.com/watch?v=Q4bTSdi1psw&t=2s
  const bfs = (visited, src, dst) => {
    const out = (x, y) => x < 0 || x > 3 || y < 0 || y > 3;

    const dir = [
      [-1, 0],
      [1, 0],
      [0, -1],
      [0, 1],
    ];

    const graph = Array.from({ length: 4 }, () => Array(4).fill(false));
    const queue = [[...src, 0]];

    while (queue.length) {
      const [y, x, cnt] = queue.shift();
      if (y === dst[0] && x === dst[1]) {
        return cnt;
      }
      for (const [dy, dx] of dir) {
        let [ny, nx] = [y + dy, x + dx];

        if (out(ny, nx)) continue;

        if (!graph[ny][nx]) {
          graph[ny][nx] = true;
          queue.push([ny, nx, cnt + 1]);
        }

        for (let i = 0; i < 2; i++) {
          if (!(visited & (1 << board[ny][nx]))) break;
          if (out(ny + dy, nx + dx)) break;

          [ny, nx] = [ny + dy, nx + dx];
        }
        if (!graph[ny][nx]) {
          graph[ny][nx] = true;
          queue.push([ny, nx, cnt + 1]);
        }
      }
    }

    return Infinity;
  };

  const permutate = (cnt, visited, src) => {
    if (visited === allVisited) {
      answer = Math.min(answer, cnt);
      return;
    }
    for (const [card, pos] of card_pos.entries()) {
      if (visited & (1 << card)) continue;

      const first =
        bfs(visited, src, pos[0]) + bfs(visited, pos[0], pos[1]) + 2;
      const second =
        bfs(visited, src, pos[1]) + bfs(visited, pos[1], pos[0]) + 2;

      permutate(cnt + first, visited | (1 << card), pos[1]);
      permutate(cnt + second, visited | (1 << card), pos[0]);
    }
  };

  const card_pos = new Map();

  let allVisited = 1;
  let answer = Infinity;

  board.forEach((row, y) => {
    row.forEach((card, x) => {
      if (!card) return;

      if (card_pos.has(card)) {
        card_pos.get(card).push([y, x]);
        return;
      }
      card_pos.set(card, [[y, x]]);
      allVisited |= 1 << card;
    });
  });

  permutate(0, 1, [r, c]);
  return answer;
};