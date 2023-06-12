class Node {
  constructor(value = "", count = 0) {
    this.value = value;
    this.count = count;
    this.child = {};
    this.end = false;
  }
}
class Trie {
  constructor() {
    this.root = new Node();
  }
  insert(string) {
    let currNode = this.root;
    currNode.count++;

    for (let i = 0; i < string.length; i++) {
      let currChar = string[i];
      if (currNode.child[currChar] === undefined) {
        currNode.child[currChar] = new Node(currNode.value + currChar, 0);
      }
      currNode = currNode.child[currChar];
      currNode.count++;
    }
    currNode.end = true;
  }
  search(string) {
    let currNode = this.root;
    for (let i = 0; i < string.length; i++) {
      let currChar = string[i];
      if (currNode.child[currChar]) {
        currNode = currNode.child[currChar];
      } else return 0;
    }
    return currNode.count;
  }
}

function solution(words, queries) {
  var ans = [];
  var arr = Array.from({ length: 100001 }, () => 0);

  for (var i = 1; i <= 100001; i++) {
    arr[i] = [new Trie(), new Trie()];
  }

  for (var i = 0; i < words.length; i++) {
    var w = words[i];
    var wl = words[i].length;
    arr[wl][0].insert(w);
    arr[wl][1].insert(w.split("").reverse().join(""));
  }

  for (var i = 0; i < queries.length; i++) {
    var ql = queries[i].length;
    var trimmedStr = queries[i].split("?").join("");
    // 1. "?"가 뒤에 있는 경우
    if (trimmedStr.length === 0 || queries[i][0] !== "?") {
      var res = arr[ql][0].search(trimmedStr);
      ans.push(res);
    } else {
      // 2. "?"가 앞에 있는 경우
      var res = arr[ql][1].search([...trimmedStr].reverse().join(""));
      ans.push(res);
    }
  }
  return ans;
}