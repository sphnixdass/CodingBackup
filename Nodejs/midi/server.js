const midi = require("midi");
const express = require("express");
var cors = require('cors')

const input = new midi.Input();

var keypressed = [66];
var keyRandom = [60];
var keyRandombase = [50];
var connectkeyboard = true;

function midion() {
  // Count the available input ports.
  input.getPortCount();
  console.log(input.getPortCount(), input.getPortName(1));
  // Get the name of a specified input port.
  input.getPortName(1);

  // Configure a callback.
  input.on("message", (deltaTime, message) => {
    // The message is an array of numbers corresponding to the MIDI bytes:
    //   [status, data1, data2]
    // https://www.cs.cf.ac.uk/Dave/Multimedia/node158.html has some helpful
    // information interpreting the messages.
    [keyup, keyid, keypressure] = message;
    if (keyup === 144) {
      console.log(`m: ${message} d: ${deltaTime}`, keyid);
      keypressed = [];
      keypressed.push(keyid);
    }
  });

  // Open the first available input port.
  input.openPort(1);
  
  // Sysex, timing, and active sensing messages are ignored
  // by default. To enable these message types, pass false for
  // the appropriate type in the function below.
  // Order: (Sysex, Timing, Active Sensing)
  // For example if you want to receive only MIDI Clock beats
  // you should use
  // input.ignoreTypes(true, false, true)
  input.ignoreTypes(false, false, false);

  // ... receive MIDI messages ...
}
// Set up a new input.

function midioff() {
  input.closePort();
  console.log("input port closed");
}

midion();

const app = express();

app.use(cors());
app.use(express.static(__dirname + "/public"));

function randomKey(startnum, rangenum) {
  return Math.floor(Math.random() * rangenum) + startnum;
}

function udpatekey(){
  // let a = keyRandom[1];
  let b = keyRandom[2];
  keyRandom = [];
  // keyRandom.push(a);
  // keyRandom.push(b);
  keyRandom.push(randomKey(60, 20));


}

function udpatekeyb(){
  // let a = keyRandom[1];
  let b = keyRandombase[2];
  keyRandombase = [];
  // keyRandombase.push(a);
  // keyRandombase.push(b);
  // keyRandombase.push(randomKey(48, 12));
  keyRandombase.push(randomKey(56, 4));


}

app.get("/keyboardoutput", (req, res) => {
    res.contentType('application/json');
    res.send(JSON.stringify({keypressed, keyRandom, keyRandombase}));
    res.end();
    if (connectkeyboard === true) {
      console.log("keyboard value : ", keyRandom[0], keypressed[0], keyRandom.length, keyRandombase.length, keyRandombase[0]) ;
      if (keyRandom.length === 1) {
        keyRandom[0] === keypressed[0]? udpatekey() : null;
      } 
      if (keyRandombase.length == 1){
        keyRandombase[0] === keypressed[0]? udpatekeyb() : null;
      }
    } else {
      udpatekey();
      udpatekeyb()

    }
    
    // udpatekey();
    
  //res.send(200);
});

const PORT = 3007;
app.listen(PORT, () => {
  console.log("server is running on ", PORT);
});
