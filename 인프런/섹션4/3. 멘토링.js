function solution(test) {
  for (let i = 1; i <= test[0].length; i++) {
    // i멘토
    for (let j = 1; j <= test[0].length; j++) {
      // j 멘티
      let count = 0;
      for (let k = 0; k < test.length; k++) {
        let pi = 0;
        let pj = 0;
        for (let s = 0; s < test[0].length; s++) {
          if (test[k][s] === i) pi = s; // 각 행에 대한 i와 j의 위치 정의
          if (test[k][s] === j) pj = s;
        }
        if (pi < pj) count++;
      }
      if (count === test.length) return count;
    }
  }
}

let arr = [
  [3, 4, 1, 2],
  [4, 3, 2, 1],
  [3, 1, 4, 2],
];
console.log(solution(arr));
