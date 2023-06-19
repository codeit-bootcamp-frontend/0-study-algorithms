function solution(s){
    if(s[0] === ')') return false
    let stack = []
    for(let x of s) {
        if (x === '(') stack.push(')')
        else stack.pop()
    }
   
    return stack.length === 0 ? true : false
}