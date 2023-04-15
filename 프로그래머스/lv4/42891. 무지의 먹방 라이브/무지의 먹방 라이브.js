function solution(food_times, k) {
    let count=0;
    let queue=food_times.map((a,b)=>[a,b]).sort((a,b)=>a[0]-b[0]);
    const total = food_times.reduce((a,b)=>{return a+b},0);
    if(total<=k) return -1;
    
    let idx=0;
    while(queue.length-idx){
        let sum=queue[idx][0]-count;
        if(k-(queue.length-idx)<0) break;
        while(k-(queue.length-idx)*sum<0)
            sum--;
        
        k-=(queue.length-idx)*sum;
        count+=sum;
        while(true){
            if(queue[idx][0]-count===0){
                queue[idx][0]=0;
                idx++;
            }else{
                break;
            }
        } 
    }
    queue=queue.filter((a,b)=>a[0]>0).sort((a,b)=>a[1]-b[1]);
    return queue[k][1]+1;
}