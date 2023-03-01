#include <vector>
#using std::vector;

class Solution
{
public:
    void swap(vector<int> &nums, int a, int b)
    {
        int temp = nums[a];
        nums[a] = nums[b];
        nums[b] = temp;
    }

    int partition(vector<int> &nums, int low, int high)
    {
        int pivot = nums[high];
        int ind = low - 1;
        for (int i = low; i < high; i++)
        {
            if (nums[i] < pivot)
            {
                ind++;
                swap(nums, ind, i);
            }
        }
        swap(nums, ind + 1, high);
        return ind + 1;
    }

    void qS(vector<int> &nums, int start, int end)
    {
        if (start < end)
        {
            int pInd = partition(nums, start, end);
            qS(nums, start, pInd - 1);
            qS(nums, pInd + 1, end);
        }
    }

    vector<int> sortArray(vector<int> &nums)
    {
        qS(nums, 0, nums.size() - 1);
        return nums;
    }
};