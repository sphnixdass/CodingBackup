function print(a,n)
{
       for (let i = 0; i <= n; i++)
        console.log(a[i] + " ");
    console.log("\n");
}
 
// Sorts a[] in descending
// order using bubble sort.
function sort(a,n)
{   
    for (let i = n;
            i >= 0; i--)
        for (let j = n;
                j > n - i; j--)
            if (a[j] > a[j-1]){
                let tempswap = a[j];
                a[j] = a[j - 1];
                a[j - 1] = tempswap;
            }
    print(a, n);
     
}
 

console.time("SortTime");
let a=[1,3,6,8,3,4,7,9,3];

sort(a, a.length -1);
console.timeEnd("SortTime");

// output:
// 9 
// 8 
// 7 
// 6 
// 4 
// 3 
// 3 
// 3 
// 1 