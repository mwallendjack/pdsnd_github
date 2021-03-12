import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

MONTH_DATA = ['all', 'january', 'february', 'march', 'april','may', 'june']
DAY_DATA = ['all','monday','tuesday','wednesday','thursday','friday']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Months are only first 6 months.Ends a July
    Days exclude weekends.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city_name = ''
    while city_name.lower() not in CITY_DATA :
        city_name = input ("Please chose one of these three cities: (Chicago, New York City, Washington)\n")
        if city_name.lower() in CITY_DATA:
            print('Great! We are able to find this city to analyze')
            city = city_name.lower()
        else:
            print("Sorry we are not able to analyze this City name. Please enter in either Chicago, New York City or Washington. \n")


    # TO DO: get user input for month (all, january, february, ... , june)
    month_name = ''
    while month_name.lower() not in MONTH_DATA:
        month_name = input ('Please enter the month...January through to June, where "all" is all months?')
        if month_name.lower() in MONTH_DATA:
            print('Great! We will analyze the months that you have entered!')
            month = month_name.lower()
        else:
            print('Please try entering in again the month from January to June that you would like to analyze')


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day_name = ''
    while day_name.lower() not in DAY_DATA:
        day_name = input ('Please enter the day of the week where "all" is all days?')
        if day_name.lower() in DAY_DATA:
            print('Great! We can analyze the day(s) that you have chosen')
            day = day_name.lower()
        else:
            print('Please try entering in another day of the week.')


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
    df['Start Hour'] = df['Start Time'].dt.hour
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month)+1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month = df['month'].value_counts().idxmax()
    print("The most common month is :", most_common_month)

    # TO DO: display the most common day of week
    most_common_day = df['day_of_week'].value_counts().idxmax()
    print("The most common day is :", most_common_day)


    # TO DO: display the most common start hour
    most_common_hour = df['Start Hour'].value_counts().idxmax()
    print("The most common start hour is :", most_common_hour)



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start_station = df['Start Station'].value_counts().idxmax()
    print('Your most common Station to start at is: ', most_common_start_station)

    # TO DO: display most commonly used end station
    most_common_end_station = df['End Station'].value_counts().idxmax()
    print('Your most common Station to end at is: ', most_common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    most_common_start_end_station = df.groupby(['Start Station', 'End Station']).count().idxmax()[0]
    print('Your most frequent combination of Start Station and End Station is:',most_common_start_end_station)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    tot_travel_time = df['Trip Duration'].sum()
    print('The total travel time for this analysis is:', tot_travel_time)

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('The average travel time is:', mean_travel_time)
    
    #TO DO: displace median travel time
    median_travel_time = df['Trip Duration'].median()
    print('The median travel time is:', median_travel_time)

    #TO DO: display mode travel time                             
    mode_travel_time = df['Trip Duration'].mode()
    print('The mode travel time is:', mode_travel_time) 
   


    print("\nThis took %s seconds." ,(time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type_counts = df['User Type'].value_counts()
    print( 'The different counts of User Types are:', user_type_counts)

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        gender_count_type = df['Gender'].value_counts()
        print('The different counts of Gender are:', gender_count_type)

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        float_earliest_birthyear = df['Birth Year'].min()
        earliest_birthyear = str(int(float_earliest_birthyear))
        float_most_recent_birthyear = df['Birth Year'].max()
        most_recent_birthyear = str(int(float_most_recent_birthyear))
        float_most_common_birthyear = df['Birth Year'].value_counts().idxmax()
        most_common_birthyear = str(int(float_most_common_birthyear))
        #print(type(earliest_birthyear))

        print('The earliest birth year is:', earliest_birthyear)
        print('The most recent birth year is:', most_recent_birthyear)
        print('The most common birth year is:', most_common_birthyear)
        print(type(earliest_birthyear))

        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)

def display_raw_data(df):
    """If prompted, this will display the 5 rows at a time of Raw Data.
    Function Arguments are the original Pandas data frame of the User's choice of City created from a .csv file.
    """
    print(df.head())
    next = 0
    while True:
        view_raw_data = input('\nWould you like to view next five rows of raw data? Enter yes or no.\n')
        if view_raw_data.lower() != 'yes':
            return
        next = next + 5
        print(df.iloc[next:next+5])




def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        while True:
            view_raw_data = input('\nWould you like to view first five rows of raw data? Please enter yes or no.\n')
            if view_raw_data.lower() == 'no':
                break
            elif view_raw_data.lower() == 'yes':
                display_raw_data(df)
                break
            else:
                print('Please enter the values of either "yes" or "no".')


        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
