function solution(food) {
    var answer = [];
    for(let i = 1; i < food.length; i++) {
        for (let j = 0; j < parseInt(food[i] / 2); j++) {
            answer.push(i)    
      }
   }
    const temp = [...answer]
    temp.reverse()
    console.log(temp)
    answer.push(0)
    answer = [...answer, ...temp]
    console.log(answer)
    
    
    return answer.join('')
}