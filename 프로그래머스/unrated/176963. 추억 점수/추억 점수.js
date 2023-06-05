function solution(name, yearning, photo) {
    // 1. name과 yearning를 key - value 형태로 객체 생성
    // 중첩 배열을 돌며 해당 배열의 숫자합 구하기
    let map = new Map()
    let answer = []
    for(let i = 0; i < name.length; i++) {
        map.set(name[i], yearning[i])
    }
    console.log(map)
    for(let i = 0; i < photo.length; i++) {
        let temp = 0
        for(let j = 0; j < photo[i].length; j++) {
            if (map.has(photo[i][j])) {
                temp += map.get(photo[i][j]) 
            } else {
                temp += 0
            }
        }
        answer.push(temp)
    }
    return answer
}