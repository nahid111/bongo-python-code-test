#### Below is the written test for Bongo’s Python Engineer position. Please read through the entire test before starting to write it.

####1. Write the following function’s body. A nested dictionary is passed as parameter. You need to print all keys with their depth.

<u>Sample Input:</u><br><br>
a = { <br>
&nbsp; &nbsp; “key1”: 1, <br>
&nbsp; &nbsp; ”key2”: { <br>
&nbsp; &nbsp; &nbsp; &nbsp; “key3”: 1, <br>
&nbsp; &nbsp; &nbsp; &nbsp; “key4”: { <br>
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; “key5”: 4 <br>
&nbsp; &nbsp; &nbsp; &nbsp; } <br>
&nbsp; &nbsp; } <br>
} <br><br>

<u>Sample Output:</u><br><br>
key1 1<br>
key2 1<br>
key3 2<br>
key4 2<br>
key5 3<br>

def print_depth(data): <br>
&nbsp; &nbsp; &nbsp; &nbsp; # Write function body

You may write additional function.





####2. Write a new function with same functionality from Question 1, but it should be able to handle a Python object in addition to a dictionary from Question 1.

<u>Sample Input:</u><br><br>
class Person(object): <br>
&nbsp; &nbsp; def __init__(self, first_name, last_name, father): <br>
&nbsp; &nbsp; &nbsp; &nbsp; self.first_name = first_name <br>
&nbsp; &nbsp; &nbsp; &nbsp; self.last_name = last_name <br>
&nbsp; &nbsp; &nbsp; &nbsp; self.father = father <br>

person_a = Person(“User”, “1”, none) <br>
person_b = Person(“User”, “2”, person_a)

a = { <br>
&nbsp; &nbsp; “key1”: 1, <br>
&nbsp; &nbsp; ”key2”: { <br>
&nbsp; &nbsp; &nbsp; &nbsp; “key3”: 1, <br>
&nbsp; &nbsp; &nbsp; &nbsp; “key4”: { <br>
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; “key5”: 4 <br>
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; “user”: person_b, <br>
&nbsp; &nbsp; &nbsp; &nbsp; } <br>
&nbsp; &nbsp; } <br>
} <br><br>

<u>Sample Output:</u><br><br>
key1 1<br>
key2 1<br>
key3 2<br>
key4 2<br>
key5 3<br>
user: 3<br>
first_name: 4<br>
last_name: 4<br>
father: 4<br>
first_name: 5<br>
last_name: 5<br>
father: 5<br>

def print_depth(data): <br>
&nbsp; &nbsp; &nbsp; &nbsp; # Write function body

You may write additional function.





#### 3. Write following functions body. 2 Nodes are passed as parameter. You need to find Least Common Ancestor and print its value. Node structure are as following:

class Node{ <br>
&nbsp; &nbsp; &nbsp; &nbsp; value; <br>
&nbsp; &nbsp; &nbsp; &nbsp; parent; <br>
}<br>
![example tree](unnamed.png)


Ancestor Definition:
1) Any node falls under parent chain till root node.
2) A node is an ancestor of itself.


For example: if we consider Node 7 it’s ancestors will be 1, 3, and 7.

All nodes values are unique for this tree.

Your function needs to find least common ancestor (closest common ancestor). For an example
for the tree image, <br>
if 6 and 7 passed to lca it should return 3 <br>
if 3 and 7 passed to lca it should return 3 <br>

def lca(node1, node2): <br>
&nbsp; &nbsp; &nbsp; &nbsp; # Write function body

You may write additional function. <br>
Explain the Runtime and Memory requirements for your solution.

Submission:
1. Implement solution for these problems.
2. You are encouraged to write unit test for all three problems.
3. Upload to github/bitbucket or any other code sharing platform.
4. Send an email to recruitment@bongobd.com with subject “Bongo Python Code Test” with your code repository URL in the email body.
5. Please attach your detailed resume in the email.

If you have any questions, please send them to mirza.asif@bongobd.com with a subject line of
“Questions on Bongo Python Code Test”.
