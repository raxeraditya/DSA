class AggresiveCow():
    def __init__(self) -> None:
        print("welcome to my code")
    def find_cow(self)-> int:
        k=4
        stalls:list[int] = [2,3,4,5,6,7,8]
        n = len(stalls)#lenth of stalls
        # print("Lenth is :",n)
        start = 1
        end = stalls[n-1]-stalls[0]
        # print("End Point :",end)
        while (start<=end):
            count = 1
            pos = stalls[0]
            mid = start + (end-start)//2
            print("mid of while loop :",mid)
            for i in range(1,n):
                if(pos+mid <= stalls[i]):
                    count+=1
                    pos = stalls[i]
                    print("pos of cow :",pos)
            if(count<k):
                # print("the mid value is count lesser than k",mid)
                end = mid - 1
                print("the end value is count lesser than k",end)
            else:
                start = mid+1
        print("The Cow is :",count)
        return count


"""
n = 7, pos = 2, end = 6 start = 1 mid = 3
"""


obj = AggresiveCow()
ANS = obj.find_cow()
print(ANS)