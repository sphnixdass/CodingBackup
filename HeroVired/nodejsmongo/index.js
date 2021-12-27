var express = require('express');
var app = express();


// const mongoose = require('mongoose');
// mongoose.connect('mongodb://127.0.0.1:27017/dassdb');

// const dassSchema = mongoose.Schema({name: String, age: Number});

// const dass = mongoose.model('students', dassSchema);

// const inst1 = new dass({name: 'Dass', age: 10});

// inst1.save().then(() => console.log('Saved'));

const students = require('./students');
app.use('/', students);



app.listen(3000);
// app.use(function (req, res, next) {

//     console.log("Time is :", Date.now())
//     next();
// });

// app.use(function (req, res, next) {

//     console.log("Time is 2:", Date.now())
//     next();
// }, function (req, res, next) {

//     console.log("Time is 2:", Date.now())
//     next();
// });

// app.get('/', function (req, res, next){

//     next();
// });

