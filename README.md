# **CustomFor - A Simple Custom Iterator**  

## **Overview**  
`CustomFor` is a lightweight Python utility that demonstrates **manual iteration** using an explicit iterator. Instead of using a traditional `for` loop, it manually retrieves elements using `next()` and applies a function to each item.  

🔹 Learn more about **Python Iterators** here: [Python Iterators](https://docs.python.org/3/tutorial/classes.html#iterators)  

## **Features**  
✅ Custom iteration over any iterable  
✅ Applies a given function to each item  
✅ Includes a built-in `capitalize` function  

## **Installation**  
No external dependencies are required. Just clone the repository and run the script.  

```bash
git clone https://github.com/YOUR-USERNAME/custom-for-loop.git
cd custom-for-loop
python custom_for.py
```

## **Usage**  
Here’s how the `CustomFor` class works:  

```python
class CustomFor:
    @staticmethod
    def iterate(iterable, func):
        iterator = iter(iterable)
        while True:
            try:
                item = next(iterator)
            except StopIteration:
                return
            else:
                func(item)

    @staticmethod
    def capitalize(item):
        print(str.capitalize(item))

def main():
    CustomFor.iterate(input("Enter your iterable: "), CustomFor.capitalize)

if __name__ == "__main__":
    main()
```

### **Example**  
#### **Input:**  
```
Enter your iterable: hello
```
#### **Output:**  
```
H
E
L
L
O
```

## **Contributing**  
Want to improve this project? Feel free to fork the repository and submit a pull request! 🚀  

## **License**  
This project is licensed under the **MIT License**.  

---
