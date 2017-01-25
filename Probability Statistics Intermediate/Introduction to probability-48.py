## 1. Probability basics ##

# Print the first two rows of the data.
print(flags[:2])
most_bars_country = flags['name'][flags['bars'].idxmax()]
highest_population_country = flags['name'][flags['population'].idxmax()]

## 2. Calculating probability ##

total_countries = flags.shape[0]
orange_probability = len(flags[flags["orange"] == 1])/total_countries
stripe_probability = len(flags[flags["stripes"] > 1])/total_countries


## 3. Conjunctive probabilities ##

five_heads = .5 ** 5
ten_heads = 0.5 ** 10
hundred_heads = 0.5 ** 100

## 4. Dependent probabilities ##

# Remember that whether a flag has red in it or not is in the `red` column.
total = len(flags)
red = len(flags[flags['red']==1])
one_red = red/total
two_red = one_red * ((red-1)/(total - 1))
three_red = two_red * ((red-2)/(total - 2))

## 5. Disjunctive probability ##

start = 1
end = 18000
def count_evenly_divisible(start, end, div):
    divisible = 0
    for i in range(start, end+1):
        if (i % div) == 0:
            divisible += 1
    return divisible

hundred_prob = count_evenly_divisible(start, end, 100) / end
seventy_prob = count_evenly_divisible(start, end, 70) / end

## 6. Disjunctive dependent probabilities ##

stripes_or_bars = None
red_or_orange = None
red = flags[flags["red"] == 1].shape[0] / flags.shape[0]
orange = flags[flags["orange"] == 1].shape[0] / flags.shape[0]
red_and_orange = flags[(flags["red"] == 1) & (flags["orange"] == 1)].shape[0] / flags.shape[0]

red_or_orange = red + orange - red_and_orange

stripes = flags[flags["stripes"] > 0].shape[0] / flags.shape[0]
bars = flags[flags["bars"] > 0].shape[0] / flags.shape[0]
stripes_and_bars = flags[(flags["stripes"] > 0) & (flags["bars"] > 0)].shape[0] / flags.shape[0]

stripes_or_bars = stripes + bars - stripes_and_bars

## 7. Disjunctive probabilities with multiple conditions ##

heads_or = None
all_three_tails = (1/2 * 1/2 * 1/2)
heads_or = 1 - all_three_tails