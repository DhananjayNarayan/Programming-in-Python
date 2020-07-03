daily_sales_replaced = daily_sales.replace(';,;', '#')

daily_transactions = daily_sales_replaced.split(',')

daily_transactions_split = []


for i in daily_transactions:
  daily_transactions_split.append(i.split('#'))

transactions_clean = []

for a in daily_transactions_split:
  inner = []
  for i in a:
    inner.append(i.strip())
  transactions_clean.append(inner)

customers = []
sales = []
thread_sold = []
date = []

for a in transactions_clean:
  customers.append(a[0])
  sales.append(a[1])
  thread_sold.append(a[2])
  date.append(a[3])

total_sales = 0

for i in sales:
  first = float(i.strip('$'))
  total_sales += first

thread_sold_split = []

for i in thread_sold:
  if i.find('&') > 0:
    lst = i.split('&')
    for x in lst:
      thread_sold_split.append(x)
  else: thread_sold_split.append(i)


def colour_count(colour, lst):
  count = lst.count(colour)
  return count

colours = ['red','yellow','green','white','black','blue','purple']

phrase = \
"""
Thread Shed sold {count} threads of {colour} thread today.
"""

for i in colours:
  count = colour_count(i, thread_sold_split)
  string = phrase.format(count=count, colour=i)
  print(string)
