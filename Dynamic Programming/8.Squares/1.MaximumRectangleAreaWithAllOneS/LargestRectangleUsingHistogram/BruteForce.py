#Using This problem Solution=> We can solve MaximumReactingleWithAllOnes
def LargestRectangleInTheHistogram(histogram): #0(N^2) sc:0(n) INPUT ONLY

    maxArea=-99999999
    for i in range(len(histogram)):

        #Find Left Minimum
        
        leftminimumIndex=i-1
        while(leftminimumIndex>=0 and histogram[leftminimumIndex]>=histogram[i]):
            leftminimumIndex=leftminimumIndex-1
        leftminimumIndex=leftminimumIndex+1

        rightminimumIndex=i+1
        while(rightminimumIndex<len(histogram) and histogram[rightminimumIndex]>=histogram[i]):
            rightminimumIndex=rightminimumIndex+1
        rightminimumIndex=rightminimumIndex-1
        #Find Maximum

        rectangleArea=((rightminimumIndex-leftminimumIndex)+1)*histogram[i]

        maxArea=max(maxArea,rectangleArea)
    return maxArea


histogram=[2,1,5,6,2,3]
print(LargestRectangleInTheHistogram(histogram))



