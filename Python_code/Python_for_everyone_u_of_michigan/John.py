h = int(input('Number of hours>'))
m = int(input('Number of minutes>'))
s = int(input('Number of seconds.'))
total = 60*60*h + 60*m + s
print (f'{h} hour(s), {m} minute(s) and {s} second(s) equal {total} second(s), or {total/60} minute(s), or {total/60/60} hour(s)')
