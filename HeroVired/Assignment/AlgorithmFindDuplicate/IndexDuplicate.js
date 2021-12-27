function findDuplicate(arr, size)
{
    let i;
    console.log("The repeating elements are:");
    for (i = 0; i < size; i++) {
        var abs_value = Math.abs(arr[i]);
        if (arr[abs_value] >= 0)
            arr[abs_value] = -arr[abs_value];
        else
            console.log(abs_value + " ");
    }
}
 
// Driver Code
    let arr = [ 1, 2, 3, 1, 3, 6, 6 ];
    findDuplicate(arr, arr.length);

/* output
The repeating elements are:
1 
3 
6   */