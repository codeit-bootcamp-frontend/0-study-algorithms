function solution(str1, str2) {
  if (str1.length !== str2.length) return false;
  let aMap = new Map();
  let bMap = new Map();

  for (let i = 0; i < str1.length; i++) {
    if (!aMap.has(str1[i])) aMap.set(str1[i], 1);
    else aMap.set(str1[i], aMap.get(str1[i]) + 1);
    if (!bMap.has(str2[i])) bMap.set(str2[i], 1);
    else bMap.set(str2[i], bMap.get(str2[i]) + 1);
  }

  for (let [key, value] of aMap) {
    if (bMap.get(key) !== value) return false;
  }

  return true;
}

let a = 'AbaACe';
let b = 'baeeCA';
console.log(solution(a, b));

function solution(str1, str2) {
  let sh = new Map();
  for (let x of str1) {
    if (sh.has(x)) sh.set(x, sh.get(x) + 1);
    else sh.set(x, 1);
  }
  for (let x of str2) {
    if (!sh.has(x) || sh.get(x) === 0) return false;
    sh.set(x, sh.get(x) - 1);
  }
  return true;
}

let a = 'AbaACee';
let b = 'baeAeCA';
console.log(solution(a, b));
