
import pandas as pd
import seaborn as sns
data=pd.read_parquet("Data/data.parquet")


# ## Uniform Distribution
# ![image.png](attachment:image.png)
# 
# Uniform distribution is a probability distribution where each value within a certain range is equally likely to
# occur and values outside of the range never occur 
# For example a coin 
# In a discrete uniform distribution, outcomes are discrete and have the same probability.
# In a continuous uniform distribution, outcomes are continuous and infinite.


# import uniform distribution
from scipy.stats import uniform


# random numbers from uniform distribution
n = 10000
start = 10
width = 20
data_uniform = uniform.rvs(size=n, loc=start,scale=width)
#data_uniform = uniform.rvs(data["NET_SALES"])


ax = sns.displot(data_uniform,
                  bins=100,
                  kde=True,
                  color='skyblue')
ax.set(xlabel='Uniform Distribution ', ylabel='Frequency')


# ##  Normal Distribution 
# ![image.png](attachment:image.png)
# 
# The normal or Gaussian distribution is a continuous probability distribution characterized by a symmetric
# bell-shaped curve. A normal distribution is defined by its center (mean) and spread (standard deviation.). 
# The bulk of the observations generated from a normal distribution lie near the mean, which lies at the exact
# center of the distribution: as a rule of thumb, about 68% of the data lies within 1 standard deviation of the mean,
# 95% lies within 2 standard deviations and 99.7% lies within 3 standard deviations.


from scipy.stats import norm
data_normal = norm.rvs(size=10000,loc=0,scale=1)
#data_normal = norm.rvs(data["NET_SALES"],scale=1)


ax = sns.displot(data_normal,
                  bins=100,
                  kde=True,
                  color='skyblue')
ax.set(xlabel='Normal Distribution', ylabel='Frequency')


# ## Binomial distribution
# 
# The binomial distribution is a discrete probability distribution that models the outcomes of a given number of random trails of some experiment or event. The binomial is defined by two parameters: the probability of success in any given trial and the number of trials. The binomial distribution tells you how likely it is to achieve a given number of successes in n trials of the experiment. For example, we could model flipping a fair coin 10 times with a binomial distribution where the number of trials is set to 10 and the probability of success is set to 0.5. In this case the distribution would tell us how likely it is to get zero heads, 1 head, 2 heads and so on.
# 
# ![image.png](attachment:image.png)
# ![image-2.png](attachment:image-2.png)


from scipy.stats import binom
data_binom = binom.rvs(n=10,p=0.8,size=10000)
#data_binom = binom.rvs(data["NET_SALES"],p=0.8)



ax = sns.displot(data_binom,
                  kde=False,
                  color='skyblue')
ax.set(xlabel='Binomial Distribution', ylabel='Frequency')


# ## Bernoulli Distribution 
# 
# ![image.png](attachment:image.png)
# 
# The Bernoulli distribution is a discrete distribution having two possible outcomes labelled by n=0 and n=1 in which n=1 ("success") occurs with probability p and n=0 ("failure") occurs with probability q=1-p, where 0<p<1.
# 
# The performance of a fixed number of trials with fixed probability of success on each trial is known as a Bernoulli trial.


from scipy.stats import bernoulli
data_bern = bernoulli.rvs(size=10000,p=0.6)


ax= sns.displot(data_bern,
                 kde=False,
                 color="skyblue")
ax.set(xlabel='Bernoulli Distribution', ylabel='Frequency')


# ## Poisson distribution
# 
# ![image.png](attachment:image.png)
# 
# The Poisson distribution models the probability of seeing a certain number of successes within a time interval,
# where the time it takes for the next success is modeled by an exponential distribution. The Poisson distribution can be 
# used to model traffic, such as the number of arrivals a hospital can expect in a hour's time or the number of emails you'd
# expect to receive in a week.


from scipy.stats import poisson
data_poisson = poisson.rvs(mu=3, size=10000)
#data_poisson = poisson.rvs(data["NET_SALES"])


ax = sns.displot(data_poisson,
                  bins=30,
                  kde=False,
                  color='skyblue')
ax.set(xlabel='Poisson Distribution', ylabel='Frequency')


# ## Exponential Distributiion
# 
# ![image.png](attachment:image.png)
# 
# To predict the amount of waiting time until the next event (i.e., success, failure, arrival, etc.).
# It is often used to model the time elapsed between events.The geometric distribution is discrete and models the number of trials it takes to achieve a success in repeated experiments with a given probability of success. The exponential distribution is a continuous analog of the geometric distribution and models the amount of time you have to wait before an event occurs given a certain occurrence rate.
# 
# Most Important property of exponential distributution is memoryless. It can be used in Car accidents. It doesn’t increase or decrease your chance of a car accident if no one has hit you in the past five hours. 
# 
# The exponential distribution is the only continuous distribution that is memoryless (or with a constant failure rate). Geometric distribution, its discrete counterpart, is the only discrete distribution that is memoryless.



from scipy.stats import expon
data_expon = expon.rvs(scale=1,loc=0,size=1000)
#data_expon = expon.rvs(data["NET_SALES"])




ax = sns.displot(data_expon,
                  kde=True,
                  bins=100,
                  color='skyblue')
ax.set(xlabel='Exponential Distribution', ylabel='Frequency')


# ## Gamma Distribution 
# ![image.png](attachment:image.png)
# 
# The exponential distribution predicts the wait time until the *very first* event. The gamma distribution, on the other hand, predicts the wait time until the *k-th* event occurs.
# 
# 
# Poisson, Exponential, and Gamma distribution model different aspects of the same process — the Poisson process.
# 
# -->Poisson distribution is used to model the # of events in the future, 
# 
# -->Exponential distribution is used to predict the wait time until the very first event, and Gamma distribution is used to predict the wait time until the k-th event.
# 
# --> Gamma’s two parameters are both strictly positive, because one is the number of events and the other is the rate of events. They can’t be negative.
# 



from scipy.stats import gamma
data_gamma = gamma.rvs(a=5, size=10000)
#data_gamma = gamma.rvs(data["NET_SALES"])

ax = sns.displot(data_gamma,
                  kde=True,
                  bins=100,
                  color='skyblue')
ax.set(xlabel='Gamma Distribution', ylabel='Frequency')

