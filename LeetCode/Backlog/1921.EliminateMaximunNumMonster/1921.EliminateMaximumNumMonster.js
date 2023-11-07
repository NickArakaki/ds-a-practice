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
        Plan (brute-force):
        1. track current minute, init at 0

        2. iterate while current minute <= num monsters or a monster has reached the city

            2a. iterate over monsters
                2b. if any of the distances are less than or equal to 0, return the current minute, can only eliminate 1 monster/min
                2c. find the monster that is closest with the highest speed

            2. remove the monster, replace the distance at idx with null
            3. increment minute

        4. return length of the
*/
}
