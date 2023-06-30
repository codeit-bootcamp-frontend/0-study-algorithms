function solution(edges, target) {
  // [{ pk: index, children: [], next: 0 }, ...]
  const nodes = Array.from(
    new Array(edges.length + 1),
    (_, index) => new Object({ pk: index, children: [], next: 0 })
  );
  edges.forEach(([parent, child]) => {
    const { children } = nodes[parent - 1];
    children.push(child - 1);
  });
  nodes.forEach(({ children }) => children.sort((a, b) => a - b));

  const findNext = (id) => {
    const { children, next, pk } = nodes[id];
    if (!children.length) return pk; // leaf
    const result = findNext(children[next]);
    nodes[id].next = (next + 1) % children.length;
    return result;
  };
  
  const getNext = () => findNext(0);

  const sum = new Array(target.length).fill(0);
  const order = [];

  while (!sum.every((num, i) => num <= target[i] && target[i] <= num * 3)) {
    const index = getNext();
    sum[index] += 1;
    order.push(index);
    if (sum[index] > target[index]) return [-1];
  }

  const nowTarget = sum.map((item, index) => target[index] - item);
  const answer = new Array(order.length).fill(1);
  for (let i = order.length - 1; i >= 0; i--) {
    const index = order[i];
    if (nowTarget[index] >= 2) {
      answer[i] += 2;
      nowTarget[index] -= 2;
    } else if (nowTarget[index] === 1) {
      answer[i] += 1;
      nowTarget[index] -= 1;
    }
  }
  return answer;
}