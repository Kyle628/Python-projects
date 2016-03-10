import math
import random


def calc_money(avg_return, stddev_return, leverage_ratio, number_of_periods):
    avg_return = avg_return / 100
    if avg_return > 40:
        avg_return = 40
    stddev_return = stddev_return / 100
    if stddev_return > 50:
        stddev_return = 50
    leverage_ratio = leverage_ratio
    if leverage_ratio > 10:
        leverage_ratio = 10
    number_of_periods = number_of_periods
    if number_of_periods > 500:
        number_of_periods = 500
    if number_of_periods < 10:
        number_of_periods = 10
    initial_balance = 10000
    current_balance = initial_balance
    for i in range(number_of_periods):
        rate_of_return = float(random.normalvariate(avg_return, stddev_return))
        current_balance = current_balance + float(rate_of_return * current_balance * leverage_ratio)
        if current_balance <= 0.0:
            current_balance = 0.0
    return current_balance / initial_balance


def monte_carlo_ratio(num_trials):
    num_trials = num_trials
    if num_trials > 10000:
        num_trials = 10000
    if num_trials < 100:
        num_trials = 100
    global per_period_return_loss
    zero_count = 0
    final_ratio = 0
    per_period_return = 0
    mean_k = per_period_return
    std_k = 0
    prev_mean = 0
    prev_std_k = 0
    prev_return = 0
    times_lost_money = 0
    std_loss = 0
    mean_loss = 0
    prev_return_loss = 0
    prev_mean_loss = per_period_return
    prev_std_loss = 0
    per_period_return_loss = 0
    for i in range(1, num_trials):
        final_ratio = final_ratio + float(calc_money(avg_return, stddev_return, leverage_ratio, number_of_periods))
        per_period_return = float(final_ratio ** (1 / float(number_of_periods)))
        mean_k = float(prev_mean + ((per_period_return - prev_return) / i))
        std_k = float(math.sqrt((prev_std_k + (per_period_return - prev_mean) ** 2) / i)
                      + (per_period_return - prev_mean) * (per_period_return - mean_k))
        prev_return = float(per_period_return)
        prev_mean = float(prev_return / i)
        prev_std_k = std_k
        if final_ratio <= 0:
            zero_count = (zero_count + 1)
        if final_ratio < 1:
            times_lost_money = times_lost_money + 1
            per_period_return_loss = float(final_ratio ** (1 / float(number_of_periods)))
            mean_loss = float(prev_mean_loss + ((per_period_return - prev_return_loss) / i))
            std_loss = float(math.sqrt((prev_std_loss + (per_period_return - prev_mean_loss) ** 2) / i)
                             + (per_period_return - prev_mean_loss) * (per_period_return - mean_loss))
            prev_return_loss = float(per_period_return)
            prev_mean_loss = mean_loss
            prev_std_loss = std_loss
    print 'average per period return =', per_period_return
    print 'standard deviation return =', std_k
    print 'times went broke =', zero_count
    print 'times lost money=', times_lost_money
    print 'average per period loss when lost money=', per_period_return_loss
    print 'standard deviation of losses=', std_loss


avg_return = float(raw_input('What is the average return in percent?'))
stddev_return = float(raw_input('What is the standard deviation return in percent?'))
leverage_ratio = float(raw_input('What is the leverage ratio?'))
number_of_periods = int(raw_input('What is the number of periods?'))
num_trials = int(raw_input('How many trials should we run?'))

feedback = monte_carlo_ratio(num_trials)
print feedback











