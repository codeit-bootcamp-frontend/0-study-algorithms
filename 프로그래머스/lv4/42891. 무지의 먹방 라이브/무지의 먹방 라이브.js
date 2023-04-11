function solution(food_times, k) {
  const len = food_times.length;

  let foods = food_times
    .map((time, index) => {
      return { index: index + 1, time };
    })
    .sort((a, b) => a.time - b.time);

  let previous = 0;
  for (let i = 0; i < len; i++) {
    const currentTime = foods[i].time;
    const remainFoodsLen = len - i;
    const eatTime = (currentTime - previous) * remainFoodsLen;
    previous = currentTime;

    if (k < eatTime) {
      foods = foods.slice(i).sort((a, b) => a.index - b.index);
      return foods[k % remainFoodsLen].index;
    }
    k -= eatTime;
  }

  return -1;
}