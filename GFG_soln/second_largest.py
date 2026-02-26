class solution:
    def Secondlargest(self, arr):
        n= len(arr)
        largest = -1
        second = -1
        for i in range(n):
            if(arr[i] > largest):
                second = largest
                largest = arr[i]
            elif(arr[i] < largest and arr[i] > second):
                second = arr[i]
        return second
    

arr = [67,78,45,90,55]
obj = solution()
result = obj.Secondlargest(arr)
print(result)