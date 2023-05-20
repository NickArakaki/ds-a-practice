function twoSum(nums, target) {
    const targetNums = {}

    for (let i = 0; i < nums.length; i++) {
        const diff = target - nums[i]

        if (diff in targetNums) return [targetNums[diff], i]
        
        targetNums[nums[i]] = i
    }
}

console.log(twoSum([2,7,11,15], 9))
console.log(twoSum([3,2,4], 6))
console.log(twoSum([3,3], 6))