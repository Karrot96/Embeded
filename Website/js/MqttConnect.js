var mqtt = require('mqtt')
var client  = mqtt.connect('http://192.168.0.10')
const express = require('express')
const app = express()
const bodyParser = require('body-parser');
app.use(express.static('public'));
app.set('view engine', 'ejs')
app.use(bodyParser.urlencoded({ extended: true }));
var obj = JSON.parse('{"RemoveFog": "True", "WindowFogged": "false", "name":"fog" , "value": "100" }')
const notifier = require('node-notifier');
const path = require('path');
const opn = require('opn');


client.on('connect', function () {
  client.subscribe('ESYS/netball')
  //client.publish('ESYS/netball', '')
})


client.on('message', function (topic, message) {
  // message is Buffer
  obj = JSON.parse(message);
  console.log(obj.WindowFogged.toString())
  if (obj.WindowFogged && !obj.RemoveFog){
      notifier.notify({
        title: 'FogMeister',
        message: 'Hello, Your car windscreen is currently fogged up',
        icon: path.join(__dirname, 'coulson.jpg'), // Absolute path (doesn't work on balloons)
        sound: true, // Only Notification Center or Windows Toasters
        wait: true // Wait with callback, until user action is taken against notification
      }, function (err, response) {
        // Response is response from notification
      });
  }else if (obj.RemoveFog){
      notifier.notify({
        title: 'FogMeister',
        message: 'Your car it now demisting',
        icon: path.join(__dirname, 'coulson.jpg'), // Absolute path (doesn't work on balloons)
        sound: true, // Only Notification Center or Windows Toasters
        wait: true // Wait with callback, until user action is taken against notification
      }, function (err, response) {
        // Response is response from notification
      });
  }else if (!obj.WindowFogged){
      notifier.notify({
        title: 'FogMeister',
        message: 'Your car it no longer fogged up',
        icon: path.join(__dirname, 'coulson.jpg'), // Absolute path (doesn't work on balloons)
        sound: true, // Only Notification Center or Windows Toasters
        wait: true // Wait with callback, until user action is taken against notification
      }, function (err, response) {
        // Response is response from notification
      });
  }
  //client.end()
})
notifier.on('timeout', function() {
  console.log('Timed out!');
  if (obj.WindowFogged && !obj.RemoveFog){
      notifier.notify({
        title: 'FogMeister',
        message: 'Hello, Your car windscreen is currently fogged up',
        icon: path.join(__dirname, 'coulson.jpg'), // Absolute path (doesn't work on balloons)
        sound: true, // Only Notification Center or Windows Toasters
        wait: true // Wait with callback, until user action is taken against notification
      }, function (err, response) {
        // Response is response from notification
      });
  }
});
notifier.on('click', (obj, options) => {
    opn('http://localhost:8080');
});

app.get('/', function (req, res) {
  //var client  = mqtt.connect('http://192.168.0.10')
  //client.subscribe('ESYS/netball')
  console.log(obj.WindowFogged)
  if ((obj.WindowFogged.toString() == "true") && (obj.RemoveFog.toString() == "false")){
      res.render('index', {display:"Demist"})
  }else if(obj.RemoveFog.toString() == "true"){
      res.render('index', {display:"Removing"})
  }else{
      res.render('index', {display: "AllGood"})
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
