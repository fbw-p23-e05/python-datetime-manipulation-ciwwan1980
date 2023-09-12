from datetime import datetime, timedelta


current_date = datetime(year=2020, month=1, day=1)

day_toPay = current_date + timedelta(days=25)

day_toPay_formatted = day_toPay.strftime("%d %B, %Y")
print(day_toPay_formatted, "day_toPay_formatted ")

message = f"Hello Friedrich, your rent of 300 € is due on {day_toPay_formatted}."

print(message)
