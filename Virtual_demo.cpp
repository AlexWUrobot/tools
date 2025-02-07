/*
2. Virtual (Used for Polymorphism & Dynamic Binding)
A virtual function allows a function to be overridden in derived classes and ensures that the correct function is called, even when using a base class pointer.

Without virtual (Static Binding) */

class Base {
public:
    void show() { cout << "Base class" << endl; }
};

class Derived : public Base {
public:
    void show() { cout << "Derived class" << endl; }
};

int main() {
    Base* ptr = new Derived();
    ptr->show();  // Calls Base::show() due to static binding
    delete ptr;
    return 0;
}
// 🛑 Issue: Even though ptr points to a Derived object, it still calls Base::show() (static binding).

// With virtual (Dynamic Binding)
class Base {
public:
    virtual void show() { cout << "Base class" << endl; }
};

class Derived : public Base {
public:
    void show() override { cout << "Derived class" << endl; }
};

int main() {
    Base* ptr = new Derived();
    ptr->show();  // Calls Derived::show() due to virtual function
    delete ptr;
    return 0;
}
// ✅ Key takeaway: virtual ensures the function is resolved at runtime (dynamic binding), calling Derived::show().
