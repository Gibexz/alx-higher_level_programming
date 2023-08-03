$(document).ready(function () {
  $('#add_item').on('click', function () {
    /* const item = '<li>Item</li>'; */
    $('ul.my_list').append('<li>Item</li>');
  });
});
