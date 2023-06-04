function solution(rectangle, characterX, characterY, itemX, itemY) {
  let g = Array.from(Array(103).fill(0), () => Array(103).fill(0));

  let doubleRect = rectangle.map((_) =>
    _.map((p) => p * 2))
  

  doubleRect.forEach(([x1, y1, x2, y2]) => {
    for (let i = y1; i <= y2; i++) {
      for (let j = x1; j <= x2; j++) {
        if (j === x1 || j === x2 || i === y1 || i === y2) {
          if (g[j][i] === 1) continue;
          else g[j][i] += 1;
        } else {
          g[j][i] += 2;
        }
      }
    }
  });

  characterX *= 2;
  characterY *= 2;
  itemX *= 2;
  itemY *= 2;

  const dx = [1, -1, 0, 0];
  const dy = [0, 0, 1, -1];

  const queue = [[characterX, characterY, 0]];
  g[characterX][characterY] += 100;

  while (queue.length) {
    const [currentX, currentY, count] = queue.shift();

    if (currentX === itemX && currentY === itemY) {
      return count / 2;
    }

    for (let i = 0; i < 4; i++) {
      const [nx, ny] = [currentX + dx[i], currentY + dy[i]];

      if (nx >= 0 && nx < 101 && ny >= 0 && ny < 101)
        if (g[nx][ny] === 1) {
          g[nx][ny] += 100;
          queue.push([nx, ny, count + 1]);
        }
    }
  }
}