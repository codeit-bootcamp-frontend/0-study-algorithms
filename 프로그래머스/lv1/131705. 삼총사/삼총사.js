function solution(number) {
    var answer = 0;
    for(let i = 0; i < number.length - 2; i++) {
        for(let j = i+1; j < number.length - 1; j++) {
            for(let k = j+1; k < number.length; k++) {
                if (i !== j && i !== k && number[i] + number[j] + number[k] === 0) {
                    answer++
                    console.log(number[i], number[j], number[k])
                }
                
            }
        }
    }
    return answer;
}