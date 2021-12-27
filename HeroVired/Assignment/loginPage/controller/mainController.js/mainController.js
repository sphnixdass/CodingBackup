const express = require('express');
const router = express.Router();
const bcrypt = require("bcryptjs");
const jwt = require("jsonwebtoken");
const mongomodel = require("../model/mainModel");
const imageModel = require("../model/imageModel");
const auth = require("../middleware/auth");
const multer = require("multer");
const fs = require("fs");
const path = require('path');


var displayname = "";



// SET STORAGE
var storage = multer.diskStorage({
    destination: function (req, file, cb) {
      cb(null, 'uploads')
    },
    filename: function (req, file, cb) {
      cb(null, file.fieldname + '-' + Date.now())
    }
  })
  var upload = multer({ storage: storage })

  router.post("/uploadphoto",upload.single('myImage'),(req,res)=>{
    var img = fs.readFileSync(req.file.path);
    var encode_img = img.toString('base64');
    var final_img = {
        contentType:req.file.mimetype,
        filePath:req.file.path,
        img: {
            data: new Buffer(encode_img,'base64'),
            contentType: req.file.mimetype
        },
        username:displayname
    };
    imageModel.create(final_img,function(err,result){
        if(err){
            console.log("Image updated error ", err);
        }else{
            console.log(result.img.Buffer);
            console.log("Saved To database");
            res.contentType(final_img.contentType);
            res.send(final_img.img.data);
        }
    })
})

router.get("/getimg/uploads/:imgid", (req, res) => {
    console.log(req.params.imgid);
    var img = fs.readFileSync("uploads/" + req.params.imgid);
    var encode_img = img.toString('base64');
    res.contentType("image/png");
    res.send(new Buffer(encode_img,'base64'));
  });


router.get("/viewimg", (req, res) => {

    var arr= [];
    imageModel.find((err, data) =>{
        if(!err){
           console.log("sss", data[1].filePath);
           data.forEach(element => {
            arr.push(element.filePath);
            console.log(element.filePath);
          });
           res.render('../views/viewImg', {"arrimg" : arr, "contenttype" : "image/png"});

        }else {
            console.log("error");
        }
    }).lean();

    
  });


router.get("/", (req, res) => {
    res.render('../views/register');
  });



  router.get("/welcome", auth, (req, res) => {
    res.status(200).render('../views/welcome', {"username" : displayname});
  });

  router.get("/login", (req, res) => {
    res.status(200).render('../views/welcome');
  });

  router.get("/logout", (req, res) => {
    res.clearCookie("token");
    res.status(200).render('../views/login');
  });

  router.post("/login", async (req, res) => {
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
        res.status(200).redirect('/welcome');
      }
      //res.status(400).send("Invalid Credentials");
    } catch (err) {
      console.log(err);
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



module.exports = router;