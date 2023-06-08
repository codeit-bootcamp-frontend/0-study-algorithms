function solution(k, m, score) {
    let nestedArr = []
    // k점 최상급 사과, 1점 최하품의 사과
    // 한 상자에 m개씩 포장
    // 사과 한 상자의 가격 m * 가장 낮은 점수 p <- p를 찾아야됨
    let answer = 0;
    score.sort((a, b) => a - b)
    let length = score.length
    for (let i = 0; i < length / m; i++) {
        const newArr = score.splice(-m)
        if(newArr.length === m) {
            let min = newArr[0]
            answer += min * m
        }
    }
    return answer
}