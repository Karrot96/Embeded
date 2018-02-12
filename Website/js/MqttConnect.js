var mqtt = require('mqtt')
var client  = mqtt.connect('http://192.168.0.10')
const express = require('express')
const app = express()
const bodyParser = require('body-parser');

client.on('connect', function () {
  client.subscribe('ESYS/netball')
  //client.publish('ESYS/netball', '')
})

client.on('message', function (topic, message) {
  // message is Buffer
  var obj = JSON.parse(message);
  console.log(obj.value.toString())
  client.end()
})

app.use(express.static('public'));
app.set('view engine', 'ejs')
app.use(bodyParser.urlencoded({ extended: true }));

app.get('/', function (req, res) {
  res.render('index');
})

app.post('/', function (req, res) {
  res.render('index');
  console.log(req.body.city);
  client.publish('ESYS/netball', '{"name":"fog" , "value": "100" ,  "WindowFogged": "True", "RemoveFog": "True"}')

})

app.listen(8080, function () {
  console.log('Example app listening on port 8080!')
})
