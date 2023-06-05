function solution(n, m) {
    const answer = []
    let greatestCommonDivisor = 1
    for(let i = 2; i <= Math.max(n, m); i++) {
        if(m % i === 0 && n % i === 0) greatestCommonDivisor = i
    }
    answer.push(greatestCommonDivisor)
    if(answer[0] === 1) {
        answer.push(m * n)
    } else {
        answer.push(greatestCommonDivisor * (m / greatestCommonDivisor) * (n /greatestCommonDivisor))
    }
    
    return answer
}