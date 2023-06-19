function solution(sales, links) {
  const tree = {};
  links.map(([leader, member]) =>
    tree[leader] ? tree[leader].push(member) : (tree[leader] = [member])
  );

  const costs = {};
  dfs_dp(tree, sales, costs, 1);

  return Math.min(...costs[1]);
}

const dfs_dp = (tree, sales, costs, index) => {
  costs[index] = [0, 0];

  const children = tree[index];
  children.map((child) => {
    !costs[child] && tree[child]
      ? dfs_dp(tree, sales, costs, child)
      : (costs[child] = [0, sales[child - 1]]);
  });

  let checkGroup = false;
  costs[index][0] = children.reduce((acc, child) => {
    if (costs[child][0] < costs[child][1]) {
      return acc + costs[child][0];
    } else {
      checkGroup = true;
      return acc + costs[child][1];
    }
  }, 0);

  costs[index][1] = costs[index][0] + sales[index - 1];

  if (!checkGroup) {
    let minOffset = Number.MAX_SAFE_INTEGER;
    children.map((child) => {
      const tempOffset = costs[child][1] - costs[child][0];
      if (tempOffset < minOffset) {
        minOffset = tempOffset;
      }
    });
    costs[index][0] += minOffset;
  }
};