var http = require('http');
var fs = require('fs');
http.createServer(function (req, res) {
  fs.readFile('app.html', function(err, data) {
    res.writeHead(200, {'Content-Type': 'text/html'});
    res.write(data);
    res.end();
  });
}).listen(8080);


var mqtt = require('mqtt')
var client  = mqtt.connect('http://192.168.0.10')

client.on('connect', function () {
  client.subscribe('ESYS/netball')
  //client.publish('ESYS/netball', '')
})

client.on('message', function (topic, message) {
  // message is Buffer
  var obj = JSON.parse(message);
  console.log(obj.toString())
  client.end()
})
