

class Fibonacci:

    def __init__(self, thing):
        self.thing = thing
        self.x = 0
        self.y = 1


    def __iter__(self):
        return self
    

    def __next__(self):
        if self.x > self.thing:
            raise StopIteration
        current = self.x
        self.x, self.y = self.y, self.x + self.y
        return current
    

fibonacci_iterator = Fibonacci(100)


print("Using for loop:")
for num in fibonacci_iterator:
    print(num)




print("\n Using next() function:")
fibonacci_iterator = Fibonacci(100)
print(next(fibonacci_iterator))
print(next(fibonacci_iterator))
print(next(fibonacci_iterator))
print(next(fibonacci_iterator))
print(next(fibonacci_iterator))
print(next(fibonacci_iterator))
print(next(fibonacci_iterator))
print(next(fibonacci_iterator))
print(next(fibonacci_iterator))
print(next(fibonacci_iterator))
print(next(fibonacci_iterator))