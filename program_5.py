#Programmer: Alethea Lo
#Date: 3/16/25
#Title: Course Info

def get_courses():
    courses = {}
    while True:
        course_id = input("Enter course ID (or 'done' to finish): ")
        if course_id.lower() == 'done':
            break
        course_name = input("Enter course name: ")
        courses[course_id] = course_name
    return courses

def filter_courses_by_subject(courses, subject):
    print(f"\nCourses under subject '{subject}':")
    found = False
    for course_id, course_name in courses.items():
        if course_id.startswith(subject):
            print(f"{course_id}: {course_name}")
            found = True
    if not found:
        print("No courses found for this subject.")

#Course details from user
course_data = get_courses()

#Subject Filter
subject_filter = input("\nEnter a subject code to filter courses (e.g., 'COS'): ")

#Displaying matching results
filter_courses_by_subject(course_data, subject_filter)