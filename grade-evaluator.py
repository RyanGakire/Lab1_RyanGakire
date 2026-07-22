import csv
import sys
import os

def load_csv_data():
    """
    Prompts the user for a filename, checks if it exists, 
    and extracts all fields into a list of dictionaries.
    """
    filename = input("Enter the name of the CSV file to process (e.g., grades.csv): ")
    
    if not os.path.exists(filename):
        print(f"Error: The file '{filename}' was not found.")
        sys.exit(1)
        
    assignments = []
    
    try:
        with open(filename, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Convert numeric fields to floats for calculations
                assignments.append({
                    'assignment': row['assignment'],
                    'group': row['group'],
                    'score': float(row['score']),
                    'weight': float(row['weight'])
                })
        return assignments
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        sys.exit(1)

def evaluate_grades(data):
    """
    Implement your logic here.
    'data' is a list of dictionaries containing the assignment records.
    """
    print("\n--- Processing Grades ---")
    
    # a) Check if all scores are percentage based (0-100)
    invalid_scores = [item for item in data if item['score'] < 0 or item['score'] > 100]
    if invalid_scores:
        print("Error: One or more scores are outside the 0-100 range.")
        for item in invalid_scores:
            print(f"  - {item['assignment']} ({item['group']}): {item['score']}")
        sys.exit(1)

    print("All scores are percentage-based and within the 0-100 range.")

    # b) Validate total weights (Total=100, Summative=40, Formative=60)
    total_weight = sum(item['weight'] for item in data)
    summative_weight = sum(item['weight'] for item in data if item['group'].lower() == 'summative')
    formative_weight = sum(item['weight'] for item in data if item['group'].lower() == 'formative')

    # Allow tiny floating point tolerance
    tol = 1e-6
    errors = []
    if abs(total_weight - 100.0) > tol:
        errors.append(f"Total weight must be 100 but is {total_weight}.")
    if abs(summative_weight - 40.0) > tol:
        errors.append(f"Summative weight must be 40 but is {summative_weight}.")
    if abs(formative_weight - 60.0) > tol:
        errors.append(f"Formative weight must be 60 but is {formative_weight}.")

    if errors:
        print("Error: Invalid weighting configuration:")
        for e in errors:
            print(f"  - {e}")
        sys.exit(1)

    print("Weights validated: Total=100, Summative=40, Formative=60.")

    # c) Calculate the Final Grade and GPA
    final_grade = sum(item['score'] * item['weight'] / 100.0 for item in data)

    def grade_to_gpa(grade):
        if grade >= 90.0:
            return 4.0
        if grade >= 80.0:
            return 3.0
        if grade >= 70.0:
            return 2.0
        if grade >= 60.0:
            return 1.0
        return 0.0

    gpa = grade_to_gpa(final_grade)
    print(f"Final grade: {final_grade:.2f}%")
    print(f"GPA equivalent: {gpa:.1f}")
    # TODO: d) Determine Pass/Fail status (>= 50% in BOTH categories)
    # TODO: e) Check for failed formative assignments (< 50%)
    #          and determine which one(s) have the highest weight for resubmission.
    # TODO: f) Print the final decision (PASSED / FAILED) and resubmission options

if __name__ == "__main__":
    # 1. Load the data
    course_data = load_csv_data()
    
    # 2. Process the features
    evaluate_grades(course_data)