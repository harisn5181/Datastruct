#include <iostream>
#include <vector>
#include <algorithm>  // For std::min

using namespace std;

//TC: 0(n)
//SC: 0(n)

class Solution {
public:
    int countSquares(vector<vector<int>>& arr) {
        int n = arr.size();  // number of rows
        int m = arr.empty() ? 0 : arr[0].size();  // number of columns

        // Initialize dp with the correct dimensions: n rows, m columns
        vector<vector<int>> dp(n, vector<int>(m, 0));
        int sum = 0;
        // Copy the first row of arr into dp
        for (int j = 0; j < m; j++) {
            dp[0][j] = arr[0][j];
            sum += dp[0][j];
        }

        // Copy the first column of arr into dp
        for (int i = 0; i < n; i++) {
            dp[i][0] = arr[i][0];
            if (i!=0)
            {
                sum += dp[i][0];
            }
        }

        // Fill the dp array using the logic for finding squares
      
        for (int i = 1; i < n; i++) {
            for (int j = 1; j < m; j++) {
                if (arr[i][j] == 0) dp[i][j] = 0;
                else {
                    dp[i][j] = 1 + std::min(std::min(dp[i - 1][j], dp[i][j - 1]), dp[i - 1][j - 1]);
                }
                 sum += dp[i][j];
            }
        }

        return sum;
    }
};

int main() {
    // Initialize the 2D vector (matrix)
    vector<vector<int>> arr = {
      {1,0,1},{1,1,0},{1,1,0}
    };

    // Create an instance of the Solution class
    Solution solution;

    // Call the countSquares function and store the result
    int result = solution.countSquares(arr);

    // Output the result
    cout << "Total number of squares: " << result << endl;

    return 0;
}
