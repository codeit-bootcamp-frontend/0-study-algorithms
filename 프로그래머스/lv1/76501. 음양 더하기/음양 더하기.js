function solution(absolutes, signs) {
    for(let i = 0; i < signs.length; i++) {
        if(signs[i]) {
            absolutes[i] = +absolutes[i]
        } else {
            absolutes[i] = -absolutes[i]
        }
    }
    return absolutes.reduce((a, b) => a + b)
}