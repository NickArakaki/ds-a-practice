dt = "2022-05-24";
function dayOfYear(dt) {
  // Write a function that takes a date string (ISO Format YYYY-MM-DD) as argument. (example: '2019-01-31')
  // return the nth day of the year
  // Example 1: dayOfYear( '2019-09-01' ) returns 244
  // Example 2: dayOfYear( '2022-01-31' ) returns 31
  // Example 3: dayOfYear( '2022-12-31' ) returns 365
  const date = new Date(dt);
  // get number difference between jan 1st of the date year and the current date in ms
  //ear, monthIndex, day, hours, minutes, seconds, milliseconds
  const newYear = new Date(`${date.getUTCFullYear()}-01-01`);
  const ms = date - newYear;
  const oneDay = 1000 * 60 * 60 * 24;

  return Math.floor(ms / oneDay) + 1;
  // calculate the number of days from diff in ms
  // return number of day
}
console.log(dayOfYear(dt));
console.log(dayOfYear("2022-12-31") === 365);
console.log(dayOfYear("2022-01-31") === 31);
console.log(dayOfYear("2022-01-01") === 1);
console.log(dayOfYear("2019-09-01") === 244);
