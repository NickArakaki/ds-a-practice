const { eliminateMaximum } = require("./1921.EliminateMaximumNumMonster");

describe("Eliminate Max Number of Monsters", () => {
  it("should return 3", () => {
    expect(eliminateMaximum([1, 3, 4], [1, 1, 1])).toBe(3);
  });

  it("should return 1", () => {
    expect(eliminateMaximum([1, 1, 2, 3], [1, 1, 1, 1])).toBe(1);
  });

  it("should retrun 1", () => {
    expect(eliminateMaximum([3, 2, 4], [5, 3, 2])).toBe(1);
  });

  it("should return 3", () => {
    expect(eliminateMaximum([4, 2, 3], [2, 1, 1])).toBe(3);
  });
});
