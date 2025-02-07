/*
1. Static (Belongs to the Class, Not the Object)
A static member (variable or function) is associated with the class itself rather than any specific instance (object).

Static Member Variables
Shared by all objects of the class (i.e., only one copy exists).
Stored in global memory, not in each object’s memory.
Must be defined outside the class.
*/

#include <iostream>
using namespace std;

class MyClass {
public:
    static int count;  // Static variable declaration

    MyClass() {
        count++;
    }
};

int MyClass::count = 0;  // Definition outside the class

int main() {
    MyClass obj1, obj2, obj3;
    cout << "Count: " << MyClass::count << endl; // Output: 3
    return 0;
}


/*
Static Member Functions
Can only access static variables, not instance variables.
Can be called without creating an object.
Example: Static Function*/

class MyClass {
public:
    static int count;

    static void showCount() {
        cout << "Count: " << count << endl;
    }
};

int MyClass::count = 5;

int main() {
    MyClass::showCount(); // Calls static function without an object
    return 0;
}
//  Key takeaway: Static functions can be accessed using ClassName::FunctionName().
