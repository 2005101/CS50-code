def main():
    time=input("What time is it now?")
    convert(time)
    meal=convert(time)
    if meal >=7 and time<=8:
        print("It is Breakfast time!")
    if meal>=12 and time<=13:
        print("It is lunch time!")
    if meal>=18 and time<=19:
        print("It is dinner time")



def convert(meal):
    hour,min=meal.split(":")
    new_time=float(min)/60
    return float(hour)+ new_time


if __name__ == "__main__":
    main()
