function solution(t, p) {
    let answer = 0
    let temp = ''
    for(let i = 0; i < p.length; i++) {
            temp += t[i]
    }
    
    for(let i = p.length; i < t.length + 1; i++) {
        if(+temp <= +p) answer++
        temp = String(temp).split('')
        temp.shift();
        temp.push(t[i])
        temp = temp.join('')
        
    }
    
    return answer;
}