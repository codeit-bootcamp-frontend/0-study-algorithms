const solution = (matrix_sizes) => {
    
    const len = matrix_sizes.length 
    const dp = new Array(len).fill(null).map(() => new Array(len).fill(Infinity))
    
    for(let i=0; i<len; i++) dp[i][i] = 0
    
    for(let i=1; i<len; i++){
        for(let s=0; s<len; s++){
            const e = s + i
            
            if(e >= len) break 
            
            for(let f=s; f<e; f++){
                dp[s][e] = Math.min(
                    dp[s][e], dp[s][f] + dp[f + 1][e] + matrix_sizes[s][0] * matrix_sizes[f + 1][0] * matrix_sizes[e][1]
                )
            }
            
        }
    }
    
    return dp[0][len - 1]
}