const $ = window.$;
const url = 'https://fourtonfish.com/hellosalut/?lang=';

$(document).ready(function () {
  $('#btn_translate').click(function () {
    getData();
  });

  $('#language_code').keypress(function (event) {
    if (event.which === 13) {
      getData();
    }
  });

  function getData () {
    const langStr = $('#language_code').val();
    $.getJSON(url + langStr, function (resp) {
      const hello = resp.hello;
      $('#hello').text(hello);
    });
  }
});
