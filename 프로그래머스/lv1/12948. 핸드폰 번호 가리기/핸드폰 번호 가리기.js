function solution(phone_number) {
    const answer = Array.from(phone_number)
    for(let i = 0; i < phone_number.length - 4; i++) {
        answer[i] = '*'
    }
    return answer.join('')
}