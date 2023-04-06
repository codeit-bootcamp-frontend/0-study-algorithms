const solution = (board, aloc, bloc) => {
  const dir = [
    [0, 1],
    [0, -1],
    [1, 0],
    [-1, 0],
  ];

  const row = board.length;
  const col = board[0].length;

  const out = (y, x) => {
    if (y < 0 || y >= row || x < 0 || x >= col || !board[y][x]) return false;
    return true;
  };

  const dfs = ([ay, ax], [by, bx], turn, cnt) => {
    if (!board[ay][ax] || !board[by][bx]) return { win: false, cnt: cnt };

    let win_cnt = Infinity;
    let lose_cnt = 0;

    const [currentY, currentX] = turn === 0 ? [ay, ax] : [by, bx];

    board[currentY][currentX] = 0;

    for (let i = 0; i < 4; i++) {
      const [y, x] = dir[i];
      const [dy, dx] = [currentY + y, currentX + x];

      if (!out(dy, dx)) continue;

      const nextTurn =
        turn === 0
          ? dfs([dy, dx], [by, bx], 1 - turn, cnt + 1)
          : dfs([ay, ax], [dy, dx], 1 - turn, cnt + 1);

      if (nextTurn.win === false) win_cnt = Math.min(win_cnt, nextTurn.cnt);
      else lose_cnt = Math.max(lose_cnt, nextTurn.cnt);
    }

    board[currentY][currentX] = 1;

    if (win_cnt === Infinity && lose_cnt === 0) return { win: false, cnt };
    if (win_cnt !== Infinity) return { win: true, cnt: win_cnt };
    return { win: false, cnt: lose_cnt };
  };

  return dfs(aloc, bloc, 0, 0).cnt;
};