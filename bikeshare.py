import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

cities= ['chicago','new york city','washington']
months=['january', 'february', 'march', 'april', 'may', 'june','all']
weekday=['monday','tuesday','wednesday','thursday','friday','saturday','sunday','all']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid 
    #inputs
    
    while True:
        city=input('Enter the city name').lower()
        if city in cities:
            break
        else:
            print('Invalid city, enter again')
        

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month=input('Enter the month').lower()
        if month in months:
            break
        else:
            print('Invalid month,ente again')

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day=input('Enter the day of week').lower()
        if day in weekday:
            break
        else:
            print('Invalid day')

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
    df= pd.read_csv(CITY_DATA[city])
    
    df['Start Time']=pd.to_datetime(df['Start Time'])
    
    df['months']= df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour
    
    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month)+1
    
        # filter by month to create the new dataframe
        df = df[df['months']==month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week']==day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['months'].mode()[0]
    print('The most common month: ',popular_month)

    # TO DO: display the most common day of week
    popular_DOW= df['day_of_week'].mode()[0]
    print('The most common DOW: ',popular_DOW)

    # TO DO: display the most common start hour
    popular_hour= df['hour'].mode()[0]
    print('The most common hour: ',popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_Startstation= df['Start Station'].mode()[0]
    print('The most common start station: ',popular_Startstation)

    # TO DO: display most commonly used end station
    popular_endstation = df['End Station'].mode()[0]
    print('The most common End station: ',popular_endstation)

    # TO DO: display most frequent combination of start station and end station trip
    most_frequent = (df['Start Station'] + "||" + df['End Station']).mode()[0]
    print('The most frequent combination: ',most_frequent)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_duration= df['Trip Duration'].sum()
    print('The total travel time: ',total_duration)

    # TO DO: display mean travel time
    travel_mean = df['Trip Duration'].mean()
    print('The mean travel time: ',travel_mean)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    User_count = df['User Type'].value_counts()
    print('The user type count: ',User_count)

    # TO DO: Display counts of gender
    try:   
        gender_count= df['Gender'].value_counts()
        print('The Gender count: ',gender_count)
        
    except Exception as err:
        print('Washington state lacks gender user data,the error is {} '.format(err))

    # TO DO: Display earliest, most recent, and most common year of birth
    try:   
        earliest_dob= df['Birth Year'].min()
        print('The earliest DOB: ',earliest_dob)
        recent_dob = df['Birth Year'].max()
        print('The Recent DOB: ',recent_dob)
        most_dob = df['Birth Year'].mode()[0]
        print('The most common DOB: ',most_dob)
        
    except Exception as err:
        print('Washington state has no Birth year,the error is {} '.format(err))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def raw_data(df):
    data= input( 'Does user want to see 5 rows of data? Enter yes or no').lower()
    x=0
    while data=='yes':
        print(df.iloc[x:(x+5)])
        x+=5
        data= input( 'Does user want to see 5 rows of data? Enter yes or no').lower()
        
    return df

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n').lower()
        if restart != 'yes':
            break


if __name__ == "__main__":
	main()
