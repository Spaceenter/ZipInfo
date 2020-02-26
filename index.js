$(function() {
  let myTable = $('#my-table').DataTable({deferRender: true});
  for (let z of zipInfo) {
    myTable.row.add(z).draw(false);
  }
});
