function solution(sequence) {
  var answer = 0;

  const pseq = [];
  const mseq = [];

  sequence.map((seq, idx) => {
    if (idx === 0) {
      pseq.push(seq);
      mseq.push(-seq);
    } else if (idx % 2 === 0) {
      pseq.push(Math.max(pseq[idx - 1] + seq, seq));
      mseq.push(Math.max(mseq[idx - 1] - seq, -seq));
    } else {
      pseq.push(Math.max(pseq[idx - 1] - seq, -seq));
      mseq.push(Math.max(mseq[idx - 1] + seq, seq));
    }

    answer = Math.max(answer, pseq[idx], mseq[idx]);
  });

  return answer;
}