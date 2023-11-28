const { removeElement } = require("./27.RemoveElement");

describe("Leetcode 27. Remove Element", () => {
  it("should return [2,2,_,_] given the input nums=[3,2,2,3], val = 3", () => {
    expect(removeElement([3, 2, 2, 3], 3)).toBe([2, 2]);
  });

  it("should return [0,1,4,0,3,_,_,_] given the input nums=[0,1,2,2,3,0,4,2], val = 2", () => {
    expect(removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2)).toBe([
      0,
      1,
      4,
      0,
      3,
      _,
      _,
      _,
    ]);
  });
});
