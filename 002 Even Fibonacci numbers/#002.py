'''
#? Even Fibonacci numbers
#?===========================

Each new term in the Fibonacci sequence is generated by adding the previous two terms.
By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence
whose values do not exceed #!four million,
find the sum of the even-valued terms.
'''
i_pre = 0
i_next = 1
end = 4e6

total = 0
while i_pre <= end:
    if i_pre % 2 == 0:  # ? why not just use i_next
        total += i_pre
    copy = i_next
    i_next += i_pre
    i_pre = copy

print(total)
