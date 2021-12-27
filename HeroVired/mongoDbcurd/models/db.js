const mongoose = require('mongoose');

mongoose.connect('mongodb://127.0.0.1:27017/dassdb',(err) => {
    if(!err){
        console.log('Connection Success');
    } else {
        console.log('Unable to connect');
    }
});
