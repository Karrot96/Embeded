//Node.js module


//Node.js mqtt module
var mqtt = require('mqtt')
var client  = mqtt.connect('http://192.168.0.10')

//Node.js express Module
const express = require('express')
const app = express()
const bodyParser = require('body-parser');
app.use(express.static('public'));
app.set('view engine', 'ejs')
app.use(bodyParser.urlencoded({ extended: true }));

//Node.js notifier module
const notifier = require('node-notifier');
const path = require('path');

//Node.js opn module
const opn = require('opn');


//Global Json variable for passing data around the device, initialised on server Starting
//Would be quickly overwritten as soon as a device starts transmitting data
var obj = JSON.parse('{"RemoveFog": "True", "WindowFogged": "false", "name":"fog" , "value": "100" }')


//Connect to the MQTT broker
client.on('connect', function () {
    //subscribe to the correct Topic
    client.subscribe('ESYS/netball')
})

//When the broker gets updated
client.on('message', function (topic, message) {
    //global json object is updated to hold the message uploaded to the broker topic
    obj = JSON.parse(message);
    console.log(obj.WindowFogged.toString())

    //The data from the broker is analysed
    //Different notifications are posted depending on the condition of the car
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
})


//Checks if the notification timesout
notifier.on('timeout', function() {
  console.log('Timed out!');
  //If car is fogged dont let the timeout remove the notification
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

//when clicking on the notification open up the browser
notifier.on('click', (obj, options) => {
    opn('http://localhost:8080');
});


//On browser refresh determine what stage we are in and display corresponding page
app.get('/', function (req, res) {
  console.log(obj.WindowFogged)
  if ((obj.WindowFogged.toString() == "true") && (obj.RemoveFog.toString() == "false")){
      res.render('index', {display:"Demist"})
  }else if(obj.RemoveFog.toString() == "true"){
      res.render('index', {display:"Removing"})
  }else{
      res.render('index', {display: "AllGood"})
  }
})


//On a submit of a form tell the device to turn on the ability to demist the car
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
