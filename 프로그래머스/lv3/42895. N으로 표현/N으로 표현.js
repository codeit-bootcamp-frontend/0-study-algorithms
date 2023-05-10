function solution(N, number) {
  const operations = [
    (a, b) => a + b,
    (a, b) => a * b,
    (a, b) => a - b,
    (a, b) => (a / b) >> 0,
  ];

  const dp = new Array(9).fill(0).map((el) => new Set());

  for (let select = 1; select < 9; select++) {
    dp[select].add("1".repeat(select) * N);
    for (let cases = 1; cases < select; cases++) {
      for (const opFunc of operations) {
        for (const arg1 of dp[cases]) {
          for (const arg2 of dp[select - cases]) {
            dp[select].add(opFunc(arg1, arg2));
          }
        }
      }
    }
    if (dp[select].has(number)) return select;
  }
  return -1;
}