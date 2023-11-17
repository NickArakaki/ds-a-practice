const { minPairSum } = require("./1877.MinimizeMaximumPairSumInArray");

describe("Minimize Maximum Pair Sum In Array", () => {
  it("should return 7 given the input [3,5,2,3]", () => {
    expect(minPairSum([3, 5, 2, 3])).toEqual(7);
  });

  it("should return 8 given the input [3,5,4,2,4,6]", () => {
    expect(minPairSum([3, 5, 4, 2, 4, 6])).toEqual(8);
  });
});
