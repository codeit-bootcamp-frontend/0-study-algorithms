function solution(numbers) {
    const set = new Set();
    for(let i = 0; i < numbers.length; i++) {
        for(let j = 0; i !== j && j < numbers.length; j++) {
            set.add(numbers[i] + numbers[j])
        }
    }
    
    return Array.from(set).sort((a, b) => a - b)
}