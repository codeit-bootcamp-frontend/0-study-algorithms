function solution(s) {
  let stack = [];
  for (let x of s) {
    if (!isNaN(x)) stack.push(+x);
    else {
      let rt = stack.pop();
      let lt = stack.pop();
      if (x === '+') stack.push(lt + rt);
      else if (x === '-') stack.push(lt - rt);
      else if (x === '*') stack.push(lt * rt);
      else if (x === '/') stack.push(lt / rt);
    }
  }
  return stack.pop();
}

let str = '352+*9-';
console.log(solution(str));
