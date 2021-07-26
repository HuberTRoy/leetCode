// 给定一个无重复元素的正整数数组 candidates 和一个正整数 target ，找出 candidates 中所有可以使数字和为目标数 target 的唯一组合。

// candidates 中的数字可以无限制重复被选取。如果至少一个所选数字数量不同，则两种组合是唯一的。 

// 对于给定的输入，保证和为 target 的唯一组合数少于 150 个。

//  

// 示例 1：

// 输入: candidates = [2,3,6,7], target = 7
// 输出: [[7],[2,2,3]]
// 示例 2：

// 输入: candidates = [2,3,5], target = 8
// 输出: [[2,2,2,2],[2,3,3],[3,5]]
// 示例 3：

// 输入: candidates = [2], target = 1
// 输出: []
// 示例 4：

// 输入: candidates = [1], target = 1
// 输出: [[1]]
// 示例 5：

// 输入: candidates = [1], target = 2
// 输出: [[1,1]]
//  

// 提示：

// 1 <= candidates.length <= 30
// 1 <= candidates[i] <= 200
// candidate 中的每个元素都是独一无二的。
// 1 <= target <= 500

/**
 * @param {number[]} candidates
 * @param {number} target
 * @return {number[][]}
 */
 var combinationSum = function(candidates, target) {
    // 思路就是dp
    // 比如target 2 的解是子问题1的解+子问题1的解，和2自己
    // target 3 的解可以是子问题1的解+子问题1的解+子问题1的解 / 子问题1的解+子问题2的解和3自己
    // target 4 的解就是3的解+1+自己。
    // 变一下这个思路，7的解应该是自己(如果有) + 6 - 1中的组合。
    // 还可继续优化。

    candidates = candidates.sort((a, b) => {
        return a - b
    })

    let _find = {}
    
    candidates.map((item) => {
        _find[item] = 1
    })

    let dp = [
    ]

    if (candidates[0] === 1) {
        dp.push({
            num: 1,
            sub: [[1]]
        })
    } else {
        dp.push({
            num: 1,
            sub: []
        })
    }

    for (let i=2; i <= target; i++) {
        let sub = []
        let old = {}
        for (let j = i-1; j > 0; j--) {
            if (dp[j-1].sub.lenght !== 0 && _find[i-j]) {
                for (let c of dp[j-1].sub) {
                    let temp = [...c, i-j].sort((a, b) => {
                        return a - b
                    })
                    if (!old[temp.join('')]) {
                        sub.push(temp)
                        old[temp.join('')] = 1
                        continue
                    }

                }
            }
        }

        if (_find[i]) {
            sub.push([i])
        }

        dp.push({
            num: i,
            sub: sub
        })
    }

    return dp[dp.length - 1].sub
};