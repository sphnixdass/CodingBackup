const express = require('express');
const app = express();
const handlebars = require('express-handlebars').create({ defaultLayout:'main' });


const fortune = require('./lib/fortune.js');


app.set("port", process.env.PORT || 3002);
app.use(express.static(__dirname + '/public'));





// set up handlebars view engine
app.engine('handlebars', handlebars.engine);
app.set('view engine', 'handlebars');


app.get('/', function(req, res){
    res.type('text/plain');
    res.send('Meadowlark Travel');
});

app.get('/about', function(req, res){
    // res.type('text/plain');
    // res.send('About Meadowlark Travel');
    
    res.render('about',{ fortune: fortune.getFortune()});

});



app.get('/home', function(req, res){
    res.render('home');
});


app.use(function (req, res){
    res.type('text/plain');
    res.status(404);
    res.send('404 file not found');
});

app.use(function (err, req, res, next){
    console.log(err.stack);
    res.type('text/plain');
    res.status(500);
    res.send('500 server error');
});

app.listen(app.get("port"),function(){
    console.log( 'Express started on http://localhost:' +
    app.get('port') + '; press Ctrl-C to terminate.' );
});