const reset = (block) => {
  let minY = Math.min(...block.map((v) => v[0]));
  let minX = Math.min(...block.map((v) => v[1]));

  return block.map((v) => [v[0] - minY, v[1] - minX]).sort();
};

const rotate = (block) => {
  let max = Math.max(...block.map((v) => Math.max(v[0], v[1])));
  let rotatedBlock = block.map((v) => [max - v[1], v[0]]);

  return reset(rotatedBlock);
};

const bfs = (start, list, k) => {
  const dy = [1, -1, 0, 0];
  const dx = [0, 0, 1, -1];

  let queue = start;
  let block = [];
  while (queue.length > 0) {
    const [cy, cx] = queue.shift();
    block.push([cy, cx]);
    for (let i = 0; i < 4; i++) {
      let ny = cy + dy[i];
      let nx = cx + dx[i];

      if (nx < 0 || ny < 0 || nx >= list.length || ny >= list.length) continue;
      else if (list[ny][nx] === k) continue;
      else {
        queue.push([ny, nx]);
        list[ny][nx] = k;
      }
    }
  }
  return reset(block);
};

const solution = (game_board, table) => {
  const blanks = [];
  const puzzles = [];

  for (let y = 0; y < game_board.length; y++) {
    for (let x = 0; x < game_board[0].length; x++) {
      if (game_board[y][x] === 0) {
        game_board[y][x] = 1;
        blanks.push(bfs([[y, x]], game_board, 1));
      }
      if (table[y][x] === 1) {
        table[y][x] = 0;
        puzzles.push(bfs([[y, x]], table, 0));
      }
    }
  }

  let answer = 0;
  puzzles.forEach((val) => {
    for (let i = 0; i < blanks.length; i++) {
      let match = false;
      for (let j = 0; j < 4; j++) {
        val = rotate(val);
        if (JSON.stringify(val) === JSON.stringify(blanks[i])) {
          blanks.splice(i, 1);
          answer += val.length;
          match = true;
          break;
        }
      }
      if (match) break;
    }
  });
  return answer;
};