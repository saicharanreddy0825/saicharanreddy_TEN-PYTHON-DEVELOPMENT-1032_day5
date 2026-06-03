fruits = ['apple', 'banana', 'mango']

fruits[0] = 'cherry'  # ✅ works!

fruits.append('grape')  # ✅ OK

print(fruits)

# ['cherry','banana','mango','grape']


coords = (10, 20, 30)

# coords[0] = 99 ← TypeError!

# Cannot modify a tuple

name = 'Python'

# name[0] = 'J' ← TypeError!

name = 'JPython'  # creates NEW str

# ── Creating Lists ─────────────────────────────────────────────

empty = []                          # empty list

nums = [10, 20, 30, 40, 50]         # integers

mixed = [1, "hello", 3.14, True]    # mixed types

nested = [[1, 2], [3, 4], [5, 6]]   # nested list

from_range = list(range(1, 6))      # [1, 2, 3, 4, 5]


# ── Indexing & Slicing ─────────────────────────────────────

print(nums[0])      # 10 (first element)

print(nums[-1])     # 50 (last element)

print(nums[1:4])    # [20, 30, 40] (index 1 to 3)

print(nums[:3])     # [10, 20, 30] (first 3)

print(nums[2:])     # [30, 40, 50] (from index 2)

print(nums[::2])    # [10, 30, 50] (every 2nd element)

print(nums[::-1])   # [50, 40, 30, 20, 10] (reversed)

# Syntax: list[start : stop : step]

fruits.append('mango')          # ['apple','banana','mango']
fruits.remove('banana')         # removes 'banana'
fruits.extend(['grape', 'kiwi'])  # adds 2 items
last = fruits.pop()             # removes & returns last
fruits.insert(1, 'cherry')      # inserts at index 1
fruits.clear()                  # []


nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

# count() — frequency of a value

print(nums.count(1))    # 2 (1 appears twice)

print(nums.count(5))    # 2

# index() — first occurrence position

print(nums.index(9))    # 5 (9 is at index 5)

print(nums.index(4))    # 2

# sort() — sorts in-place (modifies list directly)

nums.sort()                 # ascending: [1,1,2,3,3,4,5,5,6,9]

nums.sort(reverse=True)     # descending: [9,6,5,5,4,3,3,2,1,1]

# reverse() — reverses list in-place

nums.reverse()              # flips current order

# copy() — shallow copy (independent list, same inner values)

a = [1, 2, 3]

b = a.copy()    # b is a NEW list; modifying b won't affect a

b.append(99)

print(a)    # [1, 2, 3] <-- unchanged

print(b)    # [1, 2, 3, 99]

# len(), min(), max(), sum() — built-ins work on lists

print(len(nums), min(nums), max(nums), sum(nums))

# ── BASIC: squares of 1–10 ─────────────────────────────────────────────

squares = [x**2 for x in range(1, 11)]

# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# ── WITH CONDITION: even numbers only ──────────────────────────────────

evens = [x for x in range(1, 21) if x % 2 == 0]

# [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# ── TRANSFORMATION: uppercase names ────────────────────────────────────

names = ['alice', 'bob', 'charlie']

upper = [name.upper() for name in names]

# ['ALICE', 'BOB', 'CHARLIE']

# ── NESTED COMPREHENSION: flatten 2D list ──────────────────────────────

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

flat = [num for row in matrix for num in row]

# [1, 2, 3, 4, 5, 6, 7, 8, 9]

# ── EQUIVALENT for-loop (what comprehension replaces) ──────────────────


# ── Creating Tuples ────────────────────────────────────────────────────

empty = ()                          # empty tuple

single = (42,)                      # ← COMMA required for 1-element tuple!

point = (10, 20)                    # 2D coordinate

rgb = (255, 128, 0)                 # RGB color

record = ("Alice", 22, "Jaipur")    # mixed types

packed = 1, 2, 3                    # parentheses optional (tuple packing)

# ── Tuple Packing & Unpacking ────────────────────────────────────────

person = ("Bob", 25, "Engineer")    # packing: 3 values → 1 tuple

name, age, job = person             # unpacking: 1 tuple → 3 variables

print(name)     # Bob

print(age)      # 25

# ── Extended unpacking with * ────────────────────────────────────────────

first, *rest = (1, 2, 3, 4, 5)

print(first)    # 1

print(rest)     # [2, 3, 4, 5]

# ── Swap variables using tuple (Pythonic trick) ──────────────────────────

a, b = 10, 20

a, b = b, a     # swap! No temp variable needed

print(a, b)     # 20 10


# ── Creating Sets ───────────────────────────────────

empty = set()                       # NOT {} (that's a dict!)

nums = {1, 2, 3, 4, 5}

mixed = {1, "hello", 3.14}

no_dup = {1, 2, 2, 3, 3, 3}        # → {1, 2, 3} duplicates removed!

# ── Adding Elements ──────────────────────────────────

s = {10, 20, 30}

s.add(40)               # add single item → {10,20,30,40}

s.update([50, 60, 70])  # add multiple → {10,20,30,40,50,60,70}

# ── Removing Elements ───────────────────────────────

s.remove(10)    # removes 10; raises KeyError if missing

s.discard(99)   # removes 99 if present; NO error if missing (safer)

s.pop()         # removes & returns a RANDOM element (sets are unordered)

# ── Membership Testing (very fast — O(1)) ───────────

print(3 in nums)        # True

print(9 not in nums)    # True


# ── Creating Dictionaries ─────────────────────────────────────────────

empty = {}  # empty dict

student = {"name": "Alice", "age": 20, "gpa": 3.8}

prices = dict(apple=30, banana=10, mango=50)    # using dict()

squares = {x: x**2 for x in range(1, 6)}        # dict comprehension

# ── Accessing Values ──────────────────────────────────────────────────

print(student["name"])          # "Alice" — direct access

print(student.get("age"))       # 20 — safe access

print(student.get("cgpa", 0))   # 0 — default if key missing

# student["phone"] → KeyError! Use .get() for safety

# ── Adding & Updating ─────────────────────────────────────────────────

student["email"] = "alice@python.com"           # add new key-value

student["age"] = 21                             # update existing key

student.update({"age": 22, "city": "Jaipur"})  # update multiple at once


# ── Removing Items ─────────────────────────────────────────────────

val = student.pop("email")      # removes "email" key, returns value

item = student.popitem()        # removes & returns LAST inserted (key, val)

del student["city"]             # removes "city" key (no return value)

student.clear()                 # removes ALL key-value pairs → {}


# ── Nested Dictionary ─────────────────────────────────────────────────────

students = {
    "S001": {"name": "Alice",   "marks": {"Math": 95, "Science": 88, "English": 76}},
    "S002": {"name": "Bob",     "marks": {"Math": 72, "Science": 91, "English": 83}},
    "S003": {"name": "Charlie", "marks": {"Math": 85, "Science": 79, "English": 90}},
}

# Accessing nested values

print(students["S001"]["name"])                 # Alice

print(students["S002"]["marks"]["Science"])     # 91

# Iterating over nested dict

for sid, info in students.items():
    avg = sum(info["marks"].values()) / len(info["marks"])
    print(f"{info['name']} ({sid}) Avg: {avg:.1f}")

# Output:

# Alice (S001) Avg: 86.3

# Bob (S002) Avg: 82.0

# Charlie (S003) Avg: 84.7

# ── Dictionary Comprehension ────────────────────────────────────────────────

# Create dict of name → average marks

averages = {
    info["name"]: sum(info["marks"].values()) / len(info["marks"])
    for sid, info in students.items()
}

# {'Alice': 86.33, 'Bob': 82.0, 'Charlie': 84.67}

# ── Membership Testing ──────────────────────────────────────────────

fruits = ["apple", "banana", "mango", "grape"]

print("mango" in fruits)        # True — O(n) for list

print("orange" not in fruits)   # True

scores = {90, 85, 72, 95, 60}

print(85 in scores)             # True — O(1) for set ⚡

# ── sorted() — returns NEW sorted list (original unchanged) ─────────

nums = [5, 2, 8, 1, 9, 3]

asc = sorted(nums)                  # [1, 2, 3, 5, 8, 9]

desc = sorted(nums, reverse=True)   # [9, 8, 5, 3, 2, 1]

print(nums)                         # [5,2,8,1,9,3] ← original unchanged
