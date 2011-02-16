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
        return 60*(hourmin%100) + sec #+ 3600*(hourmin//100 )

    def sieve(st):
        return (st != 'hourmin') and (st != 'sec')

    sec = map(lambda t: convert(t[0], t[1]), 
                   zip(data['hourmin'], data['sec']))

    new_data = zip(sec, *map( lambda h: data[h],
                               filter(sieve, data.headers) ))
    new_headers = ['sec']+filter(sieve, data.headers)
    return tablib.Dataset(*new_data, headers=new_headers)


#Untested.
def tab_filter(data, header, testfxn):
    new_data = [];
    for (i, pt) in enumerate(data[header]):
        if testfxn(pt):
            new_data.append(data[i])
    return tablib.Dataset(*new_data, headers=data.headers)

def tab_pprint(data):
    width = 2 + max(map(lambda st: len(st), data.headers))

    def padder(st):
        l = len(str(st))
        return st + (width-l)*" " if l <= width else st[:width]

    print " | ".join(map(padder,data.headers))
    print "-"*((width+2)*len(data.headers)-1)
    for row in data:
        print " | ".join(map(padder,map(str,row)))

#Untested.
def tab_plot(data, x_header, y_headers = None ):
    import matplotlib.pyplot as pyplot

    headers = filter(lambda h: h != x_header, data.headers if y_headers == None else y_headers)

    xs = [ data[x_header] for i in range(len(headers)) ]
    ys = [ data[header] for header in headers]

    pyplot.plot(*reduce(lambda a, b: a+b, zip(xs,ys)))
    pyplot.xlabel(x_header)
    pyplot.ylabel('Everything Else')
    pyplot.show()
    return data


if __name__=='__main__':

    #note2self:
    # > import datetime
    # > datetime.date.fromordinal(44)
    # datetime.date(1, 2, 13)
    # > datetime.toordinal(_)
    # 44

    data = tab_filter(hms_to_s(import_raw_data('CR10_final_storage_1308.csv')),
                      'day',
                      lambda dy: dy==44)

    tab_pprint(data)

    #tab_plot(data, 'sec', ["needletemp", "reftemp"])
