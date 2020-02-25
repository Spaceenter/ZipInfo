import csv

template = """
<head>

  <link rel="stylesheet" href="https://cdn.datatables.net/1.10.20/css/jquery.dataTables.min.css">
  <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
  <script src="https://cdn.datatables.net/1.10.20/js/jquery.dataTables.min.js"></script>
  <script src="index.js"></script>

</head>

<body>

  <table id="my-table">
    <thead>
      <tr>
        <th>Zip Code</th>
        <th>Population</th>
        <th>A Ratio</th>
        <th>W Ratio</th>
        <th>B Ratio</th>
        <th>Median Age</th>
        <th>Median Income</th>
      </tr>
    </thead>
    <tbody>
%s
    </tbody>
  </table>

</body>
"""

s = '\n'
with open('zip_info.csv', 'r') as f:
  reader = csv.reader(f)
  for i, line in enumerate(reader):
    if i == 0:
      continue

    line_s = '      <tr> '
    skip = False

    for item in line:
      if item == '':
        skip = True
        break

      if item == '0.000000':
        item = '0'
      if item == '1.000000':
        item = '1'

      line_s += '<th> ' + item + ' </th> '

    if skip:
      continue

    line_s += '</tr>\n'
    s += line_s

print(template % (s))
