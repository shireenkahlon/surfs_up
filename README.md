# surfs_up
This project will be using Python and SQLAlchemy to analyze weather data for Hawaii; the data is located within a SQLite file
## Overview of the statistical analysis:
The purpose of this project is to analyze temperature trends in Oahu. My client has plans to open a surf and ice cream shop in Oahu, Hawaii. To do so, we spoke with an investor in hopes of extra help developing and building this business. This investor, W. Avy, would need to see the temperature trends to determine whether the surf shop would be successful. He would like to ensure that the temperature is warm enough year-round for surfers to shop and have ice cream before or after surfing the waves. I have created summary statistics for the weather in June and December of previous years by querying through and analyzing the data available to me. This provided me a clear picture of  the temperature trends year-round.
## Results:
* The count of data values per month is higher in June (1700 temperatures collected) than December (1517 temperatures). Further data analysis would need to be done to determine why the count is higher in June. It could possibly be that through the night and early mornings, the temperature changes a bit but in the daytime - when the surf shop would be open - the temperature is relatively constant. Another possibility would be if the temperature changes occur in early to mid June as the season is getting into the core of summer but remains constant in the end of June. There are various theories as to why the count may be different but this could be significant to understanding the temperature changes between June and December.
* We can gather from the mean and standard deviation that in June, the temperatures will generally be between 71.68°F and 78.2°F. The general range is perfect for surfing and eating ice cream. On the other hand, the temperatures in December will be between 67.29°F and 74.79°F. The general range for December is a bit chilly for ice cream but combined with other aspects, such as a possible low wind chill, may be a good range for surfing. 
* The statistical summary shows the minimum in December being 56°F — although by looking at the mean and standard deviation, this temperature is an outlier.  If this low temperature occurs during the daytime, it could hinder business at the shop for the day. In comparison, the minimum in June is 64°F — also an outlier; however this is a bit warmer and with a low wind chill and high humidity, this may keep the surfers coming into the store. Much of the sales would depend on further analysis on different weather patterns — including precipitation, at what times are the temperatures generally lower, among other factors.

For reference, the June summary statistics is shown below:

![june_summary_stats](https://github.com/shireenkahlon/surfs_up/blob/main/june_summary_stats.png)

The image below represents the December summary statistics: 

![dec_summary_stats](https://github.com/shireenkahlon/surfs_up/blob/main/dec_summary_stats.png)
## Summary:
The results of the queries completed are that both June and December present high enough temperatures for surfing. As discussed above, the range, in both June and December, are perfect weather to surf in. December weather could possibly be a bit chilly for ice cream but the shop would likely make profits year-round. However, temperatures are a small part of the weather. Another query that could be completed is precipitation. If it rains 300 days of the year in Oahu, for example, it might cause surfers to stay in resulting in poor sales for the shop. Another query would be to look through the months in the core of the summer and winter - such as July and January. This would give a better idea of how hot or cold it could get in Oahu. Finally, further data would need to be collected in order to query through to find the wind chill and humidity during the months of June and December to get an accurate representation of how warm or cold it may feel to people on the beach. A high wind chill could make 70°F weather feel like 60°F, whereas high humidity could make 73°F weather feel like 83°F. Additional analyses and collection of data would create a larger picture of whether the shop could succeed in Oahu or if finding another city in Hawaii or elsewhere would be ideal.
