/**
 * @param {Function} fn
 * @param {number} t
 * @return {Function}
 */
var timeLimit = function(fn, t) {
  return async function(...args) {
    // make below teo Promises race to ruturn the one that runs faster
    return Promise.race([
      fn(...args),
      new Promise((_,reject) => {setTimeout(() => {reject("Time Limit Exceed")},t)})
    ]
    )
  }
};


const limited = timeLimit((t) => new Promise(res => setTimeout(res, t)), 100);
limited(150).catch(console.log) // "Time Limit Exceeded" at t=100ms
