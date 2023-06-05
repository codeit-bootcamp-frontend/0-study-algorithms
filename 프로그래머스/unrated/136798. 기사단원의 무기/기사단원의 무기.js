function solution(number, limit, power) {
    var answer = 0;
    let counter = 0; // 약수 카운터
    
    for(let i=1; i<=number; i++){
        counter = 0;
        
        for( let k=1; k<=i/2; k++){
            if(i%k === 0){
                counter+=1;
            }
        }
        counter +=1;
        
        if(counter > limit){
            answer +=  power;
        }else{
            answer += counter;
        } 
    }
    return answer;
}