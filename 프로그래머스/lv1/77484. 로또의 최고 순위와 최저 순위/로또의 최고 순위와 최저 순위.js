function solution(lottos, win_nums) {
    var answer = [];
    // 최저등수
    let min = 0
    // 민우의 복권 중 숫자가 0인 갯수
    let zero = 0;
    lottos.sort((a, b) => a - b)
    win_nums.sort((a, b) => a - b)
    for (let i = 0; i < lottos.length; i++) {
            if(lottos[i] === 0) zero++ // 민우의 복권 중 숫자가 0인 갯수 카운드
            if(lottos.includes(win_nums[i])) min++
    }
    // min === 5 이거나 6일 때 최저 순위는 6
    // 겹치는 것이 3개면 4등
    // 겹치는 것이 4개면 3등
    let score = 6 - min + 1
    if (min === 0 || min === 1) answer.push(6)
    else answer.push(score)
    answer.push(score - zero)
    answer.reverse()
    if(answer[0] === 7) answer[0] = 6
    return answer
}