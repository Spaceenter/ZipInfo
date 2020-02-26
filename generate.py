import csv

s = 'var zipInfo = [\n'
with open('zip_info.csv', 'r') as f:
  reader = csv.reader(f)
  for i, line in enumerate(reader):
    if i == 0:
      continue

    line_s = '  ['
    skip = False
    first = True

    for item in line:
      if item == '':
        skip = True
        break

      if item == '0.000000':
        item = '0'
      if item == '1.000000':
        item = '1'

      if not first:
        line_s += ', '
      else:
        first = False
      line_s += item

    if skip:
      continue

    line_s += '],\n'
    s += line_s

s += '];'

print(s)
