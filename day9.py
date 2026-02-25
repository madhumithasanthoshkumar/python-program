#priority queue
#removed element based on priority instead of order
#higher priority -> removed first
# not normal fifo
# smaller number= higher priority

# # real time
# hospital emergency room
# cpu task scheduling
# printer task proority
# network packet routing


# normal queue vs priority queue

# #heap
# # smaller number= higher priority
# #automatic sorting
# #uses heap module


# Pseudocose


# insert


# create empty priority queue
# inseert element with priority
# heap arrange automatically


# remove
# remove smallest priority elements


# import heapq
# pq=[]
# heapq.heappush(pq,3)
# heapq.heappush(pq,2)
# heapq.heappush(pq,1)

# print("Priority queue:",pq)

# print("Removed element:",heapq.heappop(pq))
# print("Removed element:",heapq.heappop(pq))
# print("Removed element:",heapq.heappop(pq))
# import heapq
# pq = []
# heapq.heappush(pq, (2, "medium task"))
# heapq.heappush(pq, (1, "high task"))
# heapq.heappush(pq, (3, "low task"))
# while pq:
#     priority, task = heapq.heappop(pq)
#     print(priority, task)
# def finalValueAfterOperations(operations):
#     x = 0
#     for op in operations:
#         if '+' in op:
#             x += 1
#         else:
#             x -= 1       
#     return x
# operations = ["--X","X++","X++"]
# print(finalValueAfterOperations(operations))
# list1=[0,1,2,3,5]
# n=len(list1)
# missing_value=(n*(n+1)//2)-sum(list1)
# print("Missing value=",missing_value)
# list1.insert(missing_value,missing_value)
# print(list1)
# list1=[0,1,4,6,8,9]
# max_list=max(list1)
# print("Missing values")
# for i in range(max_list):
#     if i not in list1:
#         print(i,end=" ")
#         list1.insert(i,i)
# print("\nList=",list1)
# print("After removing duplicates:", result)
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# def deleteDuplicates(head):
#     current = head
    
#     while current and current.next:
#         if current.val == current.next.val:
#             current.next = current.next.next
#         else:
#             current = current.next
            
#     return head
# head = ListNode(1, ListNode(1, ListNode(2)))
# new_head = deleteDuplicates(head)

# while new_head:
#     print(new_head.val, end=" ")
#     new_head = new_head.next
def reverseWords(s):
    words = s.split()
    result = []
    for word in words:
        result.append(word[::-1])  
    return " ".join(result)
s = "Let's take LeetCode contest"
print(reverseWords(s))