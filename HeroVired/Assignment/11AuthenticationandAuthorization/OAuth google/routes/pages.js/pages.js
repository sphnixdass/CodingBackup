const express = require('express')
const router = express.Router();
const authController = require('../controllers/auth');
const passport = require('passport');

router.get('/', (req, res) => {
    res.render('login');
});

router.get('/google',
  passport.authenticate('google', { scope:
      [ 'email', 'profile' ] }
));

router.get( '/google/callback',
    passport.authenticate( 'google', {
        successRedirect: '/google/success',
        failureRedirect: '/google/failure'
}));

router.get('/google/success',(req, res) => {
    res.redirect('/welcome');
});

router.get('/google/failure',(req, res) => {
    res.redirect('/login');
});

// router.get('/google', passport.authenticate('google', { scope: ['profile', 'email'] }));

// router.get('/failed', (req, res) => res.send('You Failed to log in!'))

// router.get('/google/callback', passport.authenticate('google', { failureRedirect: '/failed' }),
//   function(req, res) {
//     // Successful authentication, redirect home.
//     res.redirect('/welcome');
//   }
// );

router.get('/login', (req, res) => {
    res.render('login');
});
router.get('/register', (req, res) => {
    res.render('register');
    // res.send("hi");
});
router.get('/welcome', authController.isLoggedIn, (req, res) => {
    console.log(req.user);

    if (req.user){
        res.render('welcome', {
            user: req.user.givenName
        }) ;
    } else {
        res.render('login', {message: 'User Must login'})
    }
    // res.send("hi");
});


module.exports = router;
