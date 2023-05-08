function solution(food) {
    var answer = [];
    for(let i = 1; i < food.length; i++) {
        for (let j = 0; j < parseInt(food[i] / 2); j++) {
            answer.push(i)    
      }
   }
    let temp = [...answer]
    for(let i = answer.length; i >= 0; i--) {
        answer.push(temp[i])
    }
    for (let i = 0; i < answer.length; i++) {
        if(!answer[i]) {
            answer[i] = 0
        }
    }
    
    
    return answer.join('')
}