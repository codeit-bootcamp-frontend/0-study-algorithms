function solution(strs, t) {
    const l = t.length 
    const dp = new Array(l).fill(Infinity)
    
    for(let i=0; i<l; i++){
        const current = t.substr(0, i+1)
        
        for(const str of strs){
            if(current.endsWith(str)){
                const diff = current.length - str.length 
                
                if(diff === 0) dp[i] = 1
                else {
                    dp[i] = Math.min(dp[i], dp[diff - 1] + 1)
                }
            }
        }
    }
    
    return dp[l - 1] === Infinity ? -1 : dp[l - 1]
}