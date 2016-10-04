# project1
## Installation
First, install the project1 following:
- [NodeJS](https://nodejs.org/en/) (v4.x.x recommended)
- [MongoDB](https://www.mongodb.com/)

Second, start mongodb locally by running the `mongod` executable in your mongodb installation (you may need to create a `data` directory or set `--dbpath`).

Then, run `webgme start` from the project root to start . Finally, navigate to `http://localhost:8888` to start using project1!

The Model:
As I understand it a single process system is machine designed to carry out one process. Thus, in the model I created a folder to hold the system in my language.
Then the system itself is within the folder. Data is a part of the system in that input is passed in and output is passed out. A process is the transition between the input and output.
This means that input is the source which goes through a process and returns an output which is the destination. All three of these aspects make up the system.

Example:
For my example I imagined a process that checks to see if an input is valid. For example, the machine would take in an ID number of some manner and use a process to test if it is valid. 
The  process could lead to one of two outputs. The first is if the process determines the id is valid it returns true. The other is when the process determines it is not valid and returns false. 
