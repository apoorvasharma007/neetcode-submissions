from typing import List, Tuple


def best_student(scores: List[Tuple[str, int]]) -> str:
    max_name = str()
    max_marks = 0
    for score in scores:
        student, marks = score
        if marks>max_marks:
            max_name=student
            max_marks=marks
    return max_name

# do not modify below this line
print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 70)]))
print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 100)]))
print(best_student([("Alice", 90), ("Bob", 100), ("Charlie", 70)]))
print(best_student([("Alice", 90), ("Bob", 90), ("Charlie", 80), ("David", 100)]))
