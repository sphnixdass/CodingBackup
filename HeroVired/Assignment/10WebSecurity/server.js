const https = require('https');
const fs = require('fs');
const bodyParser = require("body-parser");
const path = require('path');

const express = require('express');
const {engine} = require('express-handlebars');
const app = express();
app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());

const searchlist = [];

const options = {
  key: fs.readFileSync('key.pem'),
  cert: fs.readFileSync('cert.pem')
};

app.set('views',__dirname   + '/views/layouts');
app.engine('hbs', engine({extname: 'hbs', defaultLayout: 'main', layoutsDir: __dirname + '/views/layouts'}));
app.set('view engine', 'hbs');


app.get('/', (req, res) => {
    res.render('home', {displayresult: false});
});

app.get('/clearresult', (req, res) => {
    res.render('home', {displayresult: false});
});

app.post('/submit', (req, res) => {
    console.log(req.body);
    searchlist.push(req.body.search);
    res.render('home', { displayresult: true, uname: req.body.uname, search: searchlist});
    });

https.createServer(options, app).listen(3000);
