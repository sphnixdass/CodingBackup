require('./models/db');
const express = require('express');
const expresshbs = require('express-handlebars');
const router = require('./controllers/productControllers');
const path = require('path');

const app = express();

app.set('views', path.join(__dirname,'/views/'))
app.engine('hbs', expresshbs({extname: 'hbs', defaultLayout: 'mainLayout', layoutsDir: __dirname + '/views/layouts'}))
app.set('view engine', 'hbs');
app.use(express.urlencoded({extensions: true}))



// app.get('/', function(req, res, next){
    //     res.render(__dirname + '/views/addProducts')
    // })
    
    
    
    
    app.listen(3002);
    app.use('/', router);
