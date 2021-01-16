
//18.2
alert(/^http?/.test('https://nke.ru'));

//18.4
alert(/\w+\.jpe?g/.test('image.jpeg'));

//18.6
alert(/\d{1,12}/.test('71247'));

//18.8
alert(/^\d{1,2}.\d{1,2}.\d{4}/.test('5.08.2022'));

//18.10
alert(/(^[^.][a-z\d._-]+[^.])@([a-z]{4})\.([a-z]{2,3})/.test('nke@mail.ru'))