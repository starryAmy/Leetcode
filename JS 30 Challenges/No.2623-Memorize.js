/**
 * @param {Function} fn
 * @return {Function}
 */
function memoize(fn) {
    let called = {};
    return function(...args) {

      // check if this pair has already existed in this object
      if (called.hasOwnProperty(JSON.stringify(args))){
          return called[JSON.stringify(args)];
        }{
        let newPair = JSON.stringify(args);
        let result = fn(...args);
        // save this pair and the result into this object
        called[newPair] = result;
        return result;
        }
    }
}



let callCount = 0;
const memoizedFn = memoize(function (a, b) {
  callCount += 1;
  return a + b;
  })
  memoizedFn(2, 3) // 5
  memoizedFn(2, 3) // 5
  console.log(callCount) // 1
