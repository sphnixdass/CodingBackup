const mongoose = require('mongoose');
var userSchema = new mongoose.Schema({
  
    emailAddress: { type: String},
    password: { type: String },
    token: { type: String },
    firstName: { type: String },
    lastName: { type: String},
    genderOptions: { type: String }

  
      })
      
  var mongomodel = mongoose.model('HeroUser', userSchema);
  
  module.exports = mongomodel;
