# Abbas Salim
# 2026396
def find(input_date):
    month_dict = {"January": 1, "February": 2, "March": 3, "April": 4,
                  "May": 5, "June": 6, "July": 7, "August": 8, "September": 9,
                  "October": 10, "November": 11, "December": 12}

    from datetime import date
    today = date.today()

    try:
        date_and_year = input_date.split(', ')
        month_and_day = date_and_year[0].split(' ')

        month = month_and_day[0]
        day = int(month_and_day[1].rstrip(','))
        year = int(date_and_year[1])

        month_num = int(month_dict[month])
        date_input = date(year, month_num, day)

        if date_input <= today:
            return str(month_num) + '/' + str(day) + '/' + str(year)
    except (IndexError, KeyError, ValueError):
        pass

with open('inputDates.txt') as f:
    for date in f.readlines():
        if date.strip() != '-1':
            parsed_date = find(date.strip())
            if parsed_date is not None:
                with open('parsedDates.txt', 'w') as nf:
                    nf.write(parsed_date + '\n')
