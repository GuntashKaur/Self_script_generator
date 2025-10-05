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
