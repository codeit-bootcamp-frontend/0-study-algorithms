function solution(n) {
    const answer = []
    let numAnswer = 0
    function DFS() {
        if(n === 0) return
        else {
            let num = n % 3
            n = Math.floor(n / 3)
            DFS()
            answer.push(num)
        }
    }
    DFS()
    for(let i = 0; i < answer.length; i++) {
        numAnswer += (3 ** i) * answer[i]
    }
    return numAnswer
}