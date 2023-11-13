const { sortVowels } = require("./2785.SortVowelsInAString");

describe("sort vowels", () => {
  it("should return 'lEOtcede'", () => {
    expect(sortVowels("lEetcOde")).toEqual("lEOtcede");
  });

  it("should return 'lYmpH'", () => {
    expect(sortVowels("lYmpH")).toEqual("lYmpH");
  });
});
