# Unittests in JS

## Overview
This project focuses on implementing unit tests for JavaScript applications using Mocha as the testing framework, Chai for assertions, and Sinon for spies and stubs. It covers various aspects of unit testing, including async functions, integration testing, and utilizing hooks effectively.

## Requirements
Operating System: Ubuntu 18.04
Node Version: 12.x.x
Editors: vi, vim, emacs, Visual Studio Code
All files should have a .js extension and end with a new line.
A README.md file at the root of the project folder is mandatory.
Tests should be executed with npm run test *.test.js without any warnings or errors.

## Installation
Clone the repository: 
```sh
git clone https://github.com/simonrichard-dev/holbertonschool-web_back_end/
```
Navigate to the project directory:
```sh
cd personal_data
```
Install dependencies: 
```sh
npm install
```
Running Tests
Execute all tests with: npm run test *.test.js

## Project Structure
```sh
project-root/
│
├── test/                 # Contains test files
│   ├── testFile1.test.js # Test file 1
│   └── testFile2.test.js # Test file 2
│
├── src/                  # Contains source files
│   ├── file1.js          # Source file 1
│   └── file2.js          # Source file 2
│
└── README.md             # Project documentation
```

Tasks
0. Basic test with Mocha and Node assertion library
Implement a basic test using Mocha and Node's assertion library.
1. Combining descriptions
Combine test descriptions for better readability and organization.
2. Basic test using Chai assertion library
Write a basic test using Chai assertion library for more expressive assertions.
3. Spies
Learn and implement spies for tracking function calls.
4. Stubs
Utilize stubs for replacing functions during tests.
5. Hooks
Understand and utilize hooks for setup and teardown operations.
6. Async tests with done
Handle asynchronous tests using the done callback.
7. Skip
Learn how to skip tests when necessary.
8. Basic Integration testing
Write basic integration tests with a small Node server.
9. Regex integration testing
Perform integration testing using regular expressions.
10. Deep equality & Post integration testing
Implement tests for deep equality and post integration testing.

## Resources
 - [Mocha documentation](https://mochajs.org/)
 - [Chai documentation](https://www.chaijs.com/api/)
 - [Sinon documentation](https://sinonjs.org/#get-started)
 - [Express documentation](https://expressjs.com/en/guide/routing.html)
 - [Request documentation](https://www.npmjs.com/package/request)
 - [How to Test NodeJS Apps using Mocha, Chai, and SinonJS](https://www.digitalocean.com/community)

## Learning Objectives
By the end of this project, you will understand:

- How to write test suites using Mocha.
- Usage of different assertion libraries such as Node's built-in assertions and Chai.
- Strategies for presenting long test suites for better readability.
- Usage of spies for tracking function calls.
- Implementation of stubs for replacing functions.
- Utilization of hooks for setup and teardown operations.
- Handling async functions in unit tests.
- Writing integration tests for Node applications.

Author
[Simon Richard](https://www.linkedin.com/in/simonrichard-dev/)

License
This project is licensed under the MIT License.