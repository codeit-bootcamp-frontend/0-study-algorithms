function solution(s) {
    const eng = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    const newArr = s.split(/(\d)/)
    for (let i = 0; i < newArr.length; i++) {
        if (newArr[i] === '') newArr.splice(i, 1)
    }
    let answer = ''
    
    // 영어를 숫자로 변환
    for (let i = 0; i < newArr.length; i++) {
        if (!Number.isInteger(+newArr[i])) {
            let temp = ''
            for (let j = 0; j < newArr[i].length; j++) {
                temp += newArr[i][j]
                let is = eng.findIndex(item => item === temp)
                if (is >= 0) {
                    console.log(is)
                    answer += Number(is)
                    temp = ''
                }
            }
        } else {
            answer += newArr[i]
        }
    }
    // 붙어있는 단어 분리
    console.log(answer)
    return +answer
}