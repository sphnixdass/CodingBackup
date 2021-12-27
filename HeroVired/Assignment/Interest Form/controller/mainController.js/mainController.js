const express = require('express');
const router = express.Router();
const bcrypt = require("bcryptjs");
const jwt = require("jsonwebtoken");
const mongomodel = require("../model/mainModel");
const interestModel = require("../model/interestModel");
const auth = require("../middleware/auth");
const multer = require("multer");
const fs = require("fs");
const path = require('path');


var displayname = "";


router.get("/", (req, res) => {
    res.render('../views/home');
  });

  router.get("/welcome", auth, (req, res) => {
    res.status(200).render('../views/welcome', {"username" : displayname});
  });

  router.get("/login", auth, (req, res) => {
    console.log("ssss", req.url);
    res.status(200).render('../views/welcome');
  });

  router.get("/adminpage", auth, async (req, res) => {
    const cursorfirstname =[];

    var cursor = await interestModel.find({userstatus : "New"});
    cursor.forEach(element => {
      // console.log("item", element);
      cursorfirstname.push({"firstname" : element.firstname,"emailid" : element.emailid, "mobileno" : element.mobileno});

    });

    res.status(200).render('../views/adminpage', {"cursor" : cursorfirstname});
  });

  router.get("/interestform", auth, (req, res) => {
    res.status(200).render('../views/interestform');
  });

  router.get("/register", (req, res) => {
    res.status(200).render('../views/register');
  });


  router.get("/logout", (req, res) => {
    res.clearCookie("token");
    res.status(200).render('../views/login');
  });

  router.post("/updatestatus", async (req, res) => {
    // console.log(req.params);
    console.log("sssss", req.body);
    const oldUser = await interestModel.updateOne({firstname : req.body.username},{ $set: {userstatus: req.body.action} });
    res.status(200).render('../views/adminpage');

  });

  router.post("/login", async (req, res) => {
    console.log("sddddsssss", req.url, global.urlinfo);

    try {
      // Get user input
      const { username, password } = req.body;
      displayname = username;
  
      // Validate user input
      if (!(username && password)) {
        res.status(400).send("All input is required");
      }
      // Validate if user exist in our database
      const user = await mongomodel.findOne({ username });
      if (user == null)
      {
        res.status(200).redirect('/login');
      }
      if (user && (await bcrypt.compare(password, user.password))) {
        // Create token
        const token = jwt.sign(
          { user_id: user._id, username },
          process.env.secretkey,
          {
            expiresIn: "2h",
          }
        );
  
        // save user token
        user.token = token;
  
        // user
     
        res.cookie('token',token, { httpOnly: true, secure: false, maxAge: 3600000 })
        // res.status(200).json(user).redirect('/welcome');
        if (global.urlinfo == "/interestform")
        {
          res.status(200).redirect('/interestform');
        } else if (global.urlinfo == "/adminpage")
        {
          res.status(200).redirect('/adminpage');
        }
        else {
        res.status(200).redirect('/welcome');
        }
      }
      //res.status(400).send("Invalid Credentials");
    } catch (err) {
      console.log("err", err);
    }
  });

  


  router.post("/register", async (req, res) => {

    // Our register logic starts here
    try {
      // Get user input
      const { username, password } = req.body;
  
      // Validate user input
      if (!(password && username)) {
        res.status(400).send("All input is required");
      }
  
      // check if user already exist
      // Validate if user exist in our database
      const oldUser = await mongomodel.findOne({ username });
  
      if (oldUser) {
        return res.status(409).send("User Already Exist. Please Login");
      }
  
      //Encrypt user password
      encryptedPassword = await bcrypt.hash(password, 10);
  
      // Create user in our database
    //   const user = await mongomodel.create({
    //     username,
    //     password: encryptedPassword,
    //   });

      var insertobj = new mongomodel();
      insertobj.username = username;
      insertobj.password = encryptedPassword;

  
      insertobj.save((err, data)=> {
        if(!err){
            console.log("Success");
        }else {
            console.log("error", err);
        }
    });


      // Create token
      const token = jwt.sign(
        { user_id: mongomodel._id, username },
        "HeroSerectKey",
        {
          expiresIn: "2h",
        }
      );
      // save user token
      mongomodel.token = token;
  
      // return new user
      //res.status(201).json(mongomodel);
      res.status(201).redirect("/login");
      
    } catch (err) {
      console.log(err);
    }
    // Our register logic ends here
  });



  router.post("/interestform", async (req, res) => {


    // Our register logic starts here
    try {
      // Get user input
      const { fname, email, mobile } = req.body;
  
      var insertobj = new interestModel();
      insertobj.firstname = fname;
      insertobj.emailid = email;
      insertobj.mobileno = mobile;
      insertobj.userstatus = "New";

  
      insertobj.save((err, data)=> {
        if(!err){
            console.log("Success");
        }else {
            console.log("error", err);
        }
    });

    
      res.status(201).redirect("/");
      
    } catch (err) {
      console.log(err);
    }
    // Our register logic ends here
  });

module.exports = router;