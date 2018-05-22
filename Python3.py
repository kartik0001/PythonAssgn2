                                              
						ASSIGNMENT3 


1.

>>> li=[]
>>> num=input("Enter the value added in List")
Enter the value added in List 20
>>> li.append(num)
>>> print(li)
[' 20']


-----------------------------------------------------------------

2.

>>> l=[]
>>> num=input("Enter the value added in list")
Enter the value added in list 20
>>> l.append(num)
>>> l1=["google","apple","facebook","microsoft","tesla"]
>>> l.extend(l1)
>>> print(l)
[' 20', 'google', 'apple', 'facebook', 'microsoft', 'tesla']

-------------------------------------------------------------------

3.

>>> li=[1,2,3,4,2,2,2,2,5,6,4]
>>> li.count(2)
5

--------------------------------------------------------------------

4.

>>> li=[5,6,9,1,4,16,23,67,34,50,100]
>>> li.sort()
>>> print(li)
[1, 4, 5, 6, 9, 16, 23, 34, 50, 67, 100]

--------------------------------------------------------------------

5.
>>> A=[50,51,52,53,54,55]
>>> B=[56,57,58,59,60]
>>> C=[]
>>> C.extend(A)
>>> C.extend(B)
>>> C.sort()
>>> print("After merging of array A and B in C is")
After merging of array A and B in C is
>>> print(C)
[50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60]

---------------------------------------------------------------------

6.

	STACK USING THE LIST

>>> s=['A','B','C']
>>> s.append('D')
>>> print(s)
['A', 'B', 'C', 'D']
>>> s.append('E')
>>> print(s)
['A', 'B', 'C', 'D', 'E']
>>> print(s.pop())
E
>>> print(s)
['A', 'B', 'C', 'D']
>>> print(s.pop())
D
>>> print(s)
['A', 'B', 'C']


	QUEUE USING THE LIST


>>> from collections import deque
>>> q=deque(['A','B','C','D'])
>>> print(q)
deque(['A', 'B', 'C', 'D'])
>>> q.append('E')
>>> print(q)
deque(['A', 'B', 'C', 'D', 'E'])
>>> q.append('F')
>>> print(q)
deque(['A', 'B', 'C', 'D', 'E', 'F'])
>>> print(q.popleft())
A
>>> print(q.popleft())
B
>>> print(q)
deque(['C', 'D', 'E', 'F'])

----------------------------------------------------------------------------

7.

>>> li=[1,2,3,4,5,6,7,8,9,10]
>>> even,odd=[i for i in li if i%2==0],[i for i in li if i%2!=0]
>>> print(even,odd)
[2, 4, 6, 8, 10] [1, 3, 5, 7, 9]


-----------------------------------------------------------------------------
