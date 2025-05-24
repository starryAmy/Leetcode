var TimeLimitedCache = function() {
  this.cache = new Map();
};

/**
* @param {number} key
* @param {number} value
* @param {number} duration time until expiration in ms
* @return {boolean} if un-expired key already existed
*/
TimeLimitedCache.prototype.set = function(key, value, duration) {
let now = Date.now();
const exists = this.cache.has(key) && this.cache.get(key).expire > now;
this.cache.set(key, {value, expire: now + duration});
return exists;
};

/**
* @param {number} key
* @return {number} value associated with key
*/
TimeLimitedCache.prototype.get = function(key) {
const now = Date.now()
if (this.cache.has(key)) {
  const entry = this.cache.get(key);
  if (entry.expire > now) {
      return entry.value;
  } else {
      this.cache.delete(key);
  }
}
return -1
};

/**
* @return {number} count of non-expired keys
*/
TimeLimitedCache.prototype.count = function() {
const now = Date.now();
let count = 0;

// Iterate through entries and count only unexpired ones
for (const [key, entry] of this.cache) {
if (entry.expire > now) {
  count++;
} else {
  this.cache.delete(key); // Cleanup expired keys
}
}

return count;
}

/**
* const timeLimitedCache = new TimeLimitedCache()
* timeLimitedCache.set(1, 42, 1000); // false
* timeLimitedCache.get(1) // 42
* timeLimitedCache.count() // 1
*/
