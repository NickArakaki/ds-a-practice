const { hammingWeight } = require("./191.NumberOf1Bits");

describe("Leetcode 191. Number of 1 Bits", () => {
  it("should return 3 given the input 00000000000000000000000000001011", () => {
    const bin = Number();
    expect(hammingWeight(0b00000000000000000000000000001011)).toBe(3);
  });

  it("should return 1 given the input 00000000000000000000000010000000", () => {
    expect(hammingWeight(0b00000000000000000000000010000000)).toBe(1);
  });

  it("should return 31 given the input 11111111111111111111111111111101", () => {
    expect(hammingWeight(0b11111111111111111111111111111101)).toBe(31);
  });
});
