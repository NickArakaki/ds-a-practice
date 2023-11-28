const {
  reductionOperations,
} = require("./1887.ReductionOperationsMakeArrayElEqual");

describe("Leetcode 1887, Reduction Operations to Make Array Elements Equal", () => {
  it("should return 3 given the input [5,1,3]", () => {
    expect(reductionOperations([5, 1, 3])).toBe(3);
  });

  it("should return 0 given the input [1,1,1]", () => {
    expect(reductionOperations([1, 1, 1])).toBe(0);
  });

  it("should return 4 given the input [1,1,2,2,3]", () => {
    expect(reductionOperations([1, 1, 2, 2, 3])).toBe(4);
  });
});
