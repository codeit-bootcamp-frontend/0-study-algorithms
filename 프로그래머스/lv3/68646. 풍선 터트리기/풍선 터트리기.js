function solution(a) {
  var answer = 2;
  var al = a.length;

  var ldp = [...a];
  var rdp = [...a];

  for (let i = 1; i < al; i++) {
    if (ldp[i] > ldp[i - 1]) ldp[i] = ldp[i - 1];
  }
  for (let i = al - 2; i >= 0; i--) {
    if (rdp[i] > rdp[i + 1]) rdp[i] = rdp[i + 1];
  }

  for (let i = 1; i < al - 1; i++) {
    // console.log(a, a[i], ldp[i - 1], rdp[i + 1]);
    if (a[i] < ldp[i - 1] || a[i] < rdp[i + 1]) {
      answer++;
    }
  }

  return answer;
}