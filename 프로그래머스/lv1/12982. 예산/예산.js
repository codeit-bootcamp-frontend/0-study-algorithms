function solution(d, budget) {
    let answer = 0;
    d.sort((a, b) => a - b)
    for(let x of d) {
        if (budget >= x) {
            budget -= x
            answer++
        }
        else break
    }
    return answer;
}