const mongoose = require('mongoose');


//Schema
var imgSchema = mongoose.Schema({
    username: { type: String, default: null },
    filePath: { type: String, default: null },
    img:
    {
        data: Buffer,
        contentType: String
    }

});
var image = mongoose.model("image",imgSchema); 

module.exports = image;