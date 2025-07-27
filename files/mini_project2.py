# project1.  create a dictionary that contains a list of people and one interesting fact about each of them display each person and his or her interesting fact to the screen. next, change a fact about one of them the people . also add an additional person and corresponding fact. dispaly the new list of the people and fact . run the program multiple times and notice if the order changes.

people_facts = {
    "Albert Einstein": "He didn’t speak until he was four years old.",
    "Marie Curie": "She was the first woman to win a Nobel Prize.",
    "Nikola Tesla": "He invented the Tesla coil.",
    "Ada Lovelace": "She is considered the first computer programmer."
}

print("Original List of People and Facts:\n")
for person, fact in people_facts.items():
    print(f"{person}: {fact}")

people_facts["Nikola Tesla"] = "He had a photographic memory."

people_facts["Alan Turing"] = "He cracked the Nazi Enigma code in WWII."

print("\nUpdated List of People and Facts:\n")
for person, fact in people_facts.items():
    print(f"{person}: {fact}")


#project2. given the participants score sheet for your university sports day, you are required to find the runner-up score. you have scores. store them in a list and find the score of the runner-up score.

scores = list(map(int, input("Enter the scores separated by space: ").split()))

unique_scores = list(set(scores))

unique_scores.sort(reverse=True)

if len(unique_scores) >= 2:
    runner_up = unique_scores[1]
    print("Runner-up score is:", runner_up)
else:
    print("Not enough unique scores to determine a runner-up.")

#project3.  you have a record of n students.each record contains the students name, and their percent marks in math, physics and chemistry . the marks can be floating value . you are required to save the record in a dictionary data type.
#students name is the key . marks stired in a list is the value . the user enters a students name. output the average percentage marks obtained by that student.

student_records = {}

n = int(input("Enter number of students: "))

for i in range(n):
    name = input(f"Enter name of student {i+1}: ")
    marks = list(map(float, input(f"Enter marks in Math, Physics, Chemistry for {name} (separated by space): ").split()))
    if len(marks) != 3:
        print("Please enter exactly 3 marks!")
        exit()
    student_records[name] = marks

query_name = input("\nEnter the name of the student to get average marks: ")

if query_name in student_records:
    avg = sum(student_records[query_name]) / 3
    print(f"Average marks for {query_name} = {avg:.2f}%")
else:
    print("Student not found in the records.")


#project4. given a string of n words, help alex to find out how amny times his name apperas in the string.constraint1<=n<=200.
#sample input: hi alex welcomealexbyealex.

text = input("Enter a string (max 200 characters): ")

if 1 <= len(text) <= 200:
    count = text.count("alex")
    print(f"'alex' appears {count} time(s) in the string.")
else:
    print("Input length out of allowed range (1 to 200).")
