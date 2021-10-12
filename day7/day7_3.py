# 3. City Population
#
# The city has a known population p0
# A percentage of population perc is added each year
# Every year a certain number of delta also arrive (or leave)
# We need to know when (if at all) the city will reach a population of p
#
# Write a function get_city_year (p0, perc, delta, p) that returns the years (full) when p is reached.
# If p cannot be reached, then we return -1
#
# Example:
#
# get_city_year (1000,2,50,1200) -> 3
# 1000 + 1000 * 0.02 + 50 => 1070 after the 1st year
# 1070 + 1070 * 0.02 + 50 => 1141 after the 2nd year
# 1141 + 1141 * 0.02 + 50 => 1213 after the 3rd year
# so the function here returns 3 and is done
#
# PS. Note that we give perc as a percentage to be converted to a decimal number.
#
# More test examples:
#
# get_city_year (1000, 2, -50, 5000) -> -1
# get_city_year (1500, 5, 100, 5000) -> 15
# get_city_year (1500000, 2.5, 10000, 2,000,000) -> 10

def get_city_year(p0, perc, delta, p):
    years = 0
    while p >= p0:
        p0 = p0 + (p0 * perc / 100) + delta
        years += 1
        if p0 <= 0: # if population gets to 0, target cannot be reached
            years = -1
            break
    return years


print(get_city_year(1500, 5, 100, 5000))
print(get_city_year(1500000, 2.5, 10000, 2_000_000))
print(get_city_year (1000, 2, -50, 5000))