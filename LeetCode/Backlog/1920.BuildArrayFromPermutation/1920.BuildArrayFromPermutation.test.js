const { buildArray } = require("./1920.BuildArrayFromPermutation");

describe("Leetcode 1920. Build array from permutation", () => {
  it("should return [0, 1, 2, 3, 4, 5] given the input [0,2,1,5,3,4]", () => {
    expect(buildArray([0, 2, 1, 5, 3, 4])).toEqual([0, 1, 2, 3, 4, 5]);
  });

  it("should return [4,5,0,1,2,3] given the input [5,0,1,2,3,4]", () => {
    expect(buildArray([5, 0, 1, 2, 3, 4])).toEqual([4, 5, 0, 1, 2, 3]);
  });
});
