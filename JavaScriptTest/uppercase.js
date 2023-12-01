arr = ["jason", "justin", "dan"];
function changeArray(a) {
  // Write a function that updates elements of an array in 2 ways. 1) Return all characters UPPERCAASE and Sort them
  // Example: changeArray(['jason', 'justin', 'dan']) returns 'DAN', JASON', 'JUSTIN'
  a.forEach((el, i) => {
    a[i] = el.toUpperCase();
  });
  a.sort();
  return a;
}
console.log(changeArray(arr));
