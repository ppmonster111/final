a = ("name", "age", "gpa")
b = ("John", 18, 3.5)

c = dict(zip(a, b))
print(c)

data = [
    ("student", "score"),
    ("A", 10),
    ("B", 20),
    ("C", 15),
    ("A", 20),
    ("B", 15),
]

summary = {}
for student, score in data[1:]:
    summary[student] = summary.get(student, 0) + score

top_border = "+" + "-" * 10 + "+" + "-" * 7 + "+"
separator = "+" + "-" * 10 + "+" + "-" * 7 + "+"

print(top_border)
print("| Student {:>8} | Score {:>5} |".format("", ""))
print(separator)

for student, score in summary.items():
    print("| {:<8} | {:<5} |".format(student, score))

print(top_border)
