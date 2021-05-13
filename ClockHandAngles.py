# -*- coding: utf-8 -*-

ip = '3:27'
#ip = input('Enter Time (hh:mm): ')
try:
    hrs, mins = map(int, ip.split(':'))
except:
    print('Please enter a valid time')

if hrs > 24 or mins > 59:
    raise Exception('Please enter a valid time')

if hrs > 12:
    hrs -= 12
hrs *= 30
mins *= 6
hrs += (mins/12) # This will give the precise angle of hours hand

print('Angle of hands: {}° : {}°'.format(hrs, mins))
print('Angle between hands: {}°'.format(abs(mins - hrs)))
