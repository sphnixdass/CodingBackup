require("dotenv").config();
const connection = require("./db");
const express = require('express');
const bodyParser = require("body-parser");
const expresshbs = require('express-handlebars');
const router = require('./controller/mainController');
const cookieParser = require("cookie-parser");

connection();

const app = express();
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));
app.use(cookieParser());

app.use(express.static(__dirname + '/public'));

app.set('views', './views/');
app.engine('hbs', expresshbs({extname: 'hbs', defaultLayout: 'mainLayout', layoutsDir: './views/layouts'}))
app.set('view engine', 'hbs');
app.use(express.urlencoded({extensions: true}))

app.use('/', router);





const PORT = process.env.PORT;
app.listen(PORT, ()=>{ console.log("server is running on ", PORT)});

