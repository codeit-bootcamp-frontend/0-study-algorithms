function solution(s) {
    const answer = []
    const map = new Map()
    for(let i = 0; i < s.length; i++) {
        if(!map.has(s[i])) {
            map.set(s[i], i)
            answer.push(-1)
        } else {
            answer.push(i - map.get(s[i]))
            map.set(s[i], i)
        }
    }
    
    return answer;
}