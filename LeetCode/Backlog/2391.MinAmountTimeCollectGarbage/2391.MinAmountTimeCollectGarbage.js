/*
    You are given a 0-indexed array of strings garbage where garbage[i] represents the assortment
    of garbage at the ith house. garbage[i] consists only of the characters 'M', 'P' and 'G'
    representing one unit of metal, paper and glass garbage respectively. Picking up one
    unit of any type of garbage takes 1 minute.

    You are also given a 0-indexed integer array travel where travel[i] is the number of minutes
    needed to go from house i to house i + 1.

    There are three garbage trucks in the city, each responsible for picking up one type of garbage.
    Each garbage truck starts at house 0 and must visit each house in order; however, they do
    not need to visit every house.

    Only one garbage truck may be used at any given moment. While one truck is driving or picking up
    garbage, the other two trucks cannot do anything.

    Return the minimum number of minutes needed to pick up all the garbage.
*/

// const garbageCollection = (garbage, travel) => {
//   travel.push(0);
//   // track total time
//   let totalTime = 0;
//   // track the total time travelling
//   let travelTime = 0;
//   // iterate over houses (garbage)
//   for (let i = 0; i < garbage.length; i++) {
//     // count the occurances of each type of trash at each house
//     // const house = garbage[i];
//     // const garbageCount = {};
//     // for (let char of house) {
//     //   if (!(char in garbageCount)) {
//     //     garbageCount[char] = 1;
//     //   } else {
//     //     garbageCount[char]++;
//     //   }
//     // }

//     // for (let time of Object.values(garbageCount)) {
//     //   totalTime += time;
//     // }
//     totalTime += garbage[i].length;

//     travelTime += travel[i];
//   }

//   const finalSet = new Set();
//   for (let i = garbage.length - 1; i >= 0; i--) {
//     for (const char of garbage[i]) {
//       finalSet.add(char);
//     }
//     console.log(finalSet.size);
//   }
//   // return total time
//   return totalTime;
// };

const garbageCollection = (garbage, travel) => {
  travel.push(0);

  const truckTimes = {};
  let travelTime = 0;
  let collectionTime = 0;
  for (let i = 0; i < garbage.length; i++) {
    const house = garbage[i];
    collectionTime += house.length;
    for (const type of house) {
      truckTimes[type] = travelTime;
    }

    travelTime += travel[i];
  }

  return (
    Object.values(truckTimes).reduce((acc, cur) => acc + cur, 0) +
    collectionTime
  );
};

module.exports.garbageCollection = garbageCollection;
