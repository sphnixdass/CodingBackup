//https://www.youtube.com/watch?v=o9e3ex-axzA

const express = require('express');
const app = express();
const bodyParser = require('body-parser');
const {engine} = require('express-handlebars');
//const mongoose = require('mongoose');
//const cors = require('cors');
//const config = require('./config/database');
const path = require('path');
const dotenv = require('dotenv');
const cookieParser = require('cookie-parser');
const passport = require('passport');
const cookieSession = require('cookie-session');
const cors = require('cors');
require('./passport-config');
// const GoogleStrategy = require( 'passport-google-oauth2' ).Strategy;

dotenv.config({ path: './.env' });

const publicdir = path.join(__dirname,"./public");

const connection = require("./db");
connection();

app.use(express.static(publicdir));
app.use(cors());
app.use(express.urlencoded({extended: false}));
app.use(express.json());
app.use(cookieParser());
app.use(cookieSession({
    name: 'Dass-session',
    keys: ['key1', 'key2']
  }));
app.use(passport.initialize());
app.use(passport.session());


app.set('views',__dirname   + '/views');
app.engine('hbs', engine({extname: 'hbs', defaultLayout: 'index', layoutsDir: __dirname + '/views'}));
app.set('view engine', 'hbs');

// app.set('view engine', 'hbs');

// app.get('/', (req, res) => {
//     res.render('home', {displayresult: false});
// });

app.use('/', require('./routes/pages'));
app.use('/auth', require('./routes/auth'));

app.listen(3000, () => {
    console.log('Server started on port 3000');
})
