const express = require('express');
const router = express.Router();

const mongoModel = require('../models/mainModel');


router.get('/', (req, res)=>{
    res.render('../views/insertPage')
    mongoModel.find((err, data) =>{
        if(!err){
           console.log("sss", data);
           
        }else {
            console.log("error");
        }
    }).lean();

});



router.post('/insert', (req, res)=>{
    
    console.log(req.body);
    
    var insertobj = new mongoModel();
    insertobj.cuisine = req.body.cuisine;

    if (req.body.salt !== undefined){

        insertobj.ingredients.push(req.body.salt);
    }
    
    if (req.body.pepper !== undefined){

        insertobj.ingredients.push(req.body.pepper);
    }
    if (req.body.chilli !== undefined){

        insertobj.ingredients.push(req.body.chilli);
    }

    insertobj.Nutrition.Protein = req.body.Protein;
    insertobj.Nutrition.Fat = req.body.Fat;
    insertobj.Nutrition.Carbohydrate = req.body.Carbohydrate;
    if (req.body.Others1 !== undefined){

        insertobj.Nutrition.Others.push(req.body.Others1);
    }
    
    if (req.body.Others2 !== undefined){

        insertobj.Nutrition.Others.push(req.body.Others2);
    }


    insertobj.whyDoYouLikeIt = req.body.likeit;

    insertobj.anyOther.push(req.body.Others);
   
    insertobj.save((err, data)=> {
        if(!err){
            res.redirect('/');
        }else {
            console.log("error", err);
        }
    });

});


module.exports = router;