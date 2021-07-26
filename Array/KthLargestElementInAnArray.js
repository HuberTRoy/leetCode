/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */

// 写了个快排和归并。
 function sort(arr) {
    // 快排
    if (arr.length === 0) {
        return arr
    }

    // 选种
    let bean = Math.floor((arr.length-1) / 2)
    let base = arr[bean]
    let bigger = []
    let smaller = []

    for (let [index, item] of arr.entries()) {
        if (index === bean) {
            continue
        }

        if (item >= base) {
            bigger.push(item)
        } else {
            smaller.push(item)
        }
    }

    return [...sort(smaller), base, ...sort(bigger)]

}

// 归并
function split(arr) {
    let bean = Math.floor((arr.length-1) / 2)
    let left = arr.slice(0, bean)
    let right = arr.slice(bean)

    return [left, right]
}

function merge(arr, arr2) {
    let result = []

    let index1 = 0
    let index2 = 0

    while (index1 <= arr.length - 1 && index2 <= arr2.length - 1) {
        if (arr[index1] < arr2[index2]) {
            result.push(arr[index1])
            index1 += 1
        } else if (arr[index1] > arr2[index2]) {
            result.push(arr2[index2])
            index2 += 1
        } else {
            result.push(arr[index1], arr2[index2])
            index1 += 1
            index2 += 1
        }
    }
    // 如果第一个arr
    if (index1 <= arr.length - 1) {
        result.push(...arr.slice(index1))
    }

    if (index2 <= arr2.length - 1) {
        result.push(...arr2.slice(index2))
    }

    return result
}

function sort2(arr) {
    if (arr.length <= 8) {
        return sort(arr)
    }
    let sp = split(arr)
    // return sp.reduce((a,b) => merge(a,b))
    return merge(sort2(sp[0]), sort2(sp[1]))
}
 


var findKthLargest = function(nums, k) {
    // nums = nums.sort((a,b) => b-a)
    // nums = sort(nums)
    // nums = split(nums)
    // nums = merge(nums[0], nums[1])
    nums = sort2(nums)
    // console.log(nums)
    return nums[nums.length-k]
};