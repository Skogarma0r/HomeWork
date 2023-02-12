s = input("Enter your text here: ")
let_b = 0
for i in s:
    if 'A' <= i <= 'Z':
        let_b += 1

print(f"Count of capital letters: {let_b}")
