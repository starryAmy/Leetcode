/**
 * @param {Function} fn
 * @param {number} t milliseconds
 * @return {Function}
 */
var debounce = function(fn, t) {
  let timer; // declare a variable first
  return function(...args) {
      clearTimeout(timer);

      timer = setTimeout(() => {fn(...args)}, t);
      return timer
  }
};

/**
* const log = debounce(console.log, 100);
* log('Hello'); // cancelled
* log('Hello'); // cancelled
* log('Hello'); // Logged at t=100ms
*/
