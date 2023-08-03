const urlapi = 'https://fourtonfish.com/hellosalut/?lang=fr';

$.get(urlapi, data => {
  $('DIV#hello').text(data.hello);
});
