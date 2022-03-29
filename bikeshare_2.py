import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input("please enter the name of the city to be analyzed").strip().lower()
    while True :
      if city in ["chicago","washington","new york city"] :
        break
      else :
          city = input("Invalid input! please enter a city from 'chicago' , 'washington' , 'new york city' ")


    # get user input for month (all, january, february, ... , june)
    month = input("please enter the month to be analyzed or enter 'all' to all months").strip().lower()
    while True:
     if month in ["january", "february", "march", "april", "may", "june","all"]:
        break

     else:
         month = input("Invalid input! please select a month from 'january' to 'june' or 'all' to select all months")

    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("please enter the name of the day of the week or enter 'all' to select all days").strip().lower()
    while True :
       if day in ["saturday", "sunday", "monday", "tuesday", "wednesday", "thursday","friday","all"]:
           break
       else:
           day = input("Invalid input! please select a day of the week or 'all' to select all days")

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    if month != "all":
        months = ["january", "february", "march", "april", "may", "june"]
        month = months.index(month) + 1

        df = df[df["month"] == month]

    if day != "all":
        df = df[df["day_of_week"] == day]

    return df

def show_raw_data(df) :
    """gets user input as a option for showing a sample from the raw data of the loaded file for the chosen city or not ."""
    q = input("you would like to show sample from the raw data of the chosen city ?  Enter yes or no").lower().strip()
    a,b = 0,5
    while True :
        if q == "no" :
            break
        elif q== "yes" :
            print(df[a:b])
            q = input("you would like to show 5 more rows ?  Enter yes or no").lower().strip()
            a += 5
            b += 5


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    common_month = df["month"].mode()[0]
    months = ["january", "february", "march", "april", "may", "june"]
    common_month_name = months[common_month-1]
    print("most common month :",common_month_name)

    # display the most common day of week
    common_day = df["day_of_week"].mode()[0]
    print("most common day :", common_day)

    # display the most common start hour
    df["start hour"] = df["Start Time"].dt.hour
    common_hour = df['start hour'].mode()
    print("most common hour :", common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_start_station = df["Start Station"].mode()[0]
    common_start_station_count = pd.value_counts(df["Start Station"])[0]
    print(f"most common start station : {common_start_station} with {common_start_station_count} trips")


    # display most commonly used end station
    common_end_station = df["Start Station"].mode()[0]
    common_end_station_count = pd.value_counts(df["End Station"])[0]
    print(f"most common end station : {common_end_station} with {common_end_station_count} trips")

    # display most frequent combination of start station and end station trip
    df["common combined"] = df["Start Station"] + "--" + df["End Station"]
    common_combination = df["common combined"].mode()[0]
    print("most common combination of start station and end station :", common_combination)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df["Trip Duration"].sum()
    total_travel_min, total_travel_sec = divmod(total_travel_time, 60)
    print(f"total travel time: {total_travel_min} min , {round(total_travel_sec, 2)} sec")

    # display mean travel time
    mean_travel_time = df["Trip Duration"].mean()
    mean_travel_min, mean_travel_sec = divmod(mean_travel_time, 60)
    print(f"mean travel time: {mean_travel_min} min , {round(mean_travel_sec, 2)} sec")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types_count = pd.value_counts(df["User Type"])
    print("counts of user types :", user_types_count)

    # Display counts of gender
    user_gender_count = pd.value_counts(df["Gender"])
    print("counts of users gender :", user_gender_count)

    # Display earliest, most recent, and most common year of birth
    earliest_birth = df["Birth Year"].max()
    print("most earliest birth year : ", int(earliest_birth))

    recent_birth = df["Birth Year"].min()
    print("most recent birth year : ", int(recent_birth))

    common_birth = df["Birth Year"].mode()
    print("most common birth year : ", int(common_birth))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        show_raw_data(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        if city == "washington" :
            break
        else :
            user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
