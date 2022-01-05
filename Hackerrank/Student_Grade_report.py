#include<iostream>

using namespace std;

void Grade_Check(int arr[],int n)
{
  for(int i=0;i<n;i++)
  {
    int result=((arr[i]/5)+1)*5;
    if(arr[i]>=38)
    {
    if((result-arr[i])<3)
       arr[i]=result;
    }
  }
  for(int i=0;i<n;i++)
     cout<<arr[i]<<endl;
}
int main()
{
  int n;
  cin>>n;
  int arr[n];
  for(int i=0;i<n;i++)
  {
    cin>>arr[i];
  }
  Grade_Check(arr,n);
}
