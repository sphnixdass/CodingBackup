const mongoose = require('mongoose');


//Schema
var imgSchema = mongoose.Schema({
    firstname: { type: String, default: null },
    emailid: { type: String, default: null },
    mobileno: { type: Number, default: null },
    userstatus: { type: String, default: null },

});
var instuser = mongoose.model("interestUser",imgSchema); 

module.exports = instuser;