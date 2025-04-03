def mergeTwoLists(list1, list2):
        if not list1: return list2
        if not list2: return list1

        if list1.val < list2.val:
            list1.next = mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = mergeTwoLists(list1, list2.next)
            return list2

# Test case mergeTwoLists
mergeTwoLists([1,2,4], [1,3,4])
# Output: [1,1,2,3,4,4]
mergeTwoLists([], [])
# Output: []
mergeTwoLists([], [0])
# Output: [0]
mergeTwoLists([1], [])
# Output: [1]
mergeTwoLists([1], [0])
# Output: [0,1]

