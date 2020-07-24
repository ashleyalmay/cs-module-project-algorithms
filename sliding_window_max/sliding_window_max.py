'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
#from collections import deque
#def sliding_window_max(nums, k):
    # Your code here
    # q = deque()
    # results = []
    # for i in range(k):
    #     while q and nums[i] >= nums[q[-1]]:
    #         q.pop()
    #     q.append(i)
    # for i in range(k, len(nums)):
    #     results.append(nums[q[0]])
    #     while q and q[0] <= i - k:
    #         q.popleft()
    #     while q and nums[i] >= nums[q[-1]]:
    #         q.pop()
    #     q.append(i)
    # results.append(nums[q[0]])
    # return results

nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
def sliding_window_max(arr, k):
#    left = 0
#    right = k
#    answer = []
#    while right <= len(arr):
#        window = arr[left:right]
#        max_elem = max(window)
#        answer.append(max_elem)
#        left += 1
#        right += 1
#    return answer
#print(sliding_window_max(nums, k))



#window variable max length = k
#start and end variable
    start = 0
    end = k
#make the new array that will get apppend in later
    new_list = []
#loop thur the list
    for i in nums:
#if end > length of nums:
        if end >len(nums):
            break
#create our window = nums[start:end]
        window = nums[start:end]
#store our window list.sort
        window.sort()
#new_list.append(window[-1])
        new_list.append(window[-1])
        start += 1
        end += 1
#then return the new_list
    return new_list







if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
