const { sortVowels } = require("./2785.SortVowelsInAString");

describe("sort vowels", () => {
  it("should return 'lEOtcede'", () => {
    expect(sortVowels("lEetCOde")).toEqual("lEOtcede");
  });

  it("should return 'lYmpH'", () => {
    expect(sortVowels("lYmpH")).toEqual("lYmpH");
  });
});
