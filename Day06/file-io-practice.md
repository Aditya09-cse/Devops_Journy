# Day 06 – Linux Fundamentals: Read and Write Text Files

## Creating a file
```
touch
```
  -  touch used to create empty file
  -  for eg. notes.txt
## Writing text to a file
```
echo
```
  - print text to standard output
  - with > or >> , write text into file
## Appending new lines
```
 >> 
```
  - ">>" , adds new text at the end of file without deleting existing content.
  - often used with echo to append lines or blank spaces
    
## Reading the file back
```
cat
```
  - cat is used to read the content of file

### optional
```
tee
```
  - write and display at same/real time
  - echo " how are you " | tee -a notes.txt

```
head
```
  - used to print lines from starting
  - by default print first 10 lines
  - eg. head -n 2 notes.txt -> print first 2 lines of notes.txt
```
tail
```
  - used to print lines from last
  - by default print last 10 lines
  - eg. tail -n 2 notes.txt -> print last 2 lines of notes.txt
