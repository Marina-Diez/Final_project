
![traveler](images/logo_read.png)

Portugal has always been a very visited country, not only by its neighboring countries, but also by tourists from all over the world. 
We propose the study, analysis and conclusions on the reservation of accommodation in two main points of Portugal, Lisbon and Algarve. In addition, we offer a price search engine so that you can know month by month and based on different parameters, how much the night would cost in each of these areas.

# STUDY AND ANALYSIS
For the first part of our project, we have relied on a Kaggle Dataset ["Hotel booking demand
](https://www.kaggle.com/jessemostipak/hotel-booking-demand?select=hotel_bookings.csv), to be able to access much of the information we needed.
In order to reach the conclusions we needed we have done a deep analysis of the data:
>1. **Explore Kaggle Database**. 
>2. **Think on a wire conductor**  What do we need to support with this info ?
>3. **Clean the dataset**. which are the usefull datas to find and support my hypothesis?
>4. **Analyze the data**. 
>5. **Make it visual**. For me and for our client to be understable

After analyzing how the reserves are higher in the Lisbon area than in the Algarve. We go down to see if the origin of the people who visit each area the most, coincides with those who spend the most on average per night. This information will be useful to launch campaigns limited by origin of tourists.
 In the following photo, we can see that the origin of visitors that spend more money per nigth in Lisbon, do not match which come more times.

![traveler](images/mapa.JPG)

# TRAINING OUR MODEL
In addition, in order to offer the price estimation service, we have used feature engineering in training different models to see which one best fits our data.

>1. **Remove unusable columns**
>2. **Convert categorical variables into numeric**
>3. **See which model works better**
>4. **See how normalization or standardization works**

Finally we decide to get a random forest model, with none normalize data, an with a R2 = 0.83065726669631158

# PRICE STIMATION APP
Finally we use streamlit to offer a price predictor which adjusts the amount per night based on a series of variables:
![traveler](images/Streamlit.JPG)
