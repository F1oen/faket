def calculate_weighted_grade(units):
    total_weight = 0
    total_score = 0
    for units, mark, weight in units:
        total_weight += weight
        total_score += mark * (weight / 100)  
    return total_score


def gradefromscore(score):
    if score >= 70:
        return "Distinction"
    elif score >= 60:
        return "Merit"
    elif score >= 50:
        return "Pass"
    else:
        return "Fail"


def read_input_file(input_filename):
    students = {}
    with open(input_filename, "r") as file:
        for line in file:
            parts = line.strip().split(",")               
            name, unit, mark, weight = parts
            if name not in students:
                students[name] = []
            students[name].append((unit, float(mark), float(weight)))  # mark and weight to float
    return students


def write_output_file(output_filename, results):
    with open(output_filename, "w") as file:
        for name, (score, grade) in results.items():  # Fix unpacking of results
            file.write(f"{name}, {score:.2f}, {grade}\n") 


def main():
    input_filename = "input.txt"
    output_filename = "output.txt"

    try:
       
        students = read_input_file(input_filename)
        results = {}
        
        
        for name, entries in students.items():  # Fix `iteams()` typo to `items()`
            score = calculate_weighted_grade(entries)
            grade = gradefromscore(score)  # Fix function call to `grade_from_score`
            results[name] = (score, grade)

        #write a results in terminal
        write_output_file(output_filename, results)
        print(f"Results were written to this file --> {output_filename}")
    except Exception as e:
        print(e)
        print("Error,you need to creat a input.txt file")

if __name__ == "__main__":
      main()
