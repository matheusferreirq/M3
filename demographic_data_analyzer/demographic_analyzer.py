import pandas as pd

def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    df_races = df['race']
    race_count = df_races.value_counts()

    # What is the average age of men?
    df_men = df[df['sex'] == 'Male']
    average_age_men = round(df_men['age'].mean(), 1)

    # What is the percentage of people who have a Bachelor's degree?
    df_bachelors = df['education'] == 'Bachelors'
    mean_bachelors = df_bachelors.mean()
    percentage_bachelors = round(mean_bachelors * 100, 1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    df['high_ed_rich'] = ((df['education'] == 'Bachelors') | (df['education'] == 'Doctorate') | (df['education'] == 'Masters')) & (df['salary'] == '>50K')
    higher_education_rich = round(df['high_ed_rich'].mean() * 100, 1) 
    
    # What percentage of people without advanced education make more than 50K?
    lower_education = ~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    lower_education_group = df[lower_education]
    lower_education_rich = round((lower_education_group['salary'] == '>50K').mean() * 100, 1) if lower_education_group.shape[0] > 0 else 0

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = round(df['hours-per-week'].min(), 1)

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    min_workers = df[df['hours-per-week'] == min_work_hours]
    num_min_workers = min_workers.shape[0]
    rich_min_workers = min_workers[min_workers['salary'] == '>50K'].shape[0]
    rich_percentage = round((rich_min_workers / num_min_workers) * 100, 1) if num_min_workers > 0 else 0

    # What country has the highest percentage of people that earn >50K?
    country_rich_counts = df[df['salary'] == '>50K']['native-country'].value_counts()
    country_total_counts = df['native-country'].value_counts()
    country_rich_percentages = (country_rich_counts / country_total_counts) * 100
    highest_earning_country = country_rich_percentages.idxmax()
    highest_earning_country_percentage = round(country_rich_percentages.max(), 1)

    # Identify the most popular occupation for those who earn >50K in India.
    india_rich = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
    top_IN_occupation = india_rich['occupation'].value_counts().idxmax() if not india_rich.empty else None

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
calculate_demographic_data(print_data=True)