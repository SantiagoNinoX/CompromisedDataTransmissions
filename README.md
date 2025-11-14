# 🔐 Compromised Data Transmissions
An advanced algorithm implementation project for detecting malicious code patterns in data transmissions using string matching and analysis techniques.
## 📋 Overview
This project analyzes data transmission files to detect:

Malicious code patterns (mcode) within transmissions
Mirrored/palindromic code sequences
Similarities between different transmission files

## 🎯 Problem Statement
Given 5 text files:

transmission1.txt, transmission2.txt - Data transmission files
mcode1.txt, mcode2.txt, mcode3.txt - Malicious code patterns

The program performs three main analyses using efficient string algorithms.

## 🔧 Algorithms Implemented
### Part 1: Pattern Matching - KMP Algorithm
Complexity: O(n + m)
Searches for malicious code patterns within transmission files using the Knuth-Morris-Pratt algorithm.
How it works:

Preprocesses the pattern to build an LPS (Longest Proper Prefix which is also Suffix) array
Avoids unnecessary character comparisons by utilizing the LPS array
Finds pattern occurrences in linear time

Output:
true 1234    # Pattern found at position 1234
false        # Pattern not found

### Part 2: Palindrome Detection - Manacher's Algorithm
Complexity: O(n)
Finds the longest mirrored code sequence (palindrome) in each transmission file.
How it works:

Transforms the string by inserting separators to handle even/odd length palindromes uniformly
Uses the "center-radius" approach with dynamic programming principles
Expands palindromes efficiently by reusing previously computed information

Output:
45 120    # Palindrome starts at position 45 and ends at 120

### Part 3: Longest Common Substring - Binary Search + Rolling Hash
Complexity: O(n log n) time, O(n) space
Identifies the longest common substring between two transmission files to measure their similarity.
How it works:

Binary Search: Searches for the maximum length of common substring
Rolling Hash (Rabin-Karp): Efficiently computes hashes of all substrings of a given length
Hash Comparison: Quickly identifies potential matches, then verifies actual equality

Why this approach?

More practical than Suffix Array for large files (avoids O(n²) memory)
Rolling hash updates in O(1) time using a sliding window
Binary search reduces the search space logarithmically

Output:
567 890    # Common substring found from position 567 to 890 in transmission1

## 🚀 Usage
Prerequisites

Python 3.7+

Running the Program
bashpython main.py
Ensure all 5 input files are in the same directory as the script.
File Format

Files contain only characters: 0-9, A-F, and newlines
Newlines are stripped during processing


## 📊 Example Output
PARTE 1: Pattern Matching
transmission1.txt contains mcode1.txt: True
transmission1.txt does not contain mcode2.txt: False
...

PARTE 2: Longest Palindromes
Palindrome in transmission1.txt: 45 120
Palindrome in transmission2.txt: 230 445

PARTE 3: Longest Common Substring
Common substring: 567 890

## 👥 Authors

Santiago Ramírez Niño (A01665906)
Alejandro Ignacio Vargas Cruz (A01659714)
Omar Llano Tostado (A01660505)

Course: Advanced Algorithm Analysis
Professor: Dr. Salvador E. Venegas-Andraca
Date: November 6, 2025

## 🎓 Key Learnings

KMP: Efficient pattern matching without backtracking
Manacher: Linear-time palindrome detection using clever preprocessing
Rolling Hash: Constant-time substring comparison using sliding window hashing
Trade-offs: Sometimes O(n log n) implementations outperform O(n) in practice due to memory constraints


## 📝 License
This project is for academic purposes only.
