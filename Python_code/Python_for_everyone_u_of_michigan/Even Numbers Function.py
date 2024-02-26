def evens():
  i = 0
  while True:
    yield i
    i += 2
iterator = evens()
for i in range(1000):
  print(iterator.__next__())