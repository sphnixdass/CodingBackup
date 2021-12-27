const express = require('express');
const app = express();
const bodyParser = require('body-parser');
const {engine} = require('express-handlebars');
const cors = require('cors');
//const mongoose = require('mongoose');
//const cors = require('cors');
//const config = require('./config/database');
const path = require('path');
const dotenv = require('dotenv');
const cookieParser = require('cookie-parser');

dotenv.config({ path: './.env' });

const publicdir = path.join(__dirname,"./public");

const connection = require("./db");
connection();

app.use(express.static(publicdir));
app.use(express.urlencoded({extended: false}));
app.use(express.json());
app.use(cookieParser());
app.use(cors({
    methods: 'GET,POST,PATCH,DELETE,OPTIONS',
    optionsSuccessStatus: 200,
    origin: 'http://localhost:3000/welcome'
  }));
  app.options('*', cors());

//app.use(cors({origin: 'http://localhost:3000/welcome'}));
// app.use(function (req, res, next) {

//     // Website you wish to allow to connect
//     res.setHeader('Access-Control-Allow-Origin', 'http://localhost:3000/welcome');

//     // Request methods you wish to allow
//     res.setHeader('Access-Control-Allow-Methods', 'GET, POST, OPTIONS, PUT, PATCH, DELETE');

//     // Request headers you wish to allow
//     res.setHeader('Access-Control-Allow-Headers', 'X-Requested-With,content-type');

//     // Set to true if you need the website to include cookies in the requests sent
//     // to the API (e.g. in case you use sessions)
//     res.setHeader('Access-Control-Allow-Credentials', true);

//     // Pass to next layer of middleware
//     next();
// });


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
