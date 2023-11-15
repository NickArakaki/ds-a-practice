const {
  maxElementAfterDecrementAndRearrange,
} = require("./1846.MaxElAfterDecreasingAndRearranging");

describe("Maximum Element After Decreasing and Rearranging", () => {
  it("should return 2 given the input [2,2,1,2,1]", () => {
    expect(maxElementAfterDecrementAndRearrange([2, 2, 1, 2, 1])).toEqual(2);
  });

  it("should return 3 given the input [100,1,100]", () => {
    expect(maxElementAfterDecrementAndRearrange([100, 1, 100])).toEqual(3);
  });

  it("should return 5 given the input [1,2,3,4,5]", () => {
    expect(maxElementAfterDecrementAndRearrange([2, 2, 1, 2, 1])).toEqual(5);
  });
});
