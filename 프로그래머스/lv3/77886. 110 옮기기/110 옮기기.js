const extract110 = (temp, str, stack) => {
  for (const third of str) {
    if (stack.length >= 2) {
      const second = stack.pop();
      const first = stack.pop();

      if (first === "1" && second === "1" && third === "0") {
        temp += "110";
        continue;
      }
      stack.push(first);
      stack.push(second);
    }
    stack.push(third);
  }
  const stackToStr = stack.join("");
  return [temp, stackToStr, stackToStr.lastIndexOf("0") + 1];
};

const solution = (s) => {
  return s.map((str) => {
    if (!str.includes("110")) return str;

    const [str110, strRest, lastZeroIndex] = extract110("", str, []);

    return (
      strRest.substring(0, lastZeroIndex) +
      str110 +
      strRest.substring(lastZeroIndex)
    );
  });
};