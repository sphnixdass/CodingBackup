const express = require('express');
const fs = require('fs');
const bodyParser = require("body-parser");
const path = require('path');
const bcrypt = require('bcrypt');
const saltRounds = 10;
const myPlaintextPassword = 'Welcome@Hero';
const sanitizer = require('sanitize');



const {engine} = require('express-handlebars');
const app = express();
const { check, validationResult } = require('express-validator');
app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());



app.set('views',__dirname   + '/views/layouts');
app.engine('hbs', engine({extname: 'hbs', defaultLayout: 'main', layoutsDir: __dirname + '/views/layouts'}));
app.set('view engine', 'hbs');




var loginValidate = [
    // Check Username
    check('username', 'Username Must Be an Email Address').isEmail()
    .trim().escape().normalizeEmail(),
    // Check Password
    check('password').isLength({ min: 8 }).withMessage('Password Must Be at Least 8 Characters').matches('[0-9]').withMessage('Password Must Contain a Number').matches('[A-Z]').withMessage('Password Must Contain an Uppercase Letter').trim().escape()];

    

app.get('/login', (req, res) => {
    res.render('login', {displayresult: false});
});

app.get('/clearresult', (req, res) => {
    res.render('login', {displayresult: false});
});

app.post('/login', loginValidate, (req, res) => {
    const errors = validationResult(req);
    if (!errors.isEmpty()) {
        //return res.status(422).json({ errors: errors.array() });
        return res.render('login', {errors: errors.array()});

    }
    else {
  // Insert Login Code Here
  let username = req.body.username;
  let password = req.body.password;
  bcrypt.genSalt(saltRounds, function(err, salt) {
    bcrypt.hash(password, salt, function(err, hash) {
        console.log(hash);
        fs.writeFile('./users/' + username + '.txt', hash, function (err) {
            if (err) throw err;
            console.log('Saved!');
            return res.render('welcome', {username: username, isLoggedIn: true});
        });
    });
});
}
});

    

app.post('/submit', (req, res) => {
    console.log(req.body);
    searchlist.push(req.body.search);
    res.render('home', { displayresult: true, uname: req.body.uname, search: searchlist});
    });

app.listen(4000, () => {
    console.log('Server started on port 4000');
});