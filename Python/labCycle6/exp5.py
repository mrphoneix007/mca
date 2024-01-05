class Time:
    def __init__(self, hour=0, minute=0, second=0):
        self.__hour = hour
        self.__minute = minute
        self.__second = second

    def __add__(self, other_time):
        total_seconds = self.__hour * 3600 + self.__minute * 60 + self.__second
        total_seconds += other_time.__hour * 3600 + other_time.__minute * 60 + other_time.__second

        hours = total_seconds // 3600
        total_seconds %= 3600
        minutes = total_seconds // 60
        seconds = total_seconds % 60

        return Time(hours, minutes, seconds)

    def display_time(self):
        print(f"Sum of two Times: {self.__hour:02d}:{self.__minute:02d}:{self.__second:02d}")


hour1 = int(input("Enter hours for Time 1: "))
minute1 = int(input("Enter minutes for Time 1: "))
second1 = int(input("Enter seconds for Time 1: "))

hour2 = int(input("Enter hours for Time 2: "))
minute2 = int(input("Enter minutes for Time 2: "))
second2 = int(input("Enter seconds for Time 2: "))

time1 = Time(hour1, minute1, second1)
time2 = Time(hour2, minute2, second2)

result_time = time1 + time2
result_time.display_time()
