const { compress } = require("./443.StringCompression");

describe("Leetcode 443 String Compression", () => {
  it("should return 6, and the input array should be modified to be ['a','2','b','2','c','3']", () => {
    const chars = ["a", "a", "b", "b", "c", "c", "c"];
    const length = chars.length;
    const k = compress(chars);
    expect(k).toBe(6);
    expect(chars.length).toBe(length);
    expect(chars.slice(0, k)).toEqual(["a", "2", "b", "2", "c", "3"]);
  });

  it("should return 1, and the input array should be modified to be ['a']", () => {
    const chars = ["a"];
    const length = chars.length;
    const k = compress(chars);
    expect(k).toBe(1);
    expect(chars.length).toBe(length);
    expect(chars.slice(0, k)).toEqual(["a"]);
  });

  it("should return 4, and the input array should be modified to be ['a','b','1','2']", () => {
    const chars = [
      "a",
      "b",
      "b",
      "b",
      "b",
      "b",
      "b",
      "b",
      "b",
      "b",
      "b",
      "b",
      "b",
    ];
    const length = chars.length;
    const k = compress(chars);
    expect(k).toBe(4);
    expect(chars.length).toBe(length);
    expect(chars.slice(0, k)).toEqual(["a", "b", "1", "2"]);
  });
});
