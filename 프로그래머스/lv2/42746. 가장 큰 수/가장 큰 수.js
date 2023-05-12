function solution(numbers) {
    var answer = '';
    
    set_numbers = new Set(numbers);
    // if (set_numbers.values())
    if (set_numbers.has(0) && set_numbers.size === 1) return '0';
    
    numbers = numbers.map(String);
    numbers.sort((a, b) => Number(b+a) - Number(a+b));
    
    console.log(numbers)
    
    for (let i of numbers) {
        answer += i
    }
    
    return answer;
}