def largestRectagleArea(histogram):
        stack=[]
        maxArea=0
        n=len(histogram)+1
        for i in range(n):
            while(len(stack)!=0 and (i==n-1 or histogram[stack[-1]]>= histogram[i])):
                    height=histogram[stack[-1]]
                    stack.pop()
                    if(len(stack)==0):
                            width=i
                    else:
                            width=i-stack[-1]-1
                    maxArea=max(maxArea,width*height)
            stack.append(i)
        return maxArea

print(largestRectagleArea([2, 1, 5, 6, 2, 3, 1]))