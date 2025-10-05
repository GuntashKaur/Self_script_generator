"""
 Challenge: Self-Intro Script Generator

Create a Python script that interacts with the user and generates a personalized self-introduction.

Your program should:
1. Ask the user for their name, age, city, profession, and favorite hobby.
2. Format this data into a warm, friendly paragraph of self-introduction.
3. Print the final paragraph in a clean and readable format.

Example:
If the user inputs:
  Name: Priya
  Age: 22
  City: Jaipur
  Profession: Software Developer
  Hobby: playing guitar

Your script might output:
  "Hello! My name is Priya. I'm 22 years old and live in Jaipur. I work as a Software Developer and I absolutely enjoy playing guitar in my free time. Nice to meet you!"

Bonus:
- Add the current date to the end of the paragraph like: "Logged on: 2025-06-14"
- Wrap the printed message with a decorative border of stars (*)
"""

import datetime

name = input("What is your name? ").strip()
age = input("What is your age? ") .strip()
city = input("Which city do you live in? ").strip()
profession = input("What is your profession? ").strip()
hobby = input("What is your hobby? ").strip()

intro_message = (f"Hi, my name is {name}. I’m {age} years old and from {city}. I work as a {profession}, and my hobby is {hobby}. Nice to meet you!")

add_date = datetime.date.today().isoformat()

final_message =  f"\n Logged in: {add_date} \n \n {intro_message}"

border = "*"
print_border = border*20

message_with_border = f"\n {print_border} \n {final_message} \n \n {print_border}"

print(message_with_border)