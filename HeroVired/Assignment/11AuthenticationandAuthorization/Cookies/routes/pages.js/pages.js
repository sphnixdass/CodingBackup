const express = require('express')
const router = express.Router();
const authController = require('../controllers/auth');

router.get('/', (req, res) => {
    res.render('login');
});

router.get('/login', (req, res) => {
    res.render('login');
});
router.get('/register', (req, res) => {
    res.render('register');
    // res.send("hi");
});
router.get('/welcome', authController.isLoggedIn, (req, res) => {
    if (req.user){
        res.render('welcome', {
            user: req.user
        }) ;
    } else {
        res.render('login', {message: 'User Must login'})
    }
    // res.send("hi");
});


module.exports = router;
