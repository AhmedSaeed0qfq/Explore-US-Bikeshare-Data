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
    print('-'*40+'\n\n')

    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city=input("would you like to see data for chicago, new york city or washington : ").lower()
        if city== 'chicago' or city== 'new york city' or city== 'washington':
            break
        else:
            print("invalid input,please Choose from: chicago, new york city or washington")    
    # get user input for month (all, january, february, ... , june)
    # get user input for day of week (all, monday, tuesday, ... sunday)
    # get type of filter month,day or both
    while True:
        filter_choice=input("would you like to filter data by month,day,both or none of them(please Enter none if you don't want any filter ): ").lower()
        if filter_choice=='both':
            while True:
                month=input("which month: ").lower()
                months = ['all','january', 'february', 'march', 'april', 'may', 'june',]
                if month in months:
                    break
                else:
                    print("invalid input,Please try again and make sure you type correct month") 
            while True:
                day=input('which day: ').title()
                days=['all','Monday','Thursday','Wednesday','Tuesday','Saturday','Sunday','Friday']
                if day in days:
                    break
                else:
                    print("invalid input,Please try again and make sure you type correct day")
        # filter by month
        elif filter_choice=='month':
            while True:
                month=input("which month: ").lower()
                months = ['january', 'february', 'march', 'april', 'may', 'june',]
                day=None
                if month in months:
                    break
                else:
                    print("invalid input,Please try again and make sure you type correct month") 
        # filter by day
        elif filter_choice=='day':
            while True:
                day=input('which day: ').title()
                days=['Monday','Thursday','Wednesday','Tuesday','Saturday','Sunday','Friday']
                month=None
                if day in days:
                    break
                else:
                    print("invalid input,Please try again and make sure you type correct day")
        elif filter_choice=='none':
            month='none'
            day='none'   
        else:
            print("invalid input,please Choose from: month,day,both or none")
            continue
        break
    return city,filter_choice,month,day
    
def load_data(city):
    """
    Loads data for the specified city

    Args:
        (str) city - name of the city to analyze
    Returns:
        df - Pandas DataFrame containing city data
    """
    df=pd.read_csv(CITY_DATA[city])
    df['Start Time']=pd.to_datetime(df['Start Time'])
    df['month']=df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    return df
def load_data_filterd_by_both(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df=pd.read_csv(CITY_DATA[city])
    df['Start Time']=pd.to_datetime(df['Start Time'])
    df['month']=df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    #filter by month
    if month !='all':
        months = ['january', 'february', 'march', 'april', 'may', 'june',]
        month=months.index(month)+1
        df=df[df['month']==month]
    ##filter by day
    if day != 'all':
        df=df[df['day_of_week']==day.title()]
    return df    
def load_data_filterd_by_month(city, month):
    """
    Loads data for the specified city and filters by month if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month
    """
    df=pd.read_csv(CITY_DATA[city])
    df['Start Time']=pd.to_datetime(df['Start Time'])
    df['month']=df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    #filter by month
    if month !='all':
        months = ['january', 'february', 'march', 'april', 'may', 'june',]
        month=months.index(month)+1
        df=df[df['month']==month]
    return df    
def load_data_filterd_by_day(city,day):
    """
    Loads data for the specified city and filters by day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by day
    """
    df=pd.read_csv(CITY_DATA[city])
    df['Start Time']=pd.to_datetime(df['Start Time'])
    df['month']=df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    ##filter by day
    if day != 'all':
        df=df[df['day_of_week']==day.title()]
    return df       
def time_stats(df,filter_choice):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    if filter_choice !='none':
        print("Data was filterd by: "+filter_choice+'\n')
    else:
        print("Data wasn't filterd\n")
    # display the most common month
    common_month=df['month'].mode()[0]
    print('The most common month is: '+str(common_month)+'   ,   Number of repetitions = '+str((df['month'] == common_month).sum()))
    # display the most common day of week
    common_day_of_week=df['day_of_week'].mode()[0]
    print('The most common day of week is: '+str(common_day_of_week)+'   ,    Number of repetitions = '+str((df['day_of_week'] == common_day_of_week).sum()))
    # display the most common start hour
    df['hour']=df['Start Time'].dt.hour
    common_start_hour=df['hour'].mode()[0]
    print('The most common start hour is: '+str(common_start_hour)+'   ,   Number of repetitions = '+str((df['hour'] == common_start_hour).sum()))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def station_stats(df,filter_choice):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    if filter_choice !='none':
        print("Data was filterd by: "+filter_choice+'\n')
    else:
        print("Data wasn't filterd\n")
    # display most commonly used start station
    common_start_station=df['Start Station'].mode()[0]
    print("Most commonly used start station is : "+ common_start_station +'   ,   Number of repetitions = '+str((df['Start Station'] == common_start_station).sum()))

    # display most commonly used end station
    common_end_station=df['End Station'].mode()[0]
    print("Most commonly used end station is : "+common_end_station+ '   ,   Number of repetitions = '+str((df['End Station'] == common_end_station).sum()))

    # display most frequent combination of start station and end station trip
    df['Start&End Station']=df['Start Station']+','+df['End Station']
    most_frequent_combination_start_and_end_station=df['Start&End Station'].mode()[0]
    print('Most frequent combination of start station and end station trip is : '+most_frequent_combination_start_and_end_station+'   ,   Number of repetitions = '+str((df['Start&End Station'] == most_frequent_combination_start_and_end_station).sum()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def trip_duration_stats(df,filter_choice):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    if filter_choice !='none':
        print("Data was filterd by: "+filter_choice+'\n')
    else:
        print("Data wasn't filterd\n")
    # display total travel time
    print('The total travel time is: '+str(format(df['Trip Duration'].sum(),".2f")))

    # display mean travel time
    print('Average travel time is: '+str(format(df['Trip Duration'].mean(),".2f")))
    print('Count of travels = '+str(df['Trip Duration'].count()))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def user_stats(df,city,filter_choice):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    if filter_choice !='none':
        print("Data was filterd by: "+filter_choice+'\n')
    else:
        print("Data wasn't filterd\n")   
    # Display counts of user types
    print(df['User Type'].value_counts().to_string()+'\n')

    if city=='chicago' or city=='new york city':
        # Display counts of gender
        print(df['Gender'].value_counts().to_string()+'\n')
        # Display earliest, most recent, and most common year of birth
        print('The earliest year of birth is : '+str(int(df['Birth Year'].min())))
        print('The most recent year of birth is : '+str(int(df['Birth Year'].max())))
        common_year=df['Birth Year'].mode()[0]
        print('The most common year of birth is : '+str(int(common_year))+'   ,  Number of repetitions = '+str((df['Birth Year'] == common_year).sum()))
        print("\nThis took %s seconds." % (time.time() - start_time))
        
    print('-'*40)
def display_data(df):
    view_data=input("Would you like to view 5 rows of individual trip data? Enter yes or no?: ")
    start_loc = 0
    while True:
        print(df.iloc[start_loc:start_loc+5])
        start_loc += 5
        view_display = input("Do you wish to continue?: ").lower()
        if view_display!='yes':
            break
def main():
    while True:
        city,filter_choice,month,day=get_filters()
        if  filter_choice=='none':
            df=load_data(city)      
        elif filter_choice=='both':
            df=load_data_filterd_by_both(city,month,day)     
        elif filter_choice=='month':
            df=load_data_filterd_by_month(city,month)
        elif filter_choice=='day':
            df=load_data_filterd_by_day(city,day)
        time_stats(df,filter_choice)
        station_stats(df,filter_choice)
        trip_duration_stats(df,filter_choice)
        user_stats(df,city,filter_choice)
        display_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()