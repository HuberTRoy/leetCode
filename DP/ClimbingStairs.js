/**
 * @param {number} n
 * @return {number}
 */
 var climbStairs = function(n) {
    let dp = [
        1,
        2
    ]
    
    if (n <= 2) {
        return dp[n-1]
    }

    for (let i=2;i<n;i++) {
        dp.push(dp[i-2]+dp[i-1])
    }
    return dp[n-1]
};