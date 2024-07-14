#!/usr/bin/python #!/usr/bin/python

import os
import os.path
import shutil
import sys
from datetime import datetime, timedelta
from pathlib import Path

import markdown2
import pytz
import yaml
from icalendar import Calendar, Event, vCalAddress, vText

from render import PageRendered, _read

# init the calendar
cal = Calendar()
cal.add('prodid', 'ical_gen')
cal.add('version', "2.0" )

SLOTS_META = {}

def define_slot(id, start, minutes, kind=None):
    global SLOTS_META, LE 
    if isinstance(start, str):
        s = datetime.fromisoformat(start)
    else:
        s = start
    e = s + timedelta(minutes=minutes)
    LE = e
    SLOTS_META[id] = (s, e, kind)

LE = None
def create_break(title, start, minutes):
    global LE
    if isinstance(start, str):
        s = datetime.fromisoformat(start)
    else:
        s = start

    e = s + timedelta(minutes=minutes)
    LE = e

    # Add subcomponents
    event = Event()
    event.add("uid", hash(title))
    event.add("dtstamp", datetime.now())

    event.add('summary', title)
    #event.add('description', c)

    event.add('dtstart', s)
    event.add('dtend', e)

    # Add the organizer
    organizer = vCalAddress('MAILTO:weigl@kit.edu')
    # Add parameters of the event
    organizer.params['name'] = vText('Alexander Weigl')
    organizer.params['role'] = vText('Program Chair')
    event['organizer'] = organizer
    event['location'] = vText('Bad Herrenalb, Germany')
    cal.add_component(event)

day0 = lambda x: f'2024-07-29T{x}:00+02:00'
day1 = lambda x: f'2024-07-30T{x}:00+02:00'
day2 = lambda x: f'2024-07-31T{x}:00+02:00'
day3 = lambda x: f'2024-08-01T{x}:00+02:00'

C_SOCIAL = 'blue'
C_BREAK = 'grey'
C_INVITED = 'red'
C_KEY = 'turkoise'
C_KEYM = 'lightblue'

define_slot(999, day0('13:00'), 60*5, C_SOCIAL)
define_slot(998, day1('19:00'), 120,  C_SOCIAL)

create_break('Coffee Break', day1('10:30'), 30)
create_break('Lunch', day1('12:30'), 30)
create_break('Coffee Break', day1('15:30'), 30)
#
create_break('Coffee Break', day2('10:30'), 30)
create_break('Lunch', day2('12:30'), 30)
create_break('Coffee Break', day2('15:30'), 30)
#
create_break('Coffee Break', day3('10:30'), 30)
create_break('Lunch', day3('12:30'), 30)

define_slot(10, day1('08:45'), 15)
define_slot(11, LE, 60)
define_slot(12, LE, 15)
define_slot(123, LE, 15)

define_slot(113, day1('11:00'), 30)
define_slot(114, LE, 30)
define_slot(115, LE, 30)

define_slot(213, day1('11:00'), 30)
define_slot(214, LE, 30)
define_slot(215, LE, 30)

define_slot(116, day1('14:00'), 30)
define_slot(117, LE, 30)
define_slot(118, LE, 30)

define_slot(216, day1('14:00'), 30)
define_slot(217, LE, 30)
define_slot(218, LE, 30)

define_slot(19, day1('16:00'), 30)
define_slot(191, LE, 30)
define_slot(192, LE, 30)
define_slot(193, LE, 30)

#####################################
define_slot(20, day2('09:00'), 60)
define_slot(21, LE, 15)
define_slot(22, LE, 15)

define_slot(13, day2('11:00'), 30)
define_slot(14, LE, 30)
define_slot(15, LE, 30)

define_slot(207, day2('14:00'), 30)
define_slot(208, LE, 30)
define_slot(209, LE, 30)

define_slot(16, day2('16:00'), 30)
define_slot(17, LE, 30)
define_slot(18, LE, 30)
define_slot(199, LE, 30)


#####################################
define_slot(30, day3('09:00'), 60)
define_slot(31, LE, 30)
#define_slot(22, LE, 15)

define_slot(32, day3('11:00'), 15)
define_slot(33, LE, 15)
define_slot(34, LE, 15)
define_slot(35, LE, 15)
define_slot(36, LE, 10)

#from pprint import pprint 
#pprint(SLOTS_META)


def main():
    talks = []
    bySlot = {}

    for fn in Path("talks/").rglob("*.md"):
        t = _read(fn)
        try:
            bySlot[t.meta['slot']] = t
            talks.append(t)
        except:
            print(f"No slot defined for {fn}")


    for p in talks:
        # Add subcomponents
        m = p.meta
        c = p.content
        event = Event()
        author = str(m['author'])
        title = m['title']

        event.add('summary', f"{author}: {title}")
        event.add('description', c)

        try:
            (s,e,k) = SLOTS_META[m['slot']]

            event.add('color', k)
            event.add('categories', k)

            event.add('dtstart', s)
            event.add('dtend', e)
        except:
            print(f"Slot not defined {m['slot']}")

        # Add the organizer
        organizer = vCalAddress('MAILTO:weigl@kit.edu')
        # Add parameters of the event
        organizer.params['name'] = vText('Alexander Weigl')
        organizer.params['role'] = vText('Program Chair')
        event['organizer'] = organizer
        event['location'] = vText('Bad Herrenalb, Germany')
        cal.add_component(event)

    # Write to disk
    output = Path("public") / 'events.ics'
    with output.open('wb') as f:
        f.write(cal.to_ical())


if __name__ == "__main__": main()
