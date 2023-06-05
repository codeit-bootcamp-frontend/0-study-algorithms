function solution(numbers) {
    const arr = Array.from({length: 10}, (v, i) => i)
    const set = new Set(arr)
    for(let i = 0; i < numbers.length; i++) {
        set.delete(numbers[i])
    }
    
    const newArray = Array.from(set)
    return newArray.reduce((a, b) => a + b, 0)
   
}