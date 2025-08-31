greeting = input("Enter a message: ").lower()

if greeting.startswith("hello"):
    output = 0
elif greeting.startswith("h"):
    output = 20
else:
    output = 100

print(f"Output: ${output}")
