"""
Given a list of schedules for n persons. Find the list of free times.
"""


def test_calendar_schedule():
    """
    schedules = [[(10, 12), (15, 18)], [(12, 17), (23, 23)]]
    print(calendar_schedule(schedules, 0, 23))

    schedules = [[(10, 12)]]
    print (calendar_schedule(schedules, 0, 23))
    schedules = [[]]
    print (calendar_schedule(schedules, 0, 23))
    """

    schedules = [[(10, 29), (50, 99), (120, 200)],
                 [(30, 90), (130, 190)],
                 [(13, 20), (25, 90), (120, 180)]]

    # print (calendar_schedule(schedules, 105, 400))
    print (calendar_schedule(schedules, 50, 170))


def calendar_schedule(schedules, start, end):
    time_stamps = []
    for person_schedule in schedules:
        for item in person_schedule:
            if item[0] < start and item[1] < start:
                continue
            time_stamps.append((item[0], True))
            time_stamps.append((item[1], False))
    time_stamps.sort(key=lambda x: (x[0], not x[1]))

    print (time_stamps)

    output = []

    busy = 0
    if not time_stamps:
        return [(start, end)]
    if time_stamps[0][0] > start:
        output.append((start, time_stamps[0][0]))

    curr = (None, None)
    for ts in time_stamps:
        if ts[1] is False:
            busy -= 1
            if busy == 0:
                curr = (ts[0], None)
        else:
            busy += 1
            if busy == 1 and curr[0] is not None:
                curr = (curr[0], ts[0])
                output.append(curr)

    if time_stamps[-1][0] < end:
        output.append((time_stamps[-1][0], end))
    return output


test_calendar_schedule()
