#David Mamaril Horowitz
#June 6, 2023
#Homework 1

#define birth_year
birth_year = input("What is your year of birth?")
#In the PINJFU tutorial, I was lazy and just added the "int" function to modify "input." But I remember that Soma did the following, instead:
birth_year = int(birth_year)

#Here's if they're from the future ... and then, in the event they give a correct DOB the second time, I need to convert the string to an integer a secondtime.
if birth_year >= 2023:
    birth_year = input("You can't be zero years old. What is your year of birth?")
    birth_year = int(birth_year)

age = (2023 - birth_year)
print(f'You are approximately {age} years old, assuming that your birthday has passed.')

#The typical adult heart rate is 60-100 BPM, so, for the purpose of this exercise, we can use a middle value of 80 BPM
#Additionally, the instructions say to use "millions," but unless I'm mistaken, "billions" seems to make more sense
bpm = 80
#The formula for heartbeats per lifetime is 365 * 24 * 60 * BPM
heartbeats = (age * 365 * 24 * 60 * bpm)
print(f'Your heart has beaten roughly {round(heartbeats / 1000000000, 2)} billion times.')

#A blue whale was found to have a heart rate of about 11 BPM, according to The Atlantic.
whale_bpm = 11
#Let's use the same formula for heartbeats but replace the BPM with the whale BPM
whale_heartbeats = (age * 365 * 24 * 60 * whale_bpm)
print(f"A blue whale's heart beat about {round(whale_heartbeats / 1000000, 2)} million times in that period.")

#A rabbit's resting heart rate should be 120-150 BPM, according to the House Rabbit Society; let's get the average.
rabbit_bpm = (120 + 150) / 2
#We're using the same formula for heartbeats
rabbit_heartbeats = (age * 365 * 24 * 60 * rabbit_bpm)
print(f"A rabbit's heart beat about {round(rabbit_heartbeats / 1000000000, 2)} billion times in that period.")

#A year on Earth is 0.615 years in Venus. Divide their age by 0.615 to get the Venus year.
print(f'You are {round(age / 0.615, 2)} years old in Venus years.')

#A year on Earth is 165 years on Neptune. Divide their age by 165 to get their Neptune age. Multiply by 12 to get it in months.
print(f'You are {round(age / 165 * 12, 2)} months old in Neptunian time.')

#We've got to add one year to my age because my birthday hasn't happened yet this year.
david_age = 30
if (age - david_age) == 1:
    print("You're one year older than David.")
elif age > david_age:
    print(f"You're {age - david_age} years older than David.")
elif (david_age - age) == 1:
    print("You're one year younger than David.")
elif age < david_age:
    print(f"You're {david_age - age} years younger than David.")
elif age == david_age:
    print(f"You're the same age as David!")

if birth_year % 2 == 0:
    print("You were born in an even year.")
else:
    print("You were born in an odd year.")

#There have been six presidents from the Democratic Party since 1960. For each that has served two terms, the terms have been consecutive, so for the next question, what's important is the year that each president was sworn in. Technically, I could have avoided using a range. It would have been simpler. But I need to type out the full range for the next question, anyways, so I might as well type it correctly the first time so I can just copy and paste it for the next problem.
count = 0
democratic_presidents = {
    'John F. Kennedy' : range(1961, 1963), 
    'Lyndon B. Johnson' : range(1963, 1969), 
    'Jimmy Carter' : range(1977, 1981), 
    'Bill Clinton' : range(1993, 2001), 
    'Barack Obama' : range(2009, 2017), 
    'Joe Biden' : range(2021, 2023)
}

for president in democratic_presidents.values():
  if birth_year <= president[0]:
    count = count + 1

if count == 1:
    print(f'There has been one president since you were born.')
else:
    print(f'There have been {count} presidents from the Democratic Party since you were born.')

all_presidents = {
    'Dwight D. Eisenhower' : range(1953, 1961),
    'John F. Kennedy' : range(1961, 1963),
    'Lyndon B. Johnson' : range(1963, 1969),
    'Richard M. Nixon' : range(1969, 1974),
    'Gerald R. Ford' : range(1974, 1977),
    'Jimmy Carter' : range(1977, 1981),
    'Ronald Reagan' : range(1981, 1989),
    'George Bush, Sr.' : range(1989, 1993),
    'Bill Clinton' : range(1993, 2001),
    'George W. Bush' : range(2001, 2009),
    'Barack Obama' : range(2009, 2017),
    'Donald J. Trump' : range(2017, 2021),
    'Joseph R. Biden' : range(2021, 2023)
    }
#This was extremely tricky and took a long, long time. For the value of each president within all_presidents, I need to search for the birth year. This is difficult because I need to get the range value for each key. I also had to learn about the "in" function.
for president_name in all_presidents.keys():
    if birth_year in all_presidents[president_name]:
        print(f'{president_name} was the president when you were born.')
