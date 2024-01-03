# 0x14. JavaScript - Web Scraping

## Resources
Read or watch:

- [Working with JSON data](https://www.json.org/json-en.html)
- [The workflow of accessing the attributes of a simply-created JSON object by Jimmy Tran from Cohort 1 - San Francisco](https://www.youtube.com/watch?v=UUJShZCujjM)
- [request module](https://www.npmjs.com/package/request)
- [Modern JS](https://developer.mozilla.org/en-US/docs/Web/JavaScript)

**General**
- Why JavaScript programming is amazing
- How to manipulate JSON data
- How to use request and fetch API
- How to read and write a file using fs module

## More Info
**Install Node 14**
```bash
$ curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -
$ sudo apt-get install -y nodejs
```

**Install semi-standard**
Documentation: [Semi-Standard](https://github.com/standard/semistandard)
```bash
$ sudo npm install semistandard --global
```

**Install request module and use it**
Documentation: [Request](https://www.npmjs.com/package/request)
```bash
$ sudo npm install request --global
$ export NODE_PATH=/usr/lib/node_modules
```
*Notes: Request module has been deprecated since February 2020 - the team is considering an alternative to replace this module - however, it’s a really simple and powerful module for practicing web-scraping in JavaScript (and still used a lot in the industry).*

JavaScript is considered amazing for several reasons:

1. **Versatility:** JavaScript is a versatile programming language that can be used both on the client side (browser) and server side (Node.js). This allows developers to use the same language across different environments.

2. **Asynchronous Programming:** JavaScript excels at handling asynchronous tasks, making it suitable for building responsive and dynamic web applications. Features like callbacks, promises, and async/await make asynchronous programming more manageable.

3. **Extensive Ecosystem:** JavaScript has a vast ecosystem of libraries and frameworks, such as React, Angular, and Vue.js for front-end development, and Express.js for server-side development. This rich ecosystem facilitates rapid development.

Regarding manipulating JSON data:

1. **Built-in JSON Support:** JavaScript has built-in support for JSON (JavaScript Object Notation), making it easy to parse and stringify JSON data.

2. **JSON Methods:** JavaScript provides `JSON.parse()` for converting a JSON string to a JavaScript object and `JSON.stringify()` for converting a JavaScript object to a JSON string.

When it comes to using the `request` and `fetch` API:

1. **`request` Module:** In Node.js, the `request` module is often used for making HTTP requests. It simplifies the process of sending HTTP requests and handling responses.

2. **`fetch` API:** On the browser side, the `fetch` API is commonly used for making HTTP requests. It provides a modern, promise-based interface for working with HTTP.

For reading and writing files using the `fs` module:

1. **`fs` Module:** In Node.js, the `fs` (file system) module is used for file-related operations. It provides functions like `fs.readFile()` and `fs.writeFile()` for reading and writing files, respectively.

2. **Asynchronous Operations:** Many file operations in Node.js are asynchronous, and callbacks, promises, or async/await can be used to handle these operations in a non-blocking manner.

Understanding these aspects allows developers to efficiently work with data, make HTTP requests, and handle file operations in JavaScript, contributing to the language's overall appeal and versatility.
