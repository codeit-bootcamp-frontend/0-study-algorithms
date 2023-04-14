function solution(arr1, arr2) {
  let answer = [];
  let i = 0;
  let j = 0;

  while (i < arr1.length && j < arr2.length) {
    if (arr1[i] < arr2[j]) {
      answer.push(arr1[i]);
      i++;
    } else {
      answer.push(arr2[j]);
      j++;
    }
  }

  while (j < arr2.length) {
    answer.push(arr2[j]);
    j++;
  }

  while (i < arr1.length) {
    answer.push(arr1[i]);
    i++;
  }
  return answer;
}

let a = [1, 3, 5];
let b = [2, 3, 6, 7, 9];
console.log(solution(a, b));
