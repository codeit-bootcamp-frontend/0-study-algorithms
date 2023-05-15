function solution(n) {
    let numberLength = String(n).length;
    let answer = 0
    function DFS() {
        if(!numberLength) return
        else answer += parseInt(n % 10)
        n = parseInt(n /10)
        numberLength--
        DFS()
    }
    DFS()
    return answer
}