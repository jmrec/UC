def adjust(val):
    ''' 3.0 to 3 '''
    if str(val)[-1] == '0' and str(val)[-2] == '.':
        return int(val)
    else:
        return val

lbs = 300
miles = 21
f = 9900

kg = adjust(lbs / 2.205)
km = adjust(miles * 1.609)
c = adjust((f - 32) * (5/9))

age_student1 = 22
age_student2 = 19
age_student3 = 20
age_student4 = 20
age_student5 = 18
age_student6 = 21
age_student7 = 23
age_student8 = 25
age_student9 = 19
age_student10 = 21

print(f"Weight in Pounds (lbs): {lbs}")
print(f"Weight converted to Kilograms (kg): {round(kg,2)}")
print("="*33)
print(f"Length in Miles (mi): {miles}")
print(f"Length in Kilometers (km) {round(km,2)}")
print("="*33)
print(f"Temperature in Fahrenheit (F): {f}")
print(f"Temperature in Celsius (C): {round(c,2)}")
print("="*33)

print(f"Age of Student 1: {age_student1}")
print(f"Age of Student 2: {age_student2}")
print(f"Age of Student 3: {age_student3}")
print(f"Age of Student 4: {age_student4}")
print(f"Age of Student 5: {age_student5}")
print(f"Age of Student 6: {age_student6}")
print(f"Age of Student 7: {age_student7}")
print(f"Age of Student 8: {age_student8}")
print(f"Age of Student 9: {age_student9}")
print(f"Age of Student 10: {age_student10}")
print(
    f'''The average age of the students is: {
        sum([age_student1,
             age_student2,
             age_student3,
             age_student4,
             age_student5,
             age_student6,
             age_student7,
             age_student8,
             age_student9,
             age_student10]) / 10
        }'''
    )



print("="*33)

adventurer1 = "JM"
adventurer2 = "Sean"
mentor = "Johnny Sins"
mentor_exp1 = "Doctor"
mentor_exp2 = "Lawyer"
mentor_exp3 = "Plumber"
mentor_exp4 = "Astronaut"
mentor_exp5 = "Gamer"
ability1 = "rizz"
ability2 = "Talk no Jutsu"
location = "M304"
rizz_count = {
    adventurer1: 8,
    adventurer2: 30,
}

print(
f'''It's another day at {location}. Two gentlemen, {adventurer1} and {adventurer2}, wanted to know how many ladies they can use their {ability1} on.
{adventurer1} came up first using his exceptional {ability2}! He {ability1}ed not 1, not 2, but {rizz_count[adventurer1]} ladies!

Next, it's {adventurer2}'s turn. But {adventurer2} came prepared. He recently trained with his mentor, the great {mentor}. {adventurer2}'s {ability1}
was maximized after learning from Mr. {mentor.split()[1]}' accumulated wisdom in being a {mentor_exp1}, {mentor_exp2}, {mentor_exp3}, {mentor_exp4}, and {mentor_exp5}.
He {ability1}ed not 5, not 10, not 20, but {rizz_count[adventurer2]} ladies!

{adventurer2} blew away the competition.'''
)