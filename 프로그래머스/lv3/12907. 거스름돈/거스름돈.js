function solution (n, money){
    let arr = new Array(n+1).fill(0);
    
    arr[0] = 1;
    
    for(let el of money){
    	for(let i=el; i<n+1; i++){
        	arr[i] = arr[i] + arr[i - el];
        }
    }
    
    return arr[n];
}