/**
 * Given an integer n, return a counter function. This counter function initially returns n and then returns
 * 1 more than the previous value every subsequent time it is called (n, n + 1, n + 2, etc).
 */

const createCounter = (n) => {
  return () => {
    n++;
    return n - 1;
  };
};

const counter = createCounter(-2);
console.log(counter() == -2);
console.log(counter() == -1);
console.log(counter() == 0);
console.log(counter() == 1);
