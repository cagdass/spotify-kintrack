from datetime import datetime
import os

# Always assume there are 6 people in the family so people pay the minimum amount.
num_people = 6

# List of changes in pricing, with the date of the change and the total amount for the family.
# In reverse chronological order, new first old last.
price_changes = [(datetime(2017,4,25), 21.0), (datetime(1977,1,1), 15.0)]

# Return the difference of months between two dates.
# If the later date's number of days is fewer, then round down the number of months in between.
def diff_month(now, start):
    if now.day >= start.day:
        return (now.year - start.year)*12 + now.month - start.month
    else:
        return (now.year - start.year)*12 + now.month - start.month - 1

# Return the total fee owed with respect to the price change.
def combine_pricing(now, start):
    # Initialization stuff.
    counter = 0
    amount_owed = 0
    (cur_date, cur_price) = price_changes[counter]
    # Find the first date that comes before the end of subscription (the present day if the subscription is in effect)
    while diff_month(now, cur_date) < 0 and counter + 1 < price_changes.__len__():
        counter += 1
        (cur_date, cur_price) = price_changes[counter]

    # Update the total amount owed by multiplying the number of months while the subscription was in effect
    # with the per person price at the time. Always assume there had been 6 people in the family,
    # Better safe than sorry.
    for i in xrange(counter, len(price_changes)):
        (cur_date, cur_price) = price_changes[i]
        will_break = False
        # If the date when this pricing period started comes before the current user's subscription,
        # Replace the current date with their start date.
        if diff_month(start, cur_date) > 0:
            # The period where the subscription began was found, no need to check the prices before this.
            cur_date = start
            will_break = True
        # Update the total amount owed.
        amount_owed += diff_month(now, cur_date) * (cur_price/num_people)
        now = cur_date
        if will_break:
            break

    return amount_owed

def read_file(filename='spotify.log'):
    pwd = os.path.dirname(os.path.realpath(__file__)) + '/'
    return open(pwd + filename).read()

def process_date(date):
    date = date.split("-")
    if date.__len__() != 3:
        return datetime.now()
    else:
        return datetime(int(date[2]), int(date[1]), int(date[0]))


def process_user(user):
    user["Start Date"] = process_date(user["Start Date"])
    user['End Date'] = process_date(user['End Date'])
    user['Amount Paid'] = float(user['Amount Paid'])
    return user

def get_data(contents):
    lines = contents.split('\n')
    fields = lines[0].split(';')
    users = []
    for i in xrange(1, len(lines)):
        cur_user = {}
        cur_line = lines[i].split(';')
        for j in xrange(len(fields)):
            if (len(cur_line) != len(fields)):
                break
            cur_user[fields[j]] = cur_line[j]
        if len(cur_user.keys()) > 0:
            cur_user = process_user(cur_user)
            users.append(cur_user)

    return users



data = get_data(read_file())
now = datetime.now()

for user in data:
    print 'Name: {}, Amount Owed: {}TL'.format(user['Name'], combine_pricing(user['End Date'], user['Start Date']) - user['Amount Paid'])
