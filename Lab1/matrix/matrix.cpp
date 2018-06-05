#include <iostream>
#include <ctime>
#include <ratio>
#include <chrono>
 
using namespace std;
 
int main(){
 
        cout << ("Enter an n:") << endl;
        int n = 30;
 
        int A[n][n];
        int B[n][n];
        int C[n][n];
        long mean =0;
        for(int i=0;i<n;i++){
            for(int j=0;j<n;j++){
                A[i][j]=1;
                B[i][j]=2;
            }
        }
 
        for(int row=0;row<n;row++){
            for(int col=0;col<n;col++){
                int result=0;
                for(int m=0;m<n;m++){
            std::chrono::steady_clock::time_point start = std::chrono::steady_clock::now();
                    result= result + A[row][m]*B[m][col];
                    std::chrono::steady_clock::time_point end = std::chrono::steady_clock::now();
                    std::cout << "took " << std::chrono::duration_cast<std::chrono::nanoseconds>(end - start).count() << "ns.\n";
 
                }
                C[row][col] = result;
                //System.out.print(result + " ");
            }
              //System.out.print("\n");
        }
 
 
        cout << ("---------")<< endl;
 
        //cout <<(mean/(n*n*n)+ " ms.") << endl;
 
 
return 0;
}
