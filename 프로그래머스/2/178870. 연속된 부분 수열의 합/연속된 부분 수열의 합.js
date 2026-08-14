function solution(sequence, k) {
  const result = [];
  let startIdx = 0;
  let endIdx = 0;
  let currSum = sequence[startIdx];

  while (endIdx < sequence.length) {
    if (currSum < k) {
      endIdx++;
      currSum += sequence[endIdx];
    } else if (currSum === k) {
      result.push([startIdx, endIdx]);
      currSum -= sequence[startIdx];
      startIdx++;
      endIdx++;
      currSum += sequence[endIdx];
    } else {
      currSum -= sequence[startIdx];
      startIdx++;
    }
  }

  let shortestLength = Infinity;
  let shortestSubsequence = null;

  for (const subsequence of result) {
    const length = subsequence[1] - subsequence[0] + 1;
    if (length < shortestLength) {
      shortestLength = length;
      shortestSubsequence = subsequence;
    }
  }

  return shortestSubsequence;
}