function solution(board) {
  let answer = 0;
  let size = board.length;
  let isChange = true;

  while (isChange) {
    isChange = false;
    for (let i = 0; i < size; i++) {
      let y = 0;

      while (y < size && board[y][i] === 0) y++;

      if (1 < y && y < size) {
        y--;
        board[y][i] = -1;
        board[y - 1][i] = -1;
      } else if (y == 1) {
        y--;
        board[y][i] = -1;
      }
    }
    for (let i = 0; i < size; i++)
      for (let j = 0; j < size; j++) {
        let mcnt = 0;
        let bcnt = 0;
        let fnum = 0;
        let impossible = false;

        top: for (let y = i; y < i + 3 && y < size; y++) {
          for (let x = j; x < j + 2 && x < size; x++) {
            if (board[y][x] == -1) mcnt++;
            else if (board[y][x] != 0 && fnum == 0) {
              fnum = board[y][x];
              bcnt++;
            } else if (board[y][x] != 0 && fnum == board[y][x]) {
              
              bcnt++;
            } else {
              impossible = true;
              break top;
            }
          }
        }
        if (!impossible && mcnt == 2 && bcnt == 4) {
          answer++;
          isChange = true;
          for (let y = i; y < i + 3; y++) {
            for (let x = j; x < j + 2; x++) {
              board[y][x] = 0;
            }
          }
        }

        if (isChange) continue;
        mcnt = 0;
        bcnt = 0;
        fnum = 0;
        impossible = false;

        bottom: for (let y = i; y < i + 2 && y < size; y++) {
          for (let x = j; x < j + 3 && x < size; x++) {
            if (board[y][x] == -1) mcnt++;
            else if (board[y][x] != 0 && fnum == 0) {
              fnum = board[y][x];
              bcnt++;
            } else if (board[y][x] != 0 && fnum == board[y][x]) bcnt++;
            else {
              impossible = true;
              break bottom;
            }
          }
        }

        if (!impossible && mcnt == 2 && bcnt == 4) {
          isChange = true;
          answer++;
          for (let y = i; y < i + 2; y++) {
            for (let x = j; x < j + 3; x++) {
              board[y][x] = 0;
            }
          }
        }
      }

    if (isChange)
      for (let i = 0; i < size; i++)
        for (let j = 0; j < size; j++) {
          if (board[i][j] == -1) {
            board[i][j] = 0;
          }
        }
  }
  return answer;
}