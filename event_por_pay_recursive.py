import datetime as dt


result = []
def event_for_pay(s, e):
    global result
    if s < e:
        initial_start = s
        # if the event is starts during day
        if s.replace(hour=6) <= initial_start < s.replace(hour=22):
            # if event ended before 22pm
            if s.replace(hour=22) > e:
                result += [{'start': initial_start, 'end': e}]
                print('if 1', s)
                s = e
            # if the event continue after 22pm
            else:
                result += [{'start': initial_start, 'end': initial_start.replace(hour=22)}]
                print('else 1', s)
                s = initial_start.replace(hour=22)
                event_for_pay(s, e)
        # if the event is starts during night
        if s.replace(hour=22) <= initial_start < (s.replace(hour=6) + dt.timedelta(days=1)):
            # if event ended before 6am
            if (s.replace(hour=6) + dt.timedelta(days=1)) > e:
                result += [{'start': initial_start, 'end': e}]
                print('if 2', s)
                s = e
            # if the event continue after 6am
            else:
                result += [{'start': initial_start, 'end': (s.replace(hour=6) + dt.timedelta(days=1))}]
                print('else 2', s)
                s = (s.replace(hour=6) + dt.timedelta(days=1))
                event_for_pay(s, e)
    return result

s = dt.datetime(2021, 3, 11, 10, 0, 0)
e = s + dt.timedelta(days=5)
result = event_for_pay(s, e)

print(result)
for r in result:
    print(r)
