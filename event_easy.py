
import datetime as dt




class Event:

    def __init__(self, start_dt, end_dt):
        self.start_dt = start_dt
        self.end_dt = end_dt

    def number_hours_day(self):
        return dt.timedelta(hours=16)

    def number_hours_night(self):
        return dt.timedelta(hours=8)

    @property
    def event_for_pay(self):
        result = []
        s = self.start_dt
        e = self.end_dt
        while s < e:
            initial_start = s
            # if the event is starts during day
            if s.replace(hour=6) <= initial_start < s.replace(hour=22):
                # if event ended before 22pm
                if s.replace(hour=22) > e:
                    result.append({'start': initial_start, 'end': e})
                    # print('if 1', s)
                    s = e
                # if the event continue after 22pm
                else:
                    result.append({'start': initial_start, 'end': initial_start.replace(hour=22)})
                    # print('else 1', s)
                    s = initial_start.replace(hour=22)
            # if the event is starts during night
            if s.replace(hour=22) <= initial_start < (s.replace(hour=6) + dt.timedelta(days=1)):
                # if event ended before 6am
                if (s.replace(hour=6) + dt.timedelta(days=1)) > e:
                    result.append({'start': initial_start, 'end': e})
                    # print('if 2', s)
                    s = e
                # if the event continue after 6am
                else:
                    result.append({'start': initial_start, 'end': (s.replace(hour=6) + dt.timedelta(days=1))})
                    # print('else 2', s)
                    s = (s.replace(hour=6) + dt.timedelta(days=1))
        return result



start = dt.datetime(2021, 3, 8, 14, 0, 0)
end = dt.datetime(2021, 3, 10, 14, 0, 0)
my_event = Event(start_dt=start, end_dt=end)
result = my_event.event_for_pay
print(result)
for r in result:
    print(r)




