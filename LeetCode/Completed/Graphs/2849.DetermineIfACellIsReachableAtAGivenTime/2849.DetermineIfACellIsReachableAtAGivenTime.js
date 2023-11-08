/*
    You are given four integers sx, sy, fx, fy, and a non-negative integer t.

    In an infinite 2D grid, you start at the cell (sx, sy). Each second, you must move to any of its adjacent cells.

    Return true if you can reach cell (fx, fy) after exactly t seconds, or false otherwise.

    A cell's adjacent cells are the 8 cells around it that share at least one corner with it.
    You can visit the same cell several times.
*/

// const isReachableAtTime = (sx, sy, fx, fy, t) => {
//   /*
//         Plan: (Fails if start and end point are the same and time = 1)
//             Breadth First Search
//             If we can reach the end point before or at t iterations,
//             we know that the end point can be reached since we can visit the same cell multiple times

//             init a queue with array of the first coordinates and 0 (number of steps taken), might not work because arrays in js are mutable
//             init a visited set with start coords

//             while the queue is not empty
//                 pop the first el in the queue
//                 if num steps taken > t return false
//                 if the coords are equal to the end coords return true

//                 get all neighbors and add to queue and visited

//         Optimizations:
//             Use A* and use the euclidean distance as the heuristic, requires us to create a priority queue class
//     */

//   const queue = [[sx, sy, 0]];
//   const visited = new Set();
//   visited.add([sx, sy]);

//   const validNeighbors = [
//     [1, 0],
//     [-1, 0],
//     [0, 1],
//     [0, -1],
//     [1, 1],
//     [-1, 1],
//     [1, -1],
//     [-1, -1],
//   ];

//   while (queue.length) {
//     const [x, y, steps] = queue.shift();
//     if (steps > t) return false;
//     if (x === fx && y === fy) return true;

//     validNeighbors.forEach((neighbor) => {
//       const newX = x + neighbor[0];
//       const newY = y + neighbor[1];
//       if (!visited.has([newX, newY])) {
//         queue.push([newX, newY, steps + 1]);
//         visited.add([newX, newY]);
//       }
//     });
//   }

//   return false;
// };

const isReachableAtTime = (sx, sy, fx, fy, t) => {
  /*
        Plan:
            Edge case: if start coord === end coord and t === 1, automatic false

            If the distance between x positions and y positions is less than t we know that it's possible to reach that point
    */
  const xDist = Math.abs(fx - sx);
  const yDist = Math.abs(fy - sy);
  if (xDist === 0 && yDist === 0 && t === 1) return false;
  return xDist <= t && yDist <= t;
};

module.exports.isReachableAtTime = isReachableAtTime;
