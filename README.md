# Rotate Problem

Problem belonging to the post-classroom Mock Interview Question Repository.

## Problem Statement

Our goal is to write a function that will rotate a linked list by `k` places to the right.

For example, if we have the following input list:

a → b → c → d → e

After rotating by a `k` value of 2, we should get the following output list:

d → e → a → b → c

Notice that everything has been moved 2 spaces to the right. Anything that reaches the end of the list is wrapped back around to the beginning.

The value 'a' was originally in the 0th position (the head of the list), so when it is shifted by two, it ends up in the 2nd position.

The value 'e' was originally in the 4th position (the end of the list). When it is shifted two places, it wraps to the beginning of the list (position 0) and then moves one additional space, ending at the 1st position.

`k` is guaranteed to be positive.

Adapted from https://leetcode.com/problems/rotate-list/

## Examples

### Example 1

Rotating the following list

a → b → c → d → e

by 1 produces

e → a → b → c → d

### Example 2

Rotating the following list

a → b → c → d → e

by 2 produces

d → e → a → b → c

### Example 3

Rotating the following list

a → b → c → d → e

by 10 produces

a → b → c → d → e

### Example 4

Rotating the following list

55 → 8 → 2 → 99

by 6 produces

2 → 99 → 55 → 8

### Example 5

Rotating the following list

1 → 2

by 5 produces

2 → 1
