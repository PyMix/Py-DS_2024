# Project III. Guess the Number

## Table of contents

[1. Project Description](#1-project-description)

[2. Problem Statement](#2-problem-statement)

[3. Data Overview](#3-data-overview)

[4. Workflow](#4-workflow)

[5. Results](#5-results)

[6. Conclusions](#conclusions)

---

## 1. Project Description

This project involves building a program that efficiently guesses a number chosen by the computer with the minimum number of attempts.

[↑ Return to Table of Contents](#table-of-contents)

## 2. Problem Statement

The goal is to minimize the number of attempts required to guess a number in a specified range.

### Competition Conditions

- The computer generates a random number within a given range.
- A virtual player guesses the number.
- The computer provides hints on whether the guess is higher or lower.
- The virtual player continues guessing until the number is identified.

### Evaluation Metrics

Performance is measured based on the **average number of attempts** required to correctly guess the number. The average is calculated over multiple simulations.

### Skills Practiced

- Random number generation.
- Implementing the binary search algorithm.
- Using loops and conditional statements.
- Creating reusable functions.

[↑ Return to Table of Contents](#table-of-contents)

## 3. Data Overview

This project relies on random number generation to simulate the guessing game.

[↑ Return to Table of Contents](#table-of-contents)

## 4. Workflow

1. Generate a random number within the specified range (default: 1–100).
2. Simulate a virtual player guessing the number.
3. Provide feedback on whether the guess is higher or lower.
4. Repeat the process until the correct number is guessed.
5. Calculate the average number of attempts over multiple simulations (default: 10,000).

[↑ Return to Table of Contents](#table-of-contents)

## 5. Results

Simulations for each range: 10,000

range | average number of attempts
|---|---|
| 1-100   | 5
| 1-1000  | 8
| 1-10000 | 12
| 1-100000| 15
| 1-1000000| 18

[↑ Return to Table of Contents](#table-of-contents)

## 6. Conclusions

The binary search algorithm is the fastest method to guess a number, as it halves the search range with each step,

### Support

If you find this project helpful, please consider starring the repository to show your support and encourage further development! ⭐️

[↑ Return to Table of Contents](#table-of-contents)
