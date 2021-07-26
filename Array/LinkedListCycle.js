/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */

/**
 * @param {ListNode} head
 * @return {boolean}
 */

// 两个指针，一个一次走一步，一个一次走两步，如果有环会在某处相遇。
 var hasCycle = function(head) {
    if (!head) {
        return false
    }
    let oneIndex = head
    let twoIndex = head.next

    if (!twoIndex) {
        return false
    }

    while (oneIndex && twoIndex) {
        if (oneIndex === twoIndex) {
            return true
        }

        oneIndex = oneIndex.next
        twoIndex = twoIndex.next

        if (!twoIndex || !twoIndex.next) {
            return false
        }

        twoIndex = twoIndex.next
    }

    return false
};