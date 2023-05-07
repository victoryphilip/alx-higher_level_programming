const $ = window.$;
const url = 'https://fourtonfish.com/hellosalut/?lang=';

$(document).ready(function () {
  $('#btn_translate').click(function () {
    const langStr = $('#language_code').val();

    $.getJSON(url + langStr, function (resp) {
      const hello = resp.hello;
      $('#hello').text(hello);
    });
  });
});
