function solution(price, money, count) {
    const fixNum = price
    let temp = 0;
    for (let i = 0; i < count; i++) {
        temp += price
        price += fixNum
    }

    return temp - money >= 0 ? temp - money : 0
}