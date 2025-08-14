# Multiple Inheritance 

* When a class is derived from more than one base class it is called multiple Inheritance. The derived class inherits all the features of the base case.



##### What will happen if the child and the parent have the same method?

* Child's method overrides parent's method.



##### What will happen if two parents have the same parent?

* In Python, when two parent classes in a multiple inheritance scenario share a common ancestor , this creates a "diamond problem" in the class hierarchy. Python resolves method and attribute lookups in such cases using the Method Resolution Order (MRO).
* When you call a method or access an attribute on an instance of the Child class, Python follows the MRO. It searches for the method/attribute in the Child class first. If not found, it proceeds to Parent1, then Parent2, and finally Grandparent (and then object). The first definition it encounters in this order is the one that is used.



