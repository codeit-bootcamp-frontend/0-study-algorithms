function solution(n) {
    var answer = 0;
    let i = 0
    while(true) {
        if(n % i === 1) {
            return i
        }
        i++
    }
    return answer;
}