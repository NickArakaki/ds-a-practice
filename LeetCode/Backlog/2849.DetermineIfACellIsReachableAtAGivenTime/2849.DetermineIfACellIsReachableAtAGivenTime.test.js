const {
  isReachableAtTime,
} = require("./2849.DetermineIfACellIsReachableAtAGivenTime");

describe("Leet Code 2894. Cell Reachable At A Given Time", () => {
  it("should return true with the input: sx = 2, sy = 4, fx = 7, fy = 7, t = 6", () => {
    expect(isReachableAtTime(2, 4, 7, 7, 6)).toBe(true);
  });

  it("should return false with the input: sx = 3, sy = 1, fx = 7, fy = 3, t = 3", () => {
    expect(isReachableAtTime(3, 1, 7, 3, 3)).toBe(false);
  });

  it("should return true with the input: sx = 1, sy = 1, fx = 2, fy = 2, t = 1", () => {
    expect(isReachableAtTime(1, 1, 2, 2, 1)).toBe(true);
  });
});
