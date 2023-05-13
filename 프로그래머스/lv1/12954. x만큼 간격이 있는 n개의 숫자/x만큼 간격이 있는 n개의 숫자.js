function solution(x, n) {
   const answer = []
   let count = 0
   let temp = x
   function DFS() {
       if(count === n) return 
       else {
           answer.push(temp)
       }
       temp += x
       count++
       DFS()
   }
    DFS()
    return answer
}