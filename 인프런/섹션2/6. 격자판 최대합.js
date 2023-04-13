function solution(arr) {
  let max = Number.MIN_SAFE_INTEGER;
  let rowSum = 0;
  let columnSum = 0;
  let rightSum = 0;
  let lefthSum = 0;

  for (let i = 0; i < arr.length; i++) {
    rowSum = 0;
    columnSum = 0;
    for (let j = 0; j < arr.length; j++) {
      rowSum += arr[i][j];
      columnSum += arr[j][i];
    }
    max = Math.max(max, rowSum, columnSum);
  }
  for (let i = 0; i < arr.length; i++) {
    rightSum += arr[i][i];
    lefthSum += arr[arr.length - 1 - i][i];
  }
  return Math.max(max, rightSum, lefthSum);
}

let arr = [
  [10, 13, 10, 12, 15],
  [12, 39, 30, 23, 11],
  [11, 25, 50, 53, 15],
  [19, 27, 29, 37, 27],
  [19, 13, 30, 13, 19],
];
console.log(solution(arr));
