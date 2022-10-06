from flask import Flask, render_template
import datetime

app = Flask(__name__)

@app.route('/')
def index():
    now = datetime.datetime.now()

    my_birthday = datetime.datetime(now.year, 8, 10, 0, 0, 0)
    #my_birthday = datetime.datetime(now.year, 12, 27, 3, 3, 3)
    #hora de nacimiento real, los segundos son invento mio...
    #(año, mes, dia, hora, minuto, segundo)s

    si_cumple = now.month==my_birthday.month and now.day==my_birthday.day

    if my_birthday < now:
        my_birthday = my_birthday.replace(year=now.year + 1)

    dt = abs(my_birthday - now)
    #falta = dt.days
    #segs = round(dt.total_seconds())
    #horas = round(segs/60/60)
    #d=str(dt)
    #d=d.replace("days","días")
    #d=d.replace("day", "día")
    #segs=d

    days = dt.days
    falta = days
    s = dt.seconds
    # hours
    hours = s // 3600
    horas = hours
    # remaining seconds
    s = s - (hours * 3600)
    # minutes
    minutes = s // 60
    # remaining seconds
    seconds = s - (minutes * 60)

    segs = str(days) + "d " + str(hours) + "h " + str(minutes) + "m " + str(seconds) + "s"

    intervals = (
    ('m', 2540160),  # 60 * 60 * 24 * 7 * 4.2 aprox
    ('S', 604800),  # 60 * 60 * 24 * 7
    ('d', 86400),    # 60 * 60 * 24
    ('h', 3600),    # 60 * 60
    ('m', 60),
    ('s', 1),
    )

    def display_time(seconds, granularity=6):
        result = []

        for name, count in intervals:
            value = seconds // count
            if value:
                seconds -= value * count
                result.append("{}{}".format(value, name))
        return ' '.join(result[:granularity])

    segs = str(display_time(round(dt.total_seconds())))

    return render_template("index.html", si_cumple=si_cumple, falta=falta, segs=segs, horas=horas)

if __name__=="__main__":
    app.run()
