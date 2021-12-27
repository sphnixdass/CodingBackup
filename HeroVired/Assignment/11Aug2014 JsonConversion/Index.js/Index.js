var express = require('express');
var bodyParser = require('body-parser');
var multer = require('multer');
//var upload = multer();
var app = express();

const fs = require("fs");
const files = fs.readFileSync("Index.html");
const ajaxIndex = fs.readFileSync("AjexIndex.html");
const outputTxt = fs.readFileSync("outputTxt.txt");

// for parsing application/json
app.use(bodyParser.json()); 

// for parsing application/xwww-
app.use(bodyParser.urlencoded({ extended: true })); 
//form-urlencoded

// for parsing multipart/form-data
//app.use(upload.array()); 
app.use(express.static('public'));

app.post('/', function(req, res, next){
   console.log(req.body.firstName);
   console.log(req.body.lastName);
   
   var Person = {
    firstName: req.body.firstName,
    lastName: req.body.lastName}

    stringData = JSON.stringify(Person);


   fs.writeFile('outputTxt.txt', stringData, err => {
    if (err) {
      console.error(err)
      return
    }
    //file written successfully
  })


   res.setHeader("Content-Type", "text/html");
   res.end(ajaxIndex);

   //res.send("recieved your request!");
   //next();
});

app.get('/', function(req, res){
    res.statusCode = 200;
    // give correct input for html
    res.setHeader("Content-Type", "text/html");
    res.end(files);
 });

 app.get('/demo_get.txt', function(req, res){
    res.statusCode = 200;
    // give correct input for html
    res.setHeader("Content-Type", "text/html");
    res.end(outputTxt);
 });


 app.listen(3000,() => {
    console.log("Started on PORT 3000");
})


