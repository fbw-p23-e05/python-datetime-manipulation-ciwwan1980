# ### Task 1

# Using the variable called `current_datetime`, subtract 15 days from the current time.

# Hint: use `.strftime()` method to reformat the time

# - If today is 8/07/2021, your result should look like this:

# ```
# 2021-06-23


from datetime import datetime, timedelta

current_datetime = datetime.now()
print(current_datetime, "current_datetime")

new_datetime = current_datetime - timedelta(days=15)


result = new_datetime.strftime("%Y-%m-%d")

print(result)