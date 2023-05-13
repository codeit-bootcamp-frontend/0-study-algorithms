function solution(s){
    s = s.toLowerCase()
    let temp = 0;
    for(let x of s) {
     if(x === 'p') temp++
     if(x === 'y') temp--
    }
    

    // [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    console.log('Hello Javascript')

    return temp === 0 ? true : false
}