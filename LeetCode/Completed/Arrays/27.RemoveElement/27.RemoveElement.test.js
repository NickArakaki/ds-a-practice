const { removeElement } = require("./27.RemoveElement");

describe("Leetcode 27. Remove Element", () => {
  it("should return [2,2,_,_] given the input nums=[3,2,2,3], val = 3", () => {
    const arr = [3, 2, 2, 3];
    const k = removeElement(arr, 3);
    expect(k).toBe(2);
    expect(arr.slice(0, k)).toEqual([2, 2]);
  });

  it("should return [0, 1, 3, 0, 4, _, _, _] given the input nums=[0,1,2,2,3,0,4,2], val = 2", () => {
    const arr = [0, 1, 2, 2, 3, 0, 4, 2];
    const k = removeElement(arr, 2);
    expect(k).toBe(5);
    expect(arr.slice(0, k)).toEqual([0, 1, 3, 0, 4]);
  });
});
