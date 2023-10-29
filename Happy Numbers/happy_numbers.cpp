#include <iostream>
#include <string.h>
#include <vector>
#include <algorithm>

using namespace std;

int theIterator(int a, int b);

int main()
{
    int a, b;
    cin >> a >> b;
    int res = theIterator(a, b);
    cout << res;
    return 0;
}

int theIterator(int a, int b)
{
    vector<int> num_list;
    int i = a;

    while (i < b + 1)
    {
        int n = i;
        vector<int> sums;

        while (true)
        {
            int sum = 0;
            int na = n;
            while (na != 0)
            {
                int num = na % 10;
                sum += num * num;
                na /= 10;
            }
            if (sum == 1)
            {
                num_list.push_back(i);
                break;
            }
            if (count(sums.begin(), sums.end(), sum))
            {
                break;
            }
            sums.push_back(sum);
            n = sum;
        }
        i++;
    }
    return num_list.size();
}