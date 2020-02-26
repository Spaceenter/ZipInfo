$(function() {
  let myTable = $('#my-table').DataTable({
    deferRender: true,
    pageLength: 50,
  });
  for (let z of zipInfo) {
    myTable.row.add(z);
  }
  myTable.draw();
});
