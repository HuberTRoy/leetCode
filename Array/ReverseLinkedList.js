/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */

// 翻转链表的思路
// 把head取出来，把head.next取出来，head.next.next也取出来。
// head.next = head
// 新的(head.next和head)与head.next.next进行新一轮交换。
// 直至空。
// PS，链表操作好麻烦。
 var reverseList = function(head) {

    let newHead = null

    // 先不判断进行一次交换
    let nHead = head
    if (!nHead) {
        return null
    }
    let next = nHead.next
    if (!next) {
        return nHead
    }
    let lNext = next.next

    next.next = nHead
    nHead.next = null

    newHead = next

    while (nHead && next && next.next) {
        nHead = lNext
        if (!nHead) {
            return newHead
        }

        next = nHead.next

        if (!next) {
            nHead.next = newHead
            return nHead
        }
        lNext = next.next

        next.next = nHead
        nHead.next = newHead

        newHead = next

    }
};