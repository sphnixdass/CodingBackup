const mongoose = require('mongoose');

mongoose.connect('mongodb://127.0.0.1:27017/dassdb',(err) => {
    if(!err){
        console.log('Connection Success');
    } else {
        console.log('Unable to connect');
    }
});

var productSchema = new mongoose.Schema({
    cuisine: {
        type: String
    },
    ingredients: [],
    Nutrition: {
        Protein : { type: Number, default: 0},
        Fat : { type: Number, default: 0},
        Carbohydrate : { type: Number, default: 0},
        Others : []
    },
    whyDoYouLikeIt: {
        type: String
    },
    anyOther: []

    })
    
var mongomodel = mongoose.model('foods', productSchema);

module.exports = mongomodel;

