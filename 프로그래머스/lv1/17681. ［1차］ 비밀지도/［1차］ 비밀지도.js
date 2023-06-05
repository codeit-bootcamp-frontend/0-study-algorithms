const Binary = (n, k) => {
    // 2진수로 나타내기
    let answer = ''
    function DFS() {
        if(n === 0) return
        answer += n % 2 
        n = parseInt(n / 2)
        DFS()
        
    }
    DFS()
    // ?0011
    let temp = answer.split('').reverse()
    let length = temp.length
    while(k !== temp.length) {
        length++
        temp.unshift(0)
    }
    let realAnswer = temp.map(item => item === '1' ? '#' : ' ')
    return realAnswer.join('')
}

function solution(n, arr1, arr2) {
    var answer = [];
    // 배열 순회하며 두 배열을 # 형태로 만들어야됨
    // 두 배열 순회 1. 둘 다 공백일 경우 => 공백, 1개 이상일 때 # => #
    const newArr1 = arr1.map(item => Binary(item, n))
    const newArr2 = arr2.map(item => Binary(item, n))
    
    for(let i = 0; i < n; i++) {
        let temp = ''
        for(let j = 0; j < n; j++) {
            if(newArr1[i][j] === ' ' && newArr2[i][j] === ' ') {
               temp += ' '
            } else {
                temp += '#'
            }
        }
        answer.push(temp)
    }
    
    return answer;
}