import re

s = 1
m = 60 * s
h = 60 * m
d = 24 * h
y = 365.25 * d


def parse(second):
  if not isinstance(second, str):
    return second

  pattern = re.compile(
      '^((?:\d+)?\.?\d+) *(seconds?|secs?|s|minutes?|mins?|m|hours?|hrs?|h|days?|d|years?|yrs?|y)?$',
      re.IGNORECASE)

  match = pattern.match(second)

  if match is None:
    return second

  n, t = float(match.group(1)), str(match.group(2)).lower()

  if t in ['years', 'year', 'yrs', 'yr', 'y']:
    n = n * y
  elif t in ['days', 'day', 'd']:
    n = n * d
  elif t in ['hours', 'hour', 'hrs', 'hr', 'h']:
    n = n * h
  elif t in ['minutes', 'minute', 'mins', 'min', 'm']:
    n = n * m
  elif t in ['seconds', 'second', 'secs', 'sec', 's']:
    n = n * s

  return n
