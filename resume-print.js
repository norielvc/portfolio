if (new URLSearchParams(location.search).get('print') === '1') {
  window.addEventListener('load', function () {
    setTimeout(function () {
      window.print();
    }, 400);
  });
}
