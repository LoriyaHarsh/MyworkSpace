#include<iostream>
#include<vector>
using namespace std;

int main(){
    
    return 0;
}

class Solution {
public:
    long long minimumTime(vector<int>& time, int totalTrips) {
        int n = time.size();
        int count =0,trip=0;
        vector<int> time1;
        sort(time.begin(),time.end());
        count=time[0];
        trip=1;
        for (int i = 1; i < n; i++)
        {
            for (int j = i-1; j >= 0; j--)
            {
                if(time[i]>time[j]){
                    int a = (time[i]-time[i-1])/time[i-1];
                    count=count+time[i];
                    trip = trip +a;
                }
                else if(time[i]==time[i-1]){
                    trip = trip +1;
                    if(j-1=0){
                        trip++;
                    }
                }
            }
              
        }
        
    }
};