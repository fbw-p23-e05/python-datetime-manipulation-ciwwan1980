
# ### Task 2

# Using the variable called `current_datetime`, add 7 days to your current day.

# - Your result should look like this, if today is 8/07/2021:

# ```
# 2021-07-15
# ```

from datetime import datetime, timedelta

current_datetime = datetime(2021, 7, 8)


result_datetime = current_datetime + timedelta(days=7)

print(result_datetime.strftime("%Y-%m-%d"))
