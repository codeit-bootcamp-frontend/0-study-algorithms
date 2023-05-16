function solution(n) {
    var answer = [];
    let string = String(n)
    for(let x of string) answer.push(+x)
    return answer.reverse()
}