# Introduction
JavaScript, often abbreviated JS, is a programming language that is one of 
the core technologies of the World Wide Web, alongside HTML and CSS. It 
lets us add interactivity to pages

Apart from being used in the browser, it is also used in other non-browser 
environments as well such as Node.js for writing server-side code in 
JavaScript, Electron for writing desktop applications, React Native for 
mobile applications, and so on.

It is a lightweight interpreted (or just-in-time compiled), 
single-threaded, dynamic programming language supporting object-oriented, 
imperative, and declarative (e.g. functional programming) styles.

The standards for JavaScript are:
- `ECMAScript Language Specification (ECMA-262)`
- `ECMAScript Internationalization API specification (ECMA-402)`

# Ecma International - European Computer Manufacturers Association
Nonprofit standards organization for information and communication systems.
The organization was founded in 1961 to standardize computer systems in 
Europe.
It is located in Geneva.
It's an organization that creates standards for technologies.

## ECMA-262
Standard published by Ecma international. It contains the specification 
for a general purpose scripting language.

## ECMAScript
The specification defined in ECMA-262 for creating a general purpose 
scripting language.
While ECMA-262 is the name of the standard, it represents the scripting 
language specification ECMAScript.

## JavaScript
A general purpose scripting language that conforms to the ECMAScript 
specification.
By reading ECMAScript specification, you learn how to create a scripting 
language. By reading the JavaScript documentation, you learn how to use a 
scripting language.

## JavaScript Engine
A program or interpreter that understands and executes JavaScript code.
Engines include:
- Chrome V8
- Firefox SpiderMonkey
- Edge Chakra
- Safari JavaScriptCore

## JavaScript runtime
The environment in which the JavaScript code runs.

Applications make themselves available to JavaScript scripting by providing
“host objects” at runtime. For the client side, the JavaScript runtime 
would be the web browser, where host objects like windows and HTML 
documents are made available for manipulation.

The window and document objects are not actually a part of the core 
JavaScript language. They are Web APIs, objects provided by a browser 
acting as JavaScript’s host environment. For the server side, the 
JavaScript runtime is Node.js. Server-related host objects such as the 
file system, processes, and requests are provided in Node.js.

An interesting point: different JavaScript runtimes can share the same 
JavaScript engine. V8, for example, is the JavaScript engine used in both 
Google Chrome and Node.js — two very different environments.

## Babel
A transpiler that can convert ES6 code to ES5 code.
Commonly used to ensure cross-browser compatibility.
Concerned developers can use Babel to convert their ES6 code to a 
functionally equivalent version that only use ES5 features.

## Scripting language
A programming language designed specifically for acting on an existing 
entity or system.
For a general idea of what makes a programming language a scripting 
language, consider the commands “walk”, “run”, and “jump.” These actions 
require something to carry them out, perhaps a person, a dog, or a video 
game character. Without an actor to perform these commands, “walk”, “run”, 
and “jump” wouldn’t make sense. This set of actions is analogous to a 
scripting language that focuses on manipulating an external entity.

## TC39
The commitee under ECMA international for responsible for ECMAScript 
standardization.

## New versions of ECMAScript
In June 2015, the next versions of ECMAScript were decided to be published 
in June of every year.

## What is ESNext?
ESNext is a dynamic name that refers to whatever the current version of 
ECMAScript is a the given time.

## Sources
![MDN JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
![Brief History of JavaScript](https://roadmap.sh/guides/history-of-javascript)
![The difference between JavaScript and ECMAScript](https://www.freecodecamp.org/news/whats-the-difference-between-javascript-and-ecmascript-cba48c73a2b5/)
