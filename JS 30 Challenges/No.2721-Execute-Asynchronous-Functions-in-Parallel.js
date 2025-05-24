/**
 * @param {Array<Function>} functions
 * @return {Promise<any>}
 */
var promiseAll = function(functions) {
  // Promise is wrapped within the functions
  return Promise.all(functions.map(fn => fn()));
};


const promise = promiseAll([() => new Promise(res => res(42))])
promise.then(console.log); // [42]
