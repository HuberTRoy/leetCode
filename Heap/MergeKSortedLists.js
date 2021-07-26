/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode[]} lists
 * @return {ListNode}
 */


 var mergeKLists = function(lists) {
    // 这个思路是打散之后又重新生成整个ListNode。
    // 参考价值不大。
    if (!lists.length) {
        return null
    }

    let newLists = []

    for (let i of lists) {
        let l = []
        while (i && i.next) {
            l.push(i.val)
            i = i.next
        }
        
        i && l.push(i.val)
        newLists.push(l)
    }


    let x = newLists.flat().sort((a,b) => a-b)
    if (!x.length) {
        return null
    }
    let resultNode = new ListNode(x[0])
    let indexNode = resultNode
    x.shift()
    while (x.length) {
        indexNode.next = new ListNode(x[0])
        x.shift()
        indexNode = indexNode.next
    }

    return resultNode
};