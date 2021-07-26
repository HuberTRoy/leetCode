// 这个有图，直接看链接吧。
// https://leetcode-cn.com/problems/reverse-nodes-in-k-group/
// hard

/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} k
 * @return {ListNode}
 */

// 思路就是获取k个节点，然后翻转。
// 循环这个操作。
// 思路不难，个人感觉难点在于ListNode是在不好操作。
var reverseKGroup = function(head, k) {
    function getKNodes(head) {
        let nodes = []
        let newHead = head
        
        // 
        while (nodes.length < k && newHead) {
            nodes.push(newHead)
            newHead = newHead.next
        }

        return nodes
    }

    function reverse(nodes) {
        // 将nodes里的ListNode关系翻转
        if (!nodes.length) {
            return null
        }

        if (nodes.length === 1) {
            return [nodes[0],null,null]
        }

        // 新开始的节点应为最后一个节点的下一个
        let newStartNode = nodes[nodes.length - 1].next
        // 最后一个节点是翻转前的第一个节点
        let lastNode = nodes[0]

        let rNodes = nodes.reverse()
        // 翻转后的头节点是翻转后的最后一个节点。
        let first = rNodes[0]
        let indexF = first
        for (let i of rNodes.slice(1)) {
            i.next = null
            indexF.next = i
            indexF = i
        }
        // 返回新的头
        // 和下次迭代应该开始新头，为原nodes[-1]的next
        return [first, newStartNode, lastNode]

    }

    let first = getKNodes(head)

    if (!first.length) {
        return null
    }

    if (first.length < k) {
        return head
    }

    let [newHead, newStartNode, lastNode] = reverse(first)
    let indexNewHead = lastNode
    
    // 循环翻转
    // newHead为新的head，返回用，newStartNode是下一次取K个node开始的节点。
    // lastNode为当前节点的最后一个节点，用来将新的节点的head接到最后一个节点上。
    while (1) {
        if (!newStartNode) {
            return newHead
        }
        let kNodes = getKNodes(newStartNode)
        if (kNodes.length < k) {
            if (indexNewHead) {
                indexNewHead.next = kNodes[0]
            }
            return newHead
        }
        
        let [n, ns, l] = reverse(kNodes)
        indexNewHead.next = n
        newStartNode = ns
        lastNode = l
        indexNewHead = l
    }
};