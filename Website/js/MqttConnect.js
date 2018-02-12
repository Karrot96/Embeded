var mqtt = require('mqtt')
var client  = mqtt.connect('http://192.168.0.10')
const express = require('express')
const app = express()
const bodyParser = require('body-parser');
app.use(express.static('public'));
app.set('view engine', 'ejs')
app.use(bodyParser.urlencoded({ extended: true }));
var obj = JSON.parse('{"RemoveFog": "True", "WindowFogged": "False", "name":"fog" , "value": "100" }')

client.on('connect', function () {
  client.subscribe('ESYS/netball')
  //client.publish('ESYS/netball', '')
})


client.on('message', function (topic, message) {
  // message is Buffer
  obj = JSON.parse(message);
  console.log(obj.WindowFogged.toString())
  //client.end()
})

app.get('/', function (req, res) {
  //var client  = mqtt.connect('http://192.168.0.10')
  //client.subscribe('ESYS/netball')
  console.log(obj.WindowFogged)
  if (obj.WindowFogged.toString() == "true"){
      res.render('index', {display:"true"})
  }else{
      res.render('index', {display:"false"})
  }
})

app.post('/', function (req, res) {
  //var client  = mqtt.connect('http://192.168.0.10')
  var x = '{"RemoveFog": "true", "WindowFogged": "true", "name":"fog" , "value": "100" }'
  var x = JSON.parse(x)
  //var client  = mqtt.connect('http://192.168.0.10')
  client.publish('ESYS/netball', Buffer.from(JSON.stringify(x)))

})

app.listen(8080, function () {
  console.log('Example app listening on port 8080!')
})
