function solution(s, n) {
    if(n >= 26) return 
    var answer = '';
    for(let x of s) {
        if(x === ' ') {
            answer += ' '
            continue;
        }
        let num = x.charCodeAt();
        let plus = num + n
        if(num >= 65 && num <= 90) {
            if(plus > 90) {
                plus -= 26
            }
        } else if (num >= 97 && num <= 122) {
            if(plus > 122) {
                plus -= 26
            }
        }
        
        answer += String.fromCharCode(plus)
    }
    return answer;
}