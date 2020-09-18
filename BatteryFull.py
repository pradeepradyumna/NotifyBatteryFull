import psutil
from plyer import notification
import sched
import time

event_schedule = sched.scheduler(time.time, time.sleep)


def RunCheckOnBattery():
    battery = psutil.sensors_battery()
    isPlugged = battery.power_plugged
    percent = str(battery.percent)

    pluggedStatus = "Plugged In" if isPlugged else "Not Plugged In"

    batteryPercentage = percent+'%'
    print(percent+'% | '+pluggedStatus)

    if isPlugged == False:
        event_schedule.cancel(eventId)
        return

    if battery.percent > 95 and isPlugged:

        notification.notify(
            title='Hey there!',
            message='Your device is charged to '+batteryPercentage +
            '. Its time to unplug the charger and save electricity.'
        )

    event_schedule.enter(30, 1, RunCheckOnBattery)


eventId = event_schedule.enter(30, 1, RunCheckOnBattery)
event_schedule.run()
