$(function() {
  let myTable = $('#my-table').DataTable({
    deferRender: true,
    pageLength: 50,
  });
  for (let z of zipInfo) {
    z[0] = '<a href="https://google.com/maps?q=' + z[0] + '" target="_blank">' +
        z[0] + '</a>';
    myTable.row.add(z);
  }
  myTable.draw();
});
