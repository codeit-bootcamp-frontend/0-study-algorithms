function solution(s) {
    var answer = '';
    
    let arr = s.split(" ")
    for (let x of arr) {
        // 숫자라면
        for(let i = 0; i < x.length; i++) {
            if(typeof x[i] === 'number') answer += x[i]
            if(x[i] === ' ') answer += " "
            else if(i === 0) answer += x[i].toUpperCase()
            else answer += x[i].toLowerCase();
        }
        answer += ' '
        
    }
    const newArr = answer.split('')
        newArr.pop()
        let na = newArr.join('')
    return na
}