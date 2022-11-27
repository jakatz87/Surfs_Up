# Surfs Up
## Overview
I assisted in the development of a business plan to open a surf and ice cream shop on the island of Oahu.  I was given temperature data from nine different weather stations over a 7 year period to determine the viability of the business plan depending on the weather pattern.

## Resources
***Data Source***: 
- hawaii.sqlite

***Software***: 
- Python 3.7.13
- Pandas
- JSON
- Jupyter Notebook
- VS Code
- SQLite
- SQLAlchemy
- Flask

## Results
Using the source file, I worked with SQLAlchemy and SQLite in Jupyter Notebook to write queries and create Data Frames with select information like precipitation and temperature.

To alleviate the processing burden, I only used two years of data from all nine weather stations to study precipitation:
```
prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)

# Perform a query to retrieve the data and precipitation scores
results = []
results = session.query(Measurement.date, Measurement.prcp)
# Add the filter for the previous year
results = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= prev_year)
# Add the command to put the results in a list
results = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= prev_year).all()

# Save the query results as a Pandas DataFrame and set the index to the date column
df = pd.DataFrame(results, columns = ['date', 'precipitation'])
df.set_index(df['date'], inplace = True)
```

A quick plot of precipitation data highlights the times of year when precipitation tends to be higher:

![precip chart](https://github.com/jakatz87/surfs_up/blob/main/precip_plot.png)

A look at the summary statistics show the Average and Median precipitation levels are enough to ignore the Maximums:

![precip summary](https://github.com/jakatz87/surfs_up/blob/main/precip_describe.png)

To analyze temperature, I used two years of data from the most prolific weather station:
```
results=session.query(Measurement.tobs).\
    filter(Measurement.station=='USC00519281').\
    filter(Measurement.date >= prev_year).all()

#print(results)

#Put the information into a DataFrame
df = pd.DataFrame(results, columns=['tobs'])
```

The frequency table from this analysis is enough to display how perfect the weather tends to be over time:

![tobs chart](https://github.com/jakatz87/surfs_up/blob/main/temps_pop_station.png)

A look at the summary statistics only serves to justify the plan:

![tobs summary](https://github.com/jakatz87/surfs_up/blob/main/temps_describe.png)


To compare the hottest and coldest part of the year, I analyzed the months of June and December for the entire data set:
```
june_temps = session.query(Measurement.date, Measurement.tobs).filter(extract('month', Measurement.date)==6).all()
# 2. Convert the June temperatures to a list.
results=[]
results=june_temps
# 3. Create a DataFrame from the list of temperatures for the month of June. 
june_df = pd.DataFrame(results, columns = ['date', 'June Temps'])
```

June DataFrame and Summary Statistics:

![june df](https://github.com/jakatz87/surfs_up/blob/main/june_df.png)

![june summary](https://github.com/jakatz87/surfs_up/blob/main/june_describe.png)

```
dec_temps = session.query(Measurement.date, Measurement.tobs).filter(extract('month', Measurement.date)==12).all()
# 7. Convert the December temperatures to a list.
results_d=[]
results_d=dec_temps
# 8. Create a DataFrame from the list of temperatures for the month of December. 
dec_df=pd.DataFrame(results_d, columns=['date', 'December Temps'])
```

December DataFrame and Summary Statistics:

![dec df](https://github.com/jakatz87/surfs_up/blob/main/dec_df.png)

![dec summary](https://github.com/jakatz87/surfs_up/blob/main/dec_describe.png)


## Summary
1. Precipitation is not an obstacle. There will be select times with high precipitation, like January, April, July/August.
2. Temperature is certainly not an obstacle. The comparison of summary statistics between June and December show that the Average, Median, Minimum, and Maximum temperatures are not far off from one another.
3. It may be best for the rare occasions of higher precipitation and lower temperatures to make sure the surf and ice cream shop is ready to supplement its inventory with wetsuits and hot chocolate.  
