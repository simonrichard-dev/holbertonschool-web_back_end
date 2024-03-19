# <p align='center'>Redis Basic</p>

![redis basics](https://github.com/simonrichard-dev/holbertonschool-web_back_end/blob/main/0x0B_redis_basic/assets/A-Guide-to-Redis-Python_Watermarked.fadbf320f71f.jpg)

## Description :speech_ballon:
This project focuses on learning the basics of using Redis for various operations, including acting as a simple cache. It involves setting up Redis on Ubuntu 18.04, using it within a container, and performing tasks such as writing and reading data to and from Redis, incrementing values, storing and retrieving lists, and more.

## Resources :books:
 - [Redis commands](https://redis.io/commands/)
 - [Redis python client](https://redis-py.readthedocs.io/en/stable/)
 - [How to Use Redis With Python](https://realpython.com/python-redis/)
 - [Redis Crash Course Tutorial](https://www.youtube.com/watch?v=Hbt56gFj998)

## Learning Objectives :brain:
Understand how to use Redis for basic operations.
Learn how to utilize Redis as a simple cache for efficient data storage and retrieval.

## Requirements :computer:
- All code should be interpreted/compiled on Ubuntu 18.04 LTS using Python 3.7.
- Files should adhere to specific conventions such as ending with a new line and starting with #!/usr/bin/env python3.
- Code should follow the pycodestyle style (version 2.5).
- Redis installation and setup instructions are provided for Ubuntu 18.04.
- Redis can be used within a container, with instructions for starting the Redis server.

## Installation :gear:
To install Redis on Ubuntu 18.04, run the following commands:

Copy code
```
$ sudo apt-get -y install redis-server
$ pip3 install redis
$ sudo sed -i "s/bind .*/bind 127.0.0.1/g" /etc/redis/redis.conf
```
When using Redis in a container, ensure to start the Redis server with:

Copy code
```
$ service redis-server start
```

## Tasks :hammer_and_pick:
0. Writing strings to Redis
Create a Cache class that initializes a Redis client and provides a method to store data in Redis using a randomly generated key.
1. Reading from Redis and recovering original type
Implement a method to retrieve data from Redis and optionally convert it back to the original format.
2. Incrementing values
Implement a decorator to count how many times methods of the Cache class are called.
3. Storing lists
Define a decorator to store the history of inputs and outputs for a specific function.
4. Retrieving lists
Implement a function to display the history of calls of a particular function.
Each task builds upon the previous one, introducing new concepts and techniques for using Redis effectively.

## Contact
- LinkedIn Profile: [Simon Richard](https://www.linkedin.com/in/simonrichard-dev/)