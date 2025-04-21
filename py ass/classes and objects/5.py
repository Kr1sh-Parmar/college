

class Time:
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def __str__(self):
        return f"{self.hours:02}:{self.minutes:02}:{self.seconds:02}"

    def add_time(self, other):
        total_seconds = (self.hours * 3600 + self.minutes * 60 + self.seconds) + \
                        (other.hours * 3600 + other.minutes * 60 + other.seconds)
        return Time(total_seconds // 3600, (total_seconds % 3600) // 60, total_seconds % 60)

    def subtract_time(self, other):
        total_seconds = (self.hours * 3600 + self.minutes * 60 + self.seconds) - \
                        (other.hours * 3600 + other.minutes * 60 + other.seconds)
        if total_seconds < 0:
            total_seconds = 0
        return Time(total_seconds // 3600, (total_seconds % 3600) // 60, total_seconds % 60)
    

    def time_difference(self, other):
        total_seconds = abs((self.hours * 3600 + self.minutes * 60 + self.seconds) - 
                            (other.hours * 3600 + other.minutes * 60 + other.seconds))
        return Time(total_seconds // 3600, (total_seconds % 3600) // 60, total_seconds % 60)
    

    def to_seconds(self):
        return self.hours * 3600 + self.minutes * 60 + self.seconds     


# Example usage
if __name__ == "__main__":
    time1 = Time(2, 30, 45)
    time2 = Time(1, 15, 20)

    print("Time 1:", time1)
    print("Time 2:", time2)

    added_time = time1.add_time(time2)
    print("Added Time:", added_time)

    subtracted_time = time1.subtract_time(time2)
    print("Subtracted Time:", subtracted_time)

    time_diff = time1.time_difference(time2)
    print("Time Difference:", time_diff)

    total_seconds = time1.to_seconds()
    print("Total Seconds in Time 1:", total_seconds)


   