/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var filter = function(arr, fn) {
    let number = []
    for ( i = 0; i < arr.length; i++ ){
        if(fn(arr[i], i)) {
            number.push(arr[i])
        }
    }
    return number
};
