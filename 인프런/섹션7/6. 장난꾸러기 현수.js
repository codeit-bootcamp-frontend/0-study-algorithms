function solution(arr) {
  let a = [];
  let answer = [...arr];
  answer.sort((a, b) => a - b);
  for (let i = 0; i < arr.length; i++) {
    if (answer[i] !== arr[i]) a.push(i + 1);
  }
  return a;
}

let arr = [120, 125, 152, 130, 135, 135, 143, 127, 160];
console.log(solution(arr));
