function solution(arr, divisor) {
    var answer = [];
    arr.sort((a, b) => a-b)
    for(let x of arr) {
        if(x % divisor === 0) {
            answer.push(x)
        }
    }
    if (answer.length === 0) return [-1]
    return answer;
}