"""
Problem Statement:
With the range of numbers from 1 to n inclusive, we can make n! permutations. By labeling them in order starting from 1,
you are asked to return the kth permutation
"""
"""
Initial Thoughts:
... Need to learn that what I think is a permutation, is actually a factorial
"""
"""
Video Notes:
n = 4
 1234, 1243, 1324, 1342, 1423, 1432
 2134, 2143, 2314, 2341, 2413, 2431
 3124, 3142, 3214, 3241, 3412, 3421
 4123, 4132, 4213, 4231, 4312, 4321  
 Can be partitioned into 4 parts, each row starts with the same digit
 can find out row length by dividing total by n, so 24/4 = 6
 We can use this to narrow down which row we look at give k
 k % part_length = row (k is actually k-1 since we are indexing from 0)
 once row is narrowed down, k % n (using the k-1 value) gives the column of the permutation we want
 
 Now n has become 3, n! becomes 6, part_length becomes 2(n!/n) = 2
 Now that we guaranteed 3 to be first digit, its just a permutation of numbers 1, 2, 4
 which can be partitioned into 3 ways grouped by value in second digits place
 
 From here we can again find the partition by doing k/part_length = 3/2 = 1 => 
 Kth permutation is in part 1 (indexing from 0)
 
 Repeat previous step and now its down to two permutations, and again divide k/part_length = 1/1 = 1 =>
 Kth permutation is in partition 1 (indexing from)
 
 Repeat one last time where kth permutation is in partition 0
"""
def kth_permutation(n, k):
    permutation = []
    unused = list(range(1, n+1))
    # Building out all permutations
    fact = [1]*(n+1)
    for i in range(1, n+1):
        fact[i] = i*fact[i-1]
    k -= 1
    while n > 0:
        part_length = fact[n]//n
        i = k//part_length
        permutation.append(unused[i])
        unused.pop(i)
        n -= 1
        k %= part_length
    return ''.join(map(str, permutation))

if __name__ == '__main__':
    n = 4
    k = 15
    print(kth_permutation(n,k))