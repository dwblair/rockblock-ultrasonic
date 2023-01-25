import alarm
import time
import board

print("Waking up")

# Create an alarm for 60 seconds from now, and also a pin alarm.
time_alarm = alarm.time.TimeAlarm(monotonic_time=time.monotonic() + 10)
#pin_alarm = alarm.pin.PinAlarm(board.D10, False)

# Deep sleep until one of the alarm goes off. Then restart the program.
#alarm.exit_and_deep_sleep_until_alarms(time_alarm, pin_alarm)
alarm.exit_and_deep_sleep_until_alarms(time_alarm)