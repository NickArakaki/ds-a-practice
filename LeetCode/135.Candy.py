"""
There are n children standing in a line. Each child is assigned a rating value given in the integer array ratings.

You are giving candies to these children subjected to the following requirements:

Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
Return the minimum number of candies you need to have to distribute the candies to the children.
"""
# function distributeCandy(childRatings) {
#     const candyDistribution = Array(childRatings.length).fill(1)
#     const ratingMap = {}


#     for (const [i, rating] of childRatings.entries()) {
#         if (rating in ratingMap) {
#             ratingMap[rating].push(i)
#         } else {
#             ratingMap[ratingMap] = [i]
#         }
#     }

#     const sortedRatings = Object.keys(ratingMap).sort((a, b) => a - b)
#     for (const rating of sortedRatings) {
#         for (const i of ratingMap[rating]) {
#             const currRating = childRatings[i]
#             const leftNeighborRating = i > 0 ? childRatings[i - 1] : Infinity
#             const rightNeighborRating = i < childRatings.length - 1 ? childRatings[i + 1] : Infinity
#             const leftCandies = i > 0 ? candyDistribution[i - 1] : 0
#             const rightCandies = i < candyDistribution.length - 1 ? candyDistribution[i + 1] : 0

#             if (currRating > leftNeighborRating && currRating > rightNeighborRating) {
#                 candyDistribution[i] += Math.max(leftCandies, rightCandies)
#             } else if (currRating > leftNeighborRating) {
#                 candyDistribution += leftCandies
#             } else if (currRating > rightNeighborRating) {
#                 candyDistribution += rightCandies
#             }

#         }
#     }

#     return candyDistribution.reduce((partialSum, a) => partialSum + a, 0);
# }
