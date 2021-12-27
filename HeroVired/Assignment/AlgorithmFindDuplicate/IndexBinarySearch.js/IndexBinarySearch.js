
const a = [];

for (var i = 0; i <100000; i++)
{
    a.push(Math.floor(Math.random() * 100000) + 1);
}

a.sort(function (a, b) {
    return a - b;
});

console.log('a,', a);

function binarySearch(arr, i) {
    var mid = Math.floor(arr.length / 2);
    console.log(arr[mid], i);
    
    if (arr[mid] === i) {
        console.log('match', arr[mid], i);
        return arr[mid];
    } else if (arr[mid] < i && arr.length > 1) {
        console.log('mid lower', arr[mid], i);
        return binarySearch(arr.splice(mid, Number.MAX_VALUE), i);
    } else if (arr[mid] > i && arr.length > 1) {
        console.log('mid higher', arr[mid], i);
        return binarySearch(arr.splice(0, mid), i);
    } else {
        console.log('not here', i);
        return -1;
    }
    
}

function forLoopSearch(arr, i) {

    for (var j = 0; j <arr.length; j++)
    {
        if (arr[j] == i){
            console.log("for loop result found: ",  arr[j]);
            return 0;
        }


    }
    console.log("for loop not result found: ", arr.length);
}

console.time("forLoopSearch");
console.log("forLoop :", forLoopSearch(a, 10000));
console.timeEnd("forLoopSearch");


console.time("BinarySearch");
var result = binarySearch(a, 10000);
console.log("result : ", result);
console.timeEnd("BinarySearch");




