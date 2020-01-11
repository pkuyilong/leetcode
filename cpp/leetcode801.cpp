


// set swapdefault, 导致要么他一直在交换,
// 要么一直没交换,达不到原来的要求

int min_count = INT_MAX;
dfs(&A, &B, int i, int count, bool swapdefault=true)
{
    if (A B increase)
    {
        min_count = min(min_count, count);
        return min_count;
    }
    if (swapdefault == true){
        swap(A[i], B[i]);
        dfs(A, B, i+1, count+1, swapdefault=true);
        swap(A[i], B[i]);
    }
    else:
        dfs(A, B, i+1, count, swapdefault=false);
}
