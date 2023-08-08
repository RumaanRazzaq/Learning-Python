# Write your solution here
def histogram(string: str):
    groups = {}
    for char in string:
        if char not in groups:
            groups[char] = 0
        groups[char] += 1
    for key in groups:
        print(f"{key}", groups[key] * "*")

if __name__ == "__main__":
    histogram("statistically")