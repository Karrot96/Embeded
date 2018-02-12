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
  if (obj.WindowFogged){
      res.render('index', {display:true})
  }else{
      res.render('index', {display:false})
  }
  client.end()
})

app.use(express.static('public'));
app.set('view engine', 'ejs')
app.use(bodyParser.urlencoded({ extended: true }));

app.get('/', function (req, res) {
  res.render('index', {display:false})
  var client  = mqtt.connect('http://192.168.0.10')
  client.subscribe('ESYS/netball')
})

app.post('/', function (req, res) {
  res.render('index', {display:false})
  console.log(req.body.city);
  var client  = mqtt.connect('http://192.168.0.10')
  var x = '{"RemoveFog": "True", "WindowFogged": "True", "name":"fog" , "value": "100" }'
  var x = JSON.parse(x)
  var client  = mqtt.connect('http://192.168.0.10')
  client.publish('ESYS/netball', Buffer.from(JSON.stringify(x)))

})

app.listen(8080, function () {
  console.log('Example app listening on port 8080!')
})
