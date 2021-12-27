var express = require('express');
var router = express.Router();

const mongoose = require('mongoose');
mongoose.connect('mongodb://127.0.0.1:27017/dassdb');

const dassSchema = mongoose.Schema({name: String, age: Number});

const dass = mongoose.model('students', dassSchema);


router.get('/', function (req, res){
    res.send("sutdents home page");
});

router.get('/about', function (req, res){
    res.send('About this wiki');
});

router.get('/find', function (req, res){
    dass.find({'name': 'dass'}, function(err, data){
        if(!err) {
            res.send(data);

        }
    });
});

router.use((req, res, next) => {
    console.log('Got a request!');
  });
   
  router.get('/shirts', (req, res, next) => {
    console.log('Requesting shirts!');
  });

router.get('/users/:name/purchases/:purchaseId', function (req, res){
    console.log(req.params );
});


module.exports = router;