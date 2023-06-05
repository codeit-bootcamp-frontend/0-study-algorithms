function solution(array, commands) {
    var answer = [];
    for(let x of commands) {
        let temp = [...array]
        let splice = array.slice(x[0] - 1, x[1])
        splice.sort((a, b) => a - b)
        answer.push(splice[x[2] - 1])
    }
    return answer;
}