const mongoose = require('mongoose');

// mongoose.connect(process.env.DB,(err) => {
//     if(!err){
//         console.log('Connection Success');
//     } else {
//         console.log('Unable to connect');
//     }
// });

var userSchema = new mongoose.Schema({
  
  username: { type: String, default: null },
  password: { type: String },
  token: { type: String }

    })
    
var mongomodel = mongoose.model('HeroUser', userSchema);

module.exports = mongomodel;