# Monkey Patching
Refers to the technique which allows us to modify or extend the behavior of the existing modules or objects at runtime.

It works by replacing or extending the methods or properties of an object at runtime. This is done by modifying the object's prototype or directly changing objects. This is useful for adding other functionality to existing code without modifying the original source.

```javascript
const originalLog = console.log;

console.log = function(...args) {
	originalLog.apply(this, "Pre-log:")
	originalLog.apply(this, args)
	originalLog.apply(this, "Post-log.")
}
```
## Monkey patching with commonjs modules
commonjs modules are cached and we can easily change the properties or methods of the module within this cache. After the change, the module will be used with the new properties or methods and when the module is required again it will be used with the new properties or methods thanks to the cache.
commonjs share the same instance of the module when required multiple times, which is the singleton pattern.
```javascript
// counter.js
let count = 0;

module.exports = {
	counter: ()=> count++;
}

// app.js
const {counter} = require("./counter");

console.log(counter()) // 0
console.log(counter()) // 1

const counter2 = require("./counter");
console.log(counter2()) // 2

const originalCounter = counter
counter = () => {
	const c = originalCounter()
	if (c % 2 == 0) {
		console.log("foo")
	} else {
		console.log("bar")
	} 
	return c
}

console.log(counter()) // bar 3
```
## Monkey patching with ES modules
In ES modules both named and default export are immutable and read-only. This means that we can't reassign bindings but we can modify the properties of the exported object.
```javascript
// logger.js
export function log(msg) {
	console.log(msg);
}

// main.js
import {log} from "./logger.js"

log.patched = true;
log.oldLog = log;
log.call = function() { // patch its call method
	console.log("Patched log!");
	this.oldLog.apply(null, arguments);
}

log("Hello"); // Patched log! Hello
console.log(log.patched); // true
```