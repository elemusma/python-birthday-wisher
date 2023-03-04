import smtplib
import datetime as dt
import random
import pandas as pd

# quotes = pd.read_csv('quotes.txt')
# quotes.to_csv('quotes.csv', index=False)


with open('quotes.txt') as quote_file:
    all_quotes = quote_file.readlines()
    quote = random.choice(all_quotes)

print(quote)
print(len(all_quotes))

# random_num = random.randint(0, len(all_quotes))
# print(quotes.loc[random_num])
# print(len(quotes))

my_email = 'tadeoycuba@gmail.com'
password= 'xvridyweuezyoabb'
msg = quote

now = dt.datetime.now()
year = now.year
month = now.month
weekday = now.weekday()

# # with smtplib.SMTP('smtp.mail.yahoo.com') as connection:
if weekday == 5:
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email, 
            to_addrs='tadeoycuba@yahoo.com', 
            msg=f'Subject:Monday Motivation\n{msg}')





# print(weekday)
date_of_birth = dt.datetime(year=1996, month=8, day=23, hour=14)
# print(date_of_birth)