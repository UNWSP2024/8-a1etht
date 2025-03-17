# Programmer: Alethea Lo
# Date: 3/16/25
# Title: Pseudocode for Course Info

#BEGIN OF PROGRAM
    DECLARE course_name AS STRING
    DECLARE course_code AS STRING
    DECLARE instructor AS STRING
    DECLARE num_credits AS INTEGER
    DECLARE schedule AS STRING

    // Get course details from user
    DISPLAY "Enter course name: "
    INPUT course_name

    DISPLAY "Enter course code: "
    INPUT course_code

    DISPLAY "Enter instructor's name: "
    INPUT instructor

    DISPLAY "Enter number of credits: "
    INPUT num_credits

    DISPLAY "Enter course schedule (e.g., Mon/Wed 10 AM): "
    INPUT schedule

    // Display the course information
    DISPLAY "Course Information:"
    DISPLAY "Course Name: " + course_name
    DISPLAY "Course Code: " + course_code
    DISPLAY "Instructor: " + instructor
    DISPLAY "Credits: " + num_credits
    DISPLAY "Schedule: " + schedule
#END OF PROGRAM