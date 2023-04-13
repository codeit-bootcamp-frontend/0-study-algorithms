function solution(s) {
    return s.length % 2 ? s.substr(parseInt(s.length / 2), 1) : s.substr(parseInt(s.length / 2) - 1, 2)
}