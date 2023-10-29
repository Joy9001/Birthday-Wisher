import random
import smtplib
import datetime as dt
import pandas

# MY DETAILS
my_gmail = "putyouremail.com"
password_gmail = "create your gmail app password"

# CHOOSING THE LETTER

file_name = f"./letters/letter-{random.randint(1, 3)}.txt"
letter = pandas.read_csv(file_name, delimiter='\t', header=None).to_dict(orient="list")

# READING THE BIRTHDAYS
data = pandas.read_csv("birthdays.csv")
birthdays = {}
for (index, row) in data.iterrows():
    key = (row['month'], row['day'])
    value = {
        'name': row['name'],
        'email': row['email']
    }
    birthdays[key] = value

# FINDING WHOM TO WISH
today = dt.datetime.now()
month = today.month
day = today.day
name_to_wish = ""
email_to_wish = ""

if (month, day) in birthdays:
    name_to_wish = birthdays[(month, day)]['name']
    email_to_wish = birthdays[(month, day)]['email']

    # CREATING THE MESSAGE
    first_line = letter[0][0]
    new_line = first_line.replace("[Name]", name_to_wish)
    letter[0][0] = new_line
    message = "\n\n".join(letter[0])

    # SENDING THE MAIL
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_gmail, password=password_gmail)
        connection.sendmail(to_addrs=email_to_wish, from_addr=my_gmail, msg=f"Subject: Birthday Wish\n\n{message}")
