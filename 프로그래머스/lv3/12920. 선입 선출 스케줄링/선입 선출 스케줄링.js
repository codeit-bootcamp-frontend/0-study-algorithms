function solution(n, cores) {
  let l = cores.length;
  let rest = n - l;

  let min = 1,
    max = (Math.max(...cores) * rest) / l;

  while (min < max) {
    const mid = ((min + max) / 2) >> 0;
    let capacity = 0;

    for (const c of cores) capacity += (mid / c) >> 0;
    if (capacity >= rest) max = mid;
    else min = mid + 1;
  }

  for (const c of cores) {
    rest -= ((max - 1) / c) >> 0;
  }

  for (let i = 0; i < l; i++) {
    if (max % cores[i] === 0) {
      rest -= 1;
      if (!rest) return i + 1;
    }
  }
}