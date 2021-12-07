# How to use probabilistic models in practice?

Frequently, we are interested in measuring the uncertainty of some event of interest. The most common measure for this type of goal is classical probability. Through it, we can say that for a given variable, the probability of a particular event happening is a number between 0 and 1.

Some of the most famous applications of probability are:

1. Prediction in a Classification Model (Logistic Regression, Decision Tree)
2. Outlier detection
3. Measurement of an event of interest
4. Greater interpretability of some observed variable

For example, if we have the histogram of the height of a certain company:

![height](https://github.com/AlbertoRodrigues/fit_probability_distributions/blob/main/images/normal_ex1.jpeg)

We may be interested to find whether a certain value is an outlier or not. In the case of the normal distribution, to consider whether an observation is an outlier or not, we can check whether the probability of that observed value happening is small enough. One possible choice is to measure whether this value is beyond the center of the data mass.

 In the normal distribution, if the value is greater than three standard deviations beyond the mean or less than minus three standard deviations from the mean, this value can be considered an outlier. This region has approximately 0.26% probability of happening, very small indeed. The figure below illustrates the shape of the normal distribution in relation to its standard deviation and probabilities:

![teoricnormal](https://github.com/AlbertoRodrigues/fit_probability_distributions/blob/main/images/normalteorica.png)

We can adjust the normal distribution to see if it is a reasonable choice:

![fitnormal](https://github.com/AlbertoRodrigues/fit_probability_distributions/blob/main/images/normalajuste1.jpeg)

It sounds like a proper fit. In this way, we can take several important conclusions and interpretations for this variable. Let us carefully review some analysis possibilities:

1. Check whether the observed value of 1.87 is an outlier or not
2. Calculate events of interest such as ![equation](https://latex.codecogs.com/gif.latex?\mathbb{P}(X>1.8),&space;\mathbb{P}(X>1.63)&space;\text{&space;and&space;}&space;\mathbb{P}(1.58<X<1.72))
3. Obtain confidence interval
4. Obtain Hypothesis Tests

## Outlier detection

Let us calculate the probability that 1.87 is extreme. As it deals with continuous variable, we can calculate this probability through the integral in the desired interval, given by:

![prob](https://github.com/AlbertoRodrigues/fit_probability_distributions/blob/main/images/prob1.gif)

This is exactly the equivalent of calculating the following area:

![prob](https://github.com/AlbertoRodrigues/fit_probability_distributions/blob/main/images/prob187.jpg)

As the probability of this event is greater than 0.00013, we can consider it to be a typical value of the dataset.

## Measurement of some events of interest

Now, let us calculate some events of interest through probability:

![prob](https://github.com/AlbertoRodrigues/fit_probability_distributions/blob/main/images/prob2.gif)

These probabilities are calculated from the following areas, respectively:

![prob](https://github.com/AlbertoRodrigues/fit_probability_distributions/blob/main/images/prob180.jpg)

![prob](https://github.com/AlbertoRodrigues/fit_probability_distributions/blob/main/images/prob163.jpg)

![prob](https://github.com/AlbertoRodrigues/fit_probability_distributions/blob/main/images/prob158172.jpg)



In other situations, a more skewed probability distribution may better fit some variables of interest.
To illustrate, imagine that we are studying employees' salary at a company suspected of corruption. The histogram of this variable is given below: