function solution(s) {
    let answer = ''
    const temp = s.split(' ')
    for(let x of temp) {
        for(let i = 0; i < x.length; i++) {
            // 짝수 인덱스
            if(i % 2 === 0) {
                answer += x[i].toUpperCase()
            // 홀수 인덱스
            } else {
                answer += x[i].toLowerCase()
            }
        }
        answer += ' '
    }
    const temp1 = answer.split(' ')
    temp1.pop()
    answer = temp1
    return answer.join(' ')
}