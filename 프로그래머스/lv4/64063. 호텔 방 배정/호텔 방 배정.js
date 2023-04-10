function findEmpty(number, rooms){
    if(!rooms.has(number)){
        rooms.set(number, number + 1)
        return number 
    }
    
    let next = findEmpty(rooms.get(number), rooms)
    rooms.set(number, next + 1)
    return next 
}

function solution(k, room_number) {
    var answer = [];
    const rooms = new Map() 
    
    room_number.forEach((rn) => {
        answer.push(findEmpty(rn, rooms))
    })
    
    return answer;
}