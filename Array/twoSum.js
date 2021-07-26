/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
// 简单的O(1)查找。
 var twoSum = function(nums, target) {
    let dicts = {}

    for (let [index, data] of nums.entries()) {
        dicts[data] ? dicts[data].push(index) : (dicts[data] = [index])
    }


    for (let i of nums) {
        if (dicts[target - i]) {
            if (target-i === i) {
                if (dicts[i].length === 2) {
                    return [dicts[i][0], dicts[i][1]]
                } else {
                    continue
                }

            }

            return [dicts[i][0], dicts[target-i][0]]
        }
    }
};