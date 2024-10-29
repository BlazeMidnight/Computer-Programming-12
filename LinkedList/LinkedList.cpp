#include <istream>
#include <string>
using namespace std;

/*
 class intStack {
 private:
 int* stackArray;
 int stackSize;
 int numEle;
 public:
 intStack(int);
 ~intStack();
 
 void push(int);
 void pop();
 bool isFull() const;
 bool isEmpty() const;
 void display() const;
 
 };
 
 
 int main() {
    IntStack myStack(5);
    myStack.push(5);
    myStack.push(10);
    myStack.push(15);
    myStack.push(20);
    myStack.push(25);
    myStack.push(30); // Should output stack is full

    cout << "Popping...\n";
    if(!myStack.isEmpty())
        cout << myStack.pop() << endl;
    if(!myStack.isEmpty())
        cout << myStack.pop() << endl;
    if(!myStack.isEmpty())
        cout << myStack.pop() << endl;
    
    cout << "\n Printing Remaining Nums: "
    myStack.display();
 
    cout << "\n Popping... \n";
    if(!myStack.isEmpty())
        cout << myStack.pop() << endl;
    if(!myStack.isEmpty())
        cout << myStack.pop() << endl;
 

 }
 
 */

class Node {
private:
    int data;
    Node* next;
public:
    Node(int data, Node* next = nullptr) {
        this->data = data;
        this->next = next;
    }
    
    friend ostream& operator<<(ostream& os, const Node& node) {
        os << "Data: " << node.data << " >> " << typeid(node.next).name();
        return os;
    }
    
    

};
