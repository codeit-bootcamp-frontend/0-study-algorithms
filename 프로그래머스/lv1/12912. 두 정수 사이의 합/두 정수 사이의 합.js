function solution(a, b) {
    const length = Math.abs(b - a) + 1
    if(a === b) return a
    else return (a + b) / 2  * length
}