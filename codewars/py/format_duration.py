def format_duration(seconds):
    def format_single_or_plural(n, m):
        if n > 1:
            return f"{n} {m}s"
        return f"{n} {m}"

    def find_min_sec(minutes):
        resp = format_single_or_plural(minutes, "minute")
        if seconds > 0:
            resp = f"{resp} and {format_single_or_plural(seconds, 'second')}"
        return resp

    def find_hour_minutes(hours):
        resp = format_single_or_plural(hours, "hour")
        if minutes > 0:
            min_sec = find_min_sec(minutes)
            resp = f"{resp}, {min_sec}" if seconds > 0 else f"{resp} and {min_sec}"
        return resp

    def find_day_hours(days):
        resp = format_single_or_plural(days, "day")
        if hours > 0:
            resp = f"{resp}, {find_hour_minutes(hours)}"
        elif minutes > 0:
            resp = f"{resp}, {find_min_sec(minutes)}"
        return resp

    def find_year_days(years):
        resp = format_single_or_plural(years, "year")
        if days > 0:
            resp = f"{resp}, {find_day_hours(days)}"
        return resp

    if seconds < 60:
        if seconds == 0:
            return 'now'
        return format_single_or_plural(seconds, "second")

    minutes, seconds = divmod(seconds, 60)

    if minutes < 60:
        return find_min_sec(minutes)

    hours, minutes = divmod(minutes, 60)

    if hours < 24:
        return find_hour_minutes(hours)

    days, hours = divmod(hours, 24)

    if days < 365:
        return find_day_hours(days)

    years, days = divmod(days, 365)

    return find_year_days(years)


if __name__ == "__main__":
    assert format_duration(1) == "1 second"
    assert format_duration(62) == "1 minute and 2 seconds"
    assert format_duration(120) == "2 minutes"
    assert format_duration(3600) == "1 hour"
    assert format_duration(3662) == "1 hour, 1 minute and 2 seconds"
    print(format_duration(132_030_240))

# times = [("year", 365 * 24 * 60 * 60),
#          ("day", 24 * 60 * 60),
#          ("hour", 60 * 60),
#          ("minute", 60),
#          ("second", 1)]

# def format_duration(seconds):

#     if not seconds:
#         return "now"

#     chunks = []
#     for name, secs in times:
#         qty = seconds // secs
#         if qty:
#             if qty > 1:
#                 name += "s"
#             chunks.append(str(qty) + " " + name)

#         seconds = seconds % secs

# return ', '.join(chunks[:-1]) + ' and ' + chunks[-1] if len(chunks) > 1
# else chunks[0]

# def format_duration(seconds):
#     if seconds == 0: return "now"
#     units = ( (31536000, "year"  ),
#               (   86400, "day"   ),
#               (    3600, "hour"  ),
#               (      60, "minute"),
#               (       1, "second") )
#     ts, t = [], seconds
#     for unit in units:
#         u, t = divmod(t, unit[0])
#         ts += ["{} {}{}".format(u, unit[1], "s" if u>1 else "")] if u != 0 else []
# return ", ".join([str(d)for d in ts[:-1]]) + (" and " if len(ts)>1 else
# "") + ts[-1]

# def format_duration(s):
#     dt = []
#     for b, w in [(60, 'second'), (60, 'minute'), (24, 'hour'), (365, 'day'), (s+1, 'year')]:
#         s, m = divmod(s, b)
#         if m: dt.append('%d %s%s' % (m, w, 's' * (m > 1)))
#     return ' and '.join(', '.join(dt[::-1]).rsplit(', ', 1)) or 'now'
