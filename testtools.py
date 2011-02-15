from __future__ import division

import tablib

# csv.reader and tablib aren't smart enough to read in numbers as numbers.
# Therefore, I map this over the strings in the rows spat out by csv.reader.
def str2num(string):
    import re

    if re.match('^-?\d*\.\d*$', string):
        return float(string)
    elif re.match('^-?\d+$', string):
        return int(string)
    else:
        return string


def import_raw_data(filename):
    import csv

    data = tablib.Dataset()
    for row in csv.reader(open(filename, 'r')):
        data.append( map(str2num, row) )

    data.headers = ( 'logger_id'
                   , 'day'
                   , 'hourmin'
                   , 'sec'
                   , 'needletemp'
                   , 'reftemp'
                   , 'volts'
                   , 'timer')

    return data

def unique(col):
    #get unique days
    return list(set(col))


# Time is kept in two ints: one of the form hhmm, and the other in s.
# This function converts those to absolute seconds, and rebuilds the
# table appropriately.
def hms_to_s(data):
# This bit here converts hhmm to seconds and adds to s.
# It doesn't account for changes in the julian days.
# Just don't test @ midnight, I guess.
    def convert(hourmin, sec):
        return 3600* + hourmin//100 + 60* hourmin%100 + sec

    seive = lambda st: (st != 'hourmin') and (st != 'sec')

    sec = map(lambda t: convert(t[0], t[1]), 
                   zip(data['hourmin'], data['sec']))

    new_data = zip(sec, *map( lambda h: data[h],
                               filter(seive, data.headers) ))

    new_headers = ['sec']+filter(seive, data.headers)
    return tablib.Dataset(*new_data, headers=new_headers)


def tab_filter(data, header, valfxn):

if __name__=='__main__':
    data = hms_to_s(import_raw_data('CR10_final_storage_1308.csv'))

    print unique(data['day'])

    print(data.headers)
    for row in data.data[:5]:
        print(row)
