const { findDifferentBinString } = require("./1980.FindUniqueBinString");

describe("Find Unique Binary String", () => {
  it("should return '11' or '00' given the input ['01', '10']", () => {
    expect(["11", "00"]).toContain(findDifferentBinString(["01", "10"]));
  });

  it("should return '11', '10' given the input ['00', '01']", () => {
    expect(["11", "10"]).toContain(findDifferentBinString(["00", "01"]));
  });

  it("should return '101', '000', '010', '100', or '110' given the input ['111', '011', '001']", () => {
    expect(["101", "000", "010", "100", "110"]).toContain(
      findDifferentBinString(["111", "011", "001"])
    );
  });
});
