/*
https://leetcode.com/explore/learn/card/array-and-string/203/introduction-to-string/1158/

A string is actually an array of unicode characters. You can perform almost all the operations we used in an array. You can try it out by yourself.

However, there are some differences. In this article, we will go through some of them which you should be aware of when dealing with a string. These features might vary a lot from one language to another. 


Compare Function
String has its own compare function (we will show you the usage of compare function in the code below).

However, there is a problem:
Can we use "==" to compare two strings?

It depends on the answer to the question:
Does the language support operator overloading?

1. If the answer is yes (like C++), we may use "==" to compare two strings.
2. If the answer is no (like Java), we may not use "==" to compare two strings. When we use "==", it actually compares whether these two objects are the same object.
*/
#include <iostream>

int main() {
    string s1 = "Hello World";
    cout << "s1 is \"Hello World\"" << endl;
    string s2 = s1;
    cout << "s2 is initialized by s1" << endl;
    string s3(s1);
    cout << "s3 is initialized by s1" << endl;
    // compare by '=='
    cout << "Compared by '==':" << endl;
    cout << "s1 and \"Hello World\": " << (s1 == "Hello World") << endl;
    cout << "s1 and s2: " << (s1 == s2) << endl;
    cout << "s1 and s3: " << (s1 == s3) << endl;
    // compare by 'compare'
    cout << "Compared by 'compare':" << endl;
    cout << "s1 and \"Hello World\": " << !s1.compare("Hello World") << endl;
    cout << "s1 and s2: " << !s1.compare(s2) << endl;
    cout << "s1 and s3: " << !s1.compare(s3) << endl;
}