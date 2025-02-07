/*
3. Inheritance (Reusing Code)
Inheritance allows a class (child/derived class) to inherit properties and methods from another class (parent/base class).

Types of Inheritance in C++
Public Inheritance → Keeps public and protected members accessible.
Protected Inheritance → Makes public members protected.
Private Inheritance → Converts public and protected members to private.
Example: Public Inheritance
*/

#include <iostream>
using namespace std;

class Base {
public:
    void show() { cout << "Base class function" << endl; }
};

class Derived : public Base { // Inherits from Base
public:
    void display() { cout << "Derived class function" << endl; }
};

int main() {
    Derived obj;
    obj.show();    // Inherited function
    obj.display(); // Derived class function
    return 0;
}
// ✅ Key takeaway: The Derived class inherits Base::show(), enabling code reuse.

