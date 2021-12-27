const mongoose = require('mongoose');

var productSchema = new mongoose.Schema({
productName: {
    type: String
},
productType: {
    type: Number
}
})

mongoose.model('students', productSchema);

