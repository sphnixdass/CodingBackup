const express = require('express');
const router = express.Router();
const mongoose = require('mongoose');
var productSchema = new mongoose.Schema({
    productName: {
        type: String
    },
    productType: {
        type: String
    }
    })

const productsch = mongoose.model('students', productSchema);



router.get('/', (req, res)=>{
    res.render('../views/addProducts', {
        viewTitle: 'Hi Dass'
    })
    
})

router.get('/list', (req, res)=>{
    productsch.find((err, data) =>{
        if(!err){
            console.log("sss", data);
            res.render('../views/list', {
                viewTitle: 'Hi Dass',
                list: data
            })
        }else {
            console.log("error");
        }
    }).lean();
   
    
});


router.get('/delete/:id', (req, res)=>{
    productsch.findByIdAndRemove(req.params.id, (err, data)=>{
        if(!err)
        {
            res.redirect('/list');
        }else{
            console.log("error");
        }
    })
})


router.post('/products', (req, res) =>{
    insertRecord(req, res);
});

function insertRecord(req, res) {
    var product = new productsch();
    product.productName = req.body.fname;
    product.productType = req.body.lname;

    console.log(req.body);
    product.save((err, data)=> {
        if(!err){
            res.redirect('/list');
        }else {
            console.log("error");
        }
    })
}

module.exports = router;