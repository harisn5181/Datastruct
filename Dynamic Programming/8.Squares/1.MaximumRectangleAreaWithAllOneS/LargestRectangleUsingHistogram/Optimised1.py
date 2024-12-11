






def largestRectangleUsingHistogram(histogram):#TC: 0(N)+0(N) SC:3 O(N)
    nextLeftBoundary=[]
    stack=[]
    maxArea=-999999999999
    for i in range(len(histogram)):
        while(len(stack)!=0 and histogram[stack[-1]]>=histogram[i]):
            stack.pop()
        if len(stack)==0:
            nextLeftBoundary.append(0)
        else:
            nextLeftBoundary.append(stack[-1]+1)
        stack.append(i)
    nextRightBoundary=[0]*len(histogram)
    stack=[]
    for i in range(len(histogram)-1,-1,-1):
        while(len(stack)!=0 and histogram[stack[-1]]>=histogram[i]):
            stack.pop()
        if len(stack)==0:
            nextRightBoundary[i]=(len(histogram)-1)
        else:
            nextRightBoundary[i]=(stack[-1]-1)
        stack.append(i)

        rectangleArea=((nextRightBoundary[i]-nextLeftBoundary[i])+1) * histogram[i]
        maxArea=max(rectangleArea,maxArea)
    return maxArea

        
histogram=[2,1,5,6,2,3]
print(largestRectangleUsingHistogram(histogram))


