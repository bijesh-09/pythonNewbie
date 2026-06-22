import time
import datetime
import pygame  # for playing sound
import os

script_dir = os.path.dirname(os.path.abspath(__file__))


def set_alarm(alarm_time):
    print(f"Alarm set for {alarm_time}")
    sound_file = os.path.join(script_dir, "Running_It_Down-Everet_Almond.mp3")
    is_running = True

    while is_running:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        if (current_time > alarm_time):
            print("Alarm time has already passed. Please set a future time.")
            break

        # keep on printing current time until it matches the alarm time
        print(current_time)

        if current_time == alarm_time:
            print("Wake Up!!!!!!!!")
            pygame.mixer.init()
            pygame.mixer.music.load(sound_file)
            pygame.mixer.music.play()  # plays sound in bg thread , independent of running script

            # wait for user input to stop the alarm sound
            input("Press Enter to stop the alarm sound...")
            pygame.mixer.music.stop()

            # while pygame.mixer.music.get_busy(): #true if music is still playing
            #     time.sleep(1) # check every second if the music is still playing, and wait until it finishes before exiting the program

            is_running = False

        # print the current time every second until the alarm time is reached (i.e. is_running is False)
        time.sleep(1)


if __name__ == "__main__":
    alarm_time = input("Enter the alarm time (HH:MM:SS): ")
    set_alarm(alarm_time)
