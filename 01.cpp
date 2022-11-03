#include <iostream>
#include <vector>
#include <string>
#include <fstream>

using namespace std;

int* getInputdata(string inputfile)
{
    ifstream inputstream;
    inputstream.open(inputfile);
    if (!inputstream)
    {
        cout << "Unable to open file";
        exit(1);
    }

    static int initial[2000];
    string current;
    int index = 0;

    while (inputstream >> current)
    {
        initial[index++] = stoi(current);
    }
    inputstream.close();

    return initial;
}

int solveTask1(int* inputs)
{
    int previousvalue = inputs[0];
    int counter = 0;
    for (int i = 1; i < 2000; i++)
    {
        if (inputs[i] > previousvalue)
        {
            counter++;
        }
        previousvalue = inputs[i];
    }
    return counter;
}

int solveTask2(int* inputs)
{
    int previousvalue = inputs[0] + inputs[1] + inputs[2];
    int counter = 0;
    for (int i = 1; i < 1998; i++)
    {
        int currentvalue = inputs[i] + inputs[i+1] + inputs[i+2];
        if (currentvalue > previousvalue)
        {
            counter++;
        }
        previousvalue = currentvalue;
    }
    return counter;
}

int main()
{
    int* inputs = getInputdata(".\\input\\01.txt");
    cout << "Solution for Task 1: " << solveTask1(inputs) << endl;
    cout << "Solution for Task 2: " << solveTask2(inputs) << endl;
}