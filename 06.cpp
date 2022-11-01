#include <iostream>
#include <vector>
#include <string>
#include <fstream>

using namespace std;

vector<int> getInputdata(string inputfile)
{
    ifstream inputdata;
    inputdata.open(inputfile);
    if (!inputdata)
    {
        cout << "Unable to open file";
        exit(1);
    }

    vector<int> initial;
    string current;

    while (inputdata >> current)
    {
        initial.push_back(stoi(current));
    }
    inputdata.close();

    return initial;
}

vector<int> evening(vector<int> morning)
{
    vector<int> temp;
    for (vector<int>::iterator iter = morning.begin(); iter < morning.end(); iter++)
        {
            if (*iter > 0)
            {
                temp.push_back(*iter - 1);
            }
            else
            {
                temp.push_back(6);
                temp.push_back(8);
            }
        }
    return temp;
}

int main()
{
    vector<int> inputdata = getInputdata(".\\input\\06_m.txt");
    for (int day = 0; day < 150; day++)
    {
        inputdata = evening(inputdata);
        cout << "Completed day " << day << "with current size " << inputdata.size()<< endl;
    }
}