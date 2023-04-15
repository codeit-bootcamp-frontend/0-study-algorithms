const readFileSyncAddress = "/dev/stdin";

const input = require("fs")
  .readFileSync(readFileSyncAddress)
  .toString()
  .split("\n");

const N = Number(input[0]);
const M = Number(input[1]);
const city = input
  .slice(2, 2 + N)
  .map((c) => c.trimEnd().split(" ").map(Number));

const paths = input[2 + N].split(" ").map((p) => Number(p) - 1);
const parent = new Array(N).fill(0);

function getParent(num) {
  if (parent[num] === num) return num;
  return (parent[num] = getParent(parent[num]));
}
function union(a, b) {
  const aParent = getParent(a);
  const bParent = getParent(b);

  if (aParent < bParent) parent[bParent] = aParent;
  else parent[aParent] = bParent;
}
function findParent(a, b) {
  const aParent = getParent(a);
  const bParent = getParent(b);

  if (aParent === bParent) return true;
  return false;
}

for (let i = 1; i < N; i++) {
  parent[i] = i;
}
for (let i = 0; i < N; i++) {
  for (let j = i + 1; j < N; j++) {
    if (city[i][j] === 1) union(i, j);
  }
}
for (let i = 1; i < M; i++) {
  if (!findParent(paths[i - 1], paths[i])) {
    console.log("NO");
    return;
  }
}

console.log("YES");