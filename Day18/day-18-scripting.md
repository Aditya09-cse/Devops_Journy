# Day 18 – Shell Scripting: Functions & Advanced Concepts

## Overview

Today I focused on writing cleaner, reusable, and safer shell scripts using:

- Functions
- Arguments
- Local variables
- Strict mode (`set -euo pipefail`)
- Modular scripting patterns

This day helped me move from basic scripting to production-style scripting.

---

# Task 1 – Basic Functions

## Script: functions.sh

```bash
#!/bin/bash

# Function to greet a user
greet() {
    echo "Hello, $1!"
}

# Function to add two numbers
add() {
    local sum=$(( $1 + $2 ))
    echo "Sum: $sum"
}

# Calling functions
greet "Aditya"
add 5 9


Output
