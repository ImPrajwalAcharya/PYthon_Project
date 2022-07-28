
#include<conio.h>
#include<iostream>
using namespace std;

void average(int  heap[]){
    int i=0;
    while (heap[i]!=NULL)
    {
        cout<<heap[i];
        cout<<",";
        i++;
    }
}
int main(){
    int array[] = {1, 2, 3, 4, 5,5,6,7,7,8,7,5,34,4,NULL};
    average(array);
    return 0;
}