/*
    You are given four integers sx, sy, fx, fy, and a non-negative integer t.

    In an infinite 2D grid, you start at the cell (sx, sy). Each second, you must move to any of its adjacent cells.

    Return true if you can reach cell (fx, fy) after exactly t seconds, or false otherwise.

    A cell's adjacent cells are the 8 cells around it that share at least one corner with it.
    You can visit the same cell several times.
*/

const isReachableAtTime = (sx, sy, fx, fy, t) => {
  /*
        Plan:
            Calculate the euclidean distance from start point to end point
            if the distance is greater than the time it's impossible to reach the end point before
            time runs out

            euclidean distance = abs(sqrt((fx - sx)**2 + (fy - sy)**2))
    */
  const euclidDist = Math.abs(Math.sqrt((fx - sx) ** 2 + (fy - sy) ** 2));
  return euclidDist <= t;
};

module.exports.isReachableAtTime = isReachableAtTime;
