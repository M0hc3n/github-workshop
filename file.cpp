#include <iostream>

using namespace std;

int fibo(int position)
{
    if(position==0)
    {
        return 0;
    }
    else{
        return fibo(position-1) + fibo(position-2);
    }
}

int main()
{
    cout << fibo(9) << " " << fibo(11) << " " << fibo(0) << endl;
}