class Solution:
 
                            #    ROTATE ARRAY

    def rotateArr(self, arr, d):
        #step 1: Find length of array
        n = len(arr)

        # step 2: Handle cases where d>n
        #Example: rotating 7 times in array of size 5 = rotate 2 times
        d = d % n
        # Step 3: Reverse first d elements
        # Example: [ 1,2,3,4,5] -> reverse(0,1)->[2,1,3,4,5]
        self.reverse(arr, 0, d-1)
        # Step 4: Reverse remaining elements
        #Example[2,1,3,4,5] -> reverse(2,4) -> [2,1,5,4,3]
        self.reverse(arr, d, n-1)
        # Step 5: Reverse whole array
        # Example: [2,1,5,4,3] -> reverse(0,4) -> [3,4,5,1,2]
        self.reverse(arr, 0, n-1)

    def reverse(self, arr, start, end):
        # This function reverses elements from index start to end
        while(start<=end):
            # Swap elements at start and end
            arr[start], arr[end] = arr[end], arr[start]
            # Move start forward
            start+=1
            # Move end backward
            end-=1


arr = [1,2,3,4,5]
d = 2

obj = Solution()   #Step 1: Create object
obj.rotateArr(arr, d) #Step 2: Call function
print(arr)  #Output result

