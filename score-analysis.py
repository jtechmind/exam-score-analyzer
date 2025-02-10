import numpy as np


# Generate Random Exam Scores
# 50 Student, 3 Exams size=(50, 3)
def generate_scores():
    return np.random.randint(40, 100, size=(50, 3))


# Basic score analysis using NumPy
def analyse_scores(scores):
    print('Basic Statistics:')
    print(f'Average Score Per Exam: {np.mean(scores, axis=0)}')
    print(f'Highest Score Per Exam: {np.max(scores, axis=0)}')
    print(f'Lowest Score Per Exam: {np.min(scores, axis=0)}')
    print(f'Standard Deviation Per Exam: {np.std(scores, axis=0)}')


# Apply 5-point curve to scores
def apply_curves(scores):
    return np.clip(scores + 5, 0, 100)


# Main function
def main():
    # Generate and save raw scores
    raw_score = generate_scores()
    np.savetxt('data/raw_score.csv', raw_score, delimiter=',', fmt='%d')

    # Analyze Raw Scores
    print("=== Raw Scores Analysis ===")
    analyse_scores(raw_score)

    # Apply Curve and save curved scores
    curved_scores = apply_curves(raw_score)
    np.savetxt('data/curved_score.csv', curved_scores, delimiter=',', fmt='%d')

    # Analyzed Curved Scores
    print("=== Curved Scores Analysis ===")
    analyse_scores(curved_scores)


if __name__ == "__main__":
    main()
