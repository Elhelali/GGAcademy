import datetime, time, calendar



today=str(datetime.date.today()) #whole date 27-05-2019
year_today= today[0:4] # 2019
month_today=today[5:7] # 5
day_today = today[8:] #"27"


nextmonth_today = int(month_today)+1
if nextmonth_today == 13 :
	nextmonth_today = 1

monthlycal=calendar.monthcalendar(int(year_today), int(month_today)) #
nextmonthlycal=calendar.monthcalendar(int(year_today), int(nextmonth_today))

	



  

def month_name(strmonth):
	""" returns monthname when given month no."""

	dictitionary = {
	'01':'Jan',
	'02':'Feb',
	'03':'Mar',
	'04':'Apr',
	'05': 'May',
	'06': 'Jun',
	'07': 'Jul',
	'08': 'Aug',
	'09':'Sep',
	'10': 'Oct',
	'11': 'Nov',
	'12': 'Dec',
	}
	monthname = dictitionary [strmonth]
	
	return monthname

def monthdays (year_today,month_today):
	monthlycal = calendar.monthcalendar(year_today, month_today)
	
	x=[]
	for week in monthlycal:
		y=week
		for days in y:
			x.append(days)


	return (x) 


def thismonthdays(): # List to Only make URLs for days after today. Cant book in the past.
	days = monthdays(int(year_today),int(month_today))
	x=[]
	for day in days:
		if day > int(day_today):
			x.append(day)
	return x 

