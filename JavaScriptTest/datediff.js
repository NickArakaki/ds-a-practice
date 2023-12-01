start = "2021-08-10T15:14:00";
finish = "2021-08-10T15:16:00";
function timeDiff(a, b) {
  // Write a function that takes two Date/TIME strings in ISO Format as argument
  // It should return the hours:minutes:seconds between the two
  const dateA = new Date(a);
  const dateB = new Date(b);
  const diff = dateB - dateA;
  const hours = Math.floor(diff / (1000 * 60 * 60));
  const min = Math.floor((diff % (1000 * 60 * 60)) / (1000 * 60));
  const s = Math.floor((diff % (1000 * 60)) / (1000 * 60));
  console.log(`${hours}:${min}:${s}`);
  return diff;
  // Expect that either the start or end time can come first.
  // Example: timeDiff( '2023-08-10T15:14:00', '2023-08-10T15:16:00' ) returns 00:02:00
  a = "2021-08-10T15:14:00";
  b = "2021-08-10T15:16:00";
  return "calculation";
}
timeDiff(start, finish);
