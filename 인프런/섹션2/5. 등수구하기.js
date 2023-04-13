function solution(arr) {
  let answer = Array.from({ length: 5 }, () => 1);
  for (let i = 0; i < arr.length; i++) {
    for (let j = 0; j < arr.length; j++) {
      if (arr[i] < arr[j]) answer[i]++;
    }
    answer[i] = count;
  }
  return answer;
}

let arr = [87, 89, 92, 92, 76];
console.log(solution(arr));
