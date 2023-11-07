/*
You are playing a video game where you are defending your city from a group of n monsters.
You are given a 0-indexed integer array dist of size n, where dist[i] is the initial distance
in kilometers of the ith monster from the city.

The monsters walk toward the city at a constant speed. The speed of each monster is given to
you in an integer array speed of size n, where speed[i] is the speed of the ith monster in kilometers per minute.

You have a weapon that, once fully charged, can eliminate a single monster. However,
the weapon takes one minute to charge. The weapon is fully charged at the very start.

You lose when any monster reaches your city. If a monster reaches the city at the exact moment the weapon
is fully charged, it counts as a loss, and the game ends before you can use your weapon.

Return the maximum number of monsters that you can eliminate before you lose, or n if you
can eliminate all the monsters before they reach the city.
*/

/*
      example: dist = [1,1,2,3] speed = [1,1,1,1]

      1. eliminate the closest monster with the highest speed
      2. move the remaining mosters by speed, multiply speed by num minutes that have passed
      3. if any of the distances are less than or equal to 0, return the num monsters eliminated

      minute 0:
      dist = [1, 1, 2, 3] speed = [1, 1, 1, 1]
      eliminate monster at idx 0 because they are the closest with the highest speed
      dist = [X, 1, 2, 3] speed = [X, 1, 1, 1]

      minute 1:
      dist = [X, 0, 1, 2] speed = [X, 1, 1, 1]
      A monster has reached 0 before you could reload therefore the max num eliminated is 1
*/

function eliminateMaximum(dist, speed) {
  /*
    Plan
    1. combine distance and speed into nested array [[dist[0], speed[0], ...]]
    2. sort combined array by distance (desc), and if distances are equal sort by speed (asc)
    3. track number of minutes that have passed, starting at 0
    4. iterate through sorted array
        4a. calculate the distance travelled, distance - speed * mins passed
        4b. if distance travelled is less than or equal to 0 then we cannot eliminate that monster before it reaches the city, return min passed
    5. return the number of monsters, if we get through all the monsters without returning we can eliminate all of them
  */
  const n = dist.length;
  const combined_arr = dist.map((dist, idx) => {
    return [dist, speed[idx]];
  });
  combined_arr.sort((a, b) => {
    return a[0] / a[1] - b[0] / b[1] || b[1] - a[1];
  });

  for (let i = 0; i < n; i++) {
    const [dist, speed] = combined_arr[i];
    const dist_travelled = dist - speed * i;

    if (dist_travelled <= 0) return i;
  }

  return n;
}

exports.eliminateMaximum = eliminateMaximum;
