function solution(s) {
    var answer = true;
    let sum = 0
    for(let x of String(s)) {
        sum += Number(x)
    }
    
    return !(Number(s) % sum)
}