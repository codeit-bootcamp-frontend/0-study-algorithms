function solution(arr) {
  let answer = arr;
  let sum = arr.reduce((a, b) => a + b, 0);
  for (let i = 0; i < 8; i++) {
    for (let j = i + 1; j < 9; j++) {
      if (sum - (answer[i] + answer[j]) == 100) {
        answer.splice(j, 1);
        answer.splice(i, 1);
      }
    }
  }
  return answer;
}

let arr = [20, 7, 23, 19, 10, 15, 25, 8, 13];
console.log(solution(arr));

// splice 메소드는 제거한 요소를 담은 배열은 반환한다. splice(시작 인덱스, 0, 'dog') 형식으로 추가할 수 있으며 splice(시작 인덱스, 제거할 요소 갯수)
// 배열의 합을 구할 때는 for문을 이용하지말고 reduce 메소드를 사용하자
