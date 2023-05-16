import time

def pomodoro_timer(minutes):
    """Starts a Pomodoro timer for a given number of minutes."""
    seconds = minutes * 60
    while seconds > 0:
        minutes, secs = divmod(seconds, 60)
        countdown = '{:02d}:{:02d}'.format(minutes, secs)
        print(countdown, end='\r')
        time.sleep(1)
        seconds -= 1
    print('Time\'s up!')

pomodoro_timer(25) # Starts a 25-minute Pomodoro timer
