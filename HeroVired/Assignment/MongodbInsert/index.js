const express = require('express');
const expresshbs = require('express-handlebars');
const router = require('./controller/mainController');

const app = express();

app.use(express.static(__dirname + '/public'));

app.set('views', './views/');
app.engine('hbs', expresshbs({extname: 'hbs', defaultLayout: 'mainLayout', layoutsDir: './views/layouts'}))
app.set('view engine', 'hbs');
app.use(express.urlencoded({extensions: true}))

app.use('/', router);

app.listen(3005);