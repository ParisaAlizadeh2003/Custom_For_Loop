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
   CustomFor.iterate(input("Enter your iterable : "),CustomFor.capitalize)
   
if __name__ == "__main__":
    main()    