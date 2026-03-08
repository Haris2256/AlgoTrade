from source.deprecated import variables
from source.bots import bot
from source.bots import dumbass
from datetime import datetime
from source.common.state import State

start_date = "2020-07-03"
end_date = "2025-08-05"
date_format = variables.date_format

start = datetime.strptime(start_date, date_format)
end = datetime.strptime(end_date, date_format)

num_days = (end - start).days
money = 100000

b = dumbass.Dumbass()

for i in range (num_days):

    actions = b.act(state)
