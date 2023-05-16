function solution(arr) {
    let min = Number.MAX_SAFE_INTEGER;
    let index = 0
    for(let i = 0; i < arr.length; i++) {
        if(arr[i] < min) {
            min = arr[i]
            index = i
        }
    }
    let answer = arr.splice(index, 1)
    return arr.length ? arr : [-1]
}