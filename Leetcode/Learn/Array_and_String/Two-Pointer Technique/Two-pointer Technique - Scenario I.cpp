/*
https://leetcode.com/explore/learn/card/array-and-string/205/array-two-pointer-technique/1156/

https://leetcode.com/explore/learn/card/array-and-string/205/array-two-pointer-technique/1156/


-> Example:
"Reverse the elements in an array."

The idea is to swap the first element with the end, advance to the next element and swapping repeatedly until it reaches the middle position. 

We can use two pointers at the same time to do the iteration: one starts from the first element and another starts from the last element. Continue swapping the elements until the two pointers meet each other.

Here is the code for your reference:
*/
void reverse(int *v, int N) {
    int i = 0;
    int j = N - 1;
    while (i < j) {
        swap(v[i], v[j]);
        i++;
        j--;
    }
}