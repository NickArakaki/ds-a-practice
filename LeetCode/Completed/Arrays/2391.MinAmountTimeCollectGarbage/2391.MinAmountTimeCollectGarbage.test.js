const { garbageCollection } = require("./2391.MinAmountTimeCollectGarbage");

describe("Minimum Amount of Time to Collect Garbage", () => {
  it('should return 21 given the input: garbage = ["G","P","GP","GG"], travel = [2,4,3]', () => {
    expect(
      garbageCollection(
        (garbage = ["G", "P", "GP", "GG"]),
        (travel = [2, 4, 3])
      )
    ).toEqual(21);
  });

  it('should return 37 given the input: garbage = ["MMM","PGM","GP"], travel = [3,10]]', () => {
    expect(
      garbageCollection((garbage = ["MMM", "PGM", "GP"]), (travel = [3, 10]))
    ).toEqual(37);
  });
});
