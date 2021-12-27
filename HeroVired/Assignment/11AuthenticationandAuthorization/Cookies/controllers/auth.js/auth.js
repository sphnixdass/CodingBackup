const jwt = require('jsonwebtoken');
const bcrypt= require('bcryptjs');
const mongomodel = require('../models/loginModel');
const {promisify} = require('util');



exports.login = async (req, res) =>{
    console.log(req.body);

    try {
        const {emailAddress, password} = req.body;
        if(!(emailAddress && password)){
            res.status(401).render('login', {message: 'Email and Password is required'})    
        }
        const user = await mongomodel.findOne({emailAddress});
        if (user == null)
        {
            res.status(401).render('login', {message: 'You are not registed'})    
        }

        if(user && (await bcrypt.compare(password, user.password)))
        {
           
            const token = jwt.sign({user_id: user._id, emailAddress}, process.env.JWT_SECERT, {
                expiresIn: process.env.JWT_EXPIRES_IN
            });
    
            console.log("the token is: ", token);
            const cookieOptions = {
                expires: new Date(
                    Date.now() + process.env.JWT_COOKIE_EXPIRES * 24 * 60 * 60 * 1000
                ),
                httpOnly: true
            }
    
            res.cookie('jwt', token, cookieOptions);
            res.status(200).redirect('/welcome');

        } else {
            res.status(401).render('login', {message: 'Email or Password is incorrect'})
            
        }


    }
    catch (err) {
        console.log("err", err);
      }
    
};


exports.register = async (req, res) => {
    console.log(req.body);
    
    try {
        
        const {emailAddress, password, firstName, lastName, genderOptions, passwordconfirm} = req.body;
        if (!(emailAddress && password && firstName)) {
            res.status(401).render('register', {message: 'All inputs are required'});
          } else if (password !== passwordconfirm) {
            res.status(401).render('register', {message: 'passwords are not matched'});
          } else {
          
          const oldUser = await mongomodel.findOne({ emailAddress });
          if (oldUser) {
            res.status(401).render('register', {message: 'User Already Exist.'});

        } else {

            let hashedpassword = await bcrypt.hash(password, 8);


            var insertobj = new mongomodel();
            insertobj.emailAddress = emailAddress;
            insertobj.firstName = firstName;
            insertobj.lastName = lastName;
            insertobj.password = hashedpassword;
            insertobj.genderOptions = genderOptions;

            insertobj.save((err, data)=>{
                if(!err){
                    res.status(200).render('register', {message: 'Successfully registed'})
                } else {
                    res.status(200).render('register', {message: 'Unable to register'})
                    console.log("error", err);
                }
            })

        }
    }
    // res.send("form submissted");


    }catch (err) {
      console.log("err", err);
    }
    

    

};

exports.isLoggedIn = async(req, res, next) => {
    req.message = "Inside middleware";
    console.log(req.cookies);
    if(req.cookies.jwt)
    {
        try {
            const decoded = await promisify(jwt.verify)(req.cookies.jwt, process.env.JWT_SECERT);
            const user_id = decoded.user_id;
            const user = await mongomodel.findOne({user_id});
            console.log(decoded, decoded.user_id, user);
            if (user == null)
            {
                return next();   
            } else {
                req.user = user.firstName;
                return next();
            }

        } catch (error) {
            console.log(error);
        }
    } else {

        next();
    }
};

exports.logout = async(req, res, next) => {
    res.cookie('jwt', 'logout', {
        expires: new Date(Date.now() + 1000),
        httpOnly:true
    });
    res.status(200).redirect('/')

};