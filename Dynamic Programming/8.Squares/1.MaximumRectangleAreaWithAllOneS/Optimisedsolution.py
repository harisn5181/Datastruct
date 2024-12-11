class Solution:
    def maximalRectangle(self, matrix):
        height=[0]*len(matrix[0])
        maxArea=0
        for i in range(len(matrix)):
              for j in range(len(matrix[i])):
                    if matrix[i][j]==1:
                          height=height[j]+1
                    else:
                          height=0
              maxArea=max(self.largestRectagleArea(),maxArea)
        return maxArea

    def largestRectagleArea(self,histogram):
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