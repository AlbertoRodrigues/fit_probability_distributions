# How to use probabilistic models in practice?

Frequently, we are interested in measuring the uncertainty of some event of interest. The most common measure for this type of goal is classical probability. Through it, we can say that for a given variable, the probability of a particular event happening is a number between 0 and 1.

Some of the most famous applications of probability are:

1. Prediction in a Classification Model (Logistic Regression, Decision Tree)
2. Outlier detection
3. Measurement of an event of interest
4. Greater interpretability of some observed variable

For example, if we have the histogram of the height of a certain company:

![height](https://github.com/AlbertoRodrigues/fit_probability_distributions/blob/main/images/normal_ex1.jpeg)

We may be interested in finding out whether a certain value is an outlier or not. In the case of the normal distribution, to consider whether an observation is an outlier or not, we can check whether the probability of that observed value happening is small enough. One possible choice is to measure whether this value is beyond the center of the data mass.

 In the normal distribution, if the value is greater than three standard deviations beyond the mean or less than minus three standard deviations from the mean, this value can be considered an outlier. This region has approximately 0.26% probability of happening, very small indeed. The figure below illustrates the shape of the normal distribution in relation to its standard deviation and probabilities:

![teoricnormal](https://github.com/AlbertoRodrigues/fit_probability_distributions/blob/main/images/normalteorica.png)

We can adjust the normal distribution to see if it is a reasonable choice:

![fitnormal](https://github.com/AlbertoRodrigues/fit_probability_distributions/blob/main/images/normalajuste1.jpeg)

It sounds like a proper fit. In this way, we can draw several important conclusions and interpretations of this variable. Let us carefully review some possibilities:

1. Check whether the observed value of 1.97 is an outlier or not
2. Calculate events of interest such as $`\sqrt{2}`$
3. Obtain confidence interval
4. Obtain Hypothesis Tests

In other situations, a more skewed probability distribution may better fit some variables of interest.
To illustrate, imagine that we are studying employees' salary at a company suspected of corruption. The histogram of this variable is given below: