import time
from datetime import datetime


class Timer:
    def __init__(self, _name, _duration):
        self.name = _name
        self.duration = _duration
        self.started_at = datetime.now()

    def __str__(self):
        return f"Timer '{self.name}' set for {self.duration} minutes (Started at:{self.print_started_at()}"

    def __repr__(self):
        return f"Timer('{self.name}',{self.duration})"

    def __del__(self):
        print(f"Goodbye from Timer name: {self.name}")

    def print_started_at(self):
        return self.started_at.strftime("%H:%M:%S")

    def run(self):
        print("starting timer at:", self.print_started_at())
        time.sleep(self.duration* 60)
        end_time = datetime.now().strftime("%H:%M:%S")
        print(f"Timer '{self.name}' finished.")
        print(f"End time: {end_time}")
    def time_passed(self):
        now=datetime.now()
        diff= now-self.started_at
        return str(diff).split('.')[0]