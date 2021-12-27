var fs = require('fs'); 
var http = require('http');
var url = require('url');


http.createServer(function (req, res) {
    console.log(req.headers.accept);
    if(req.headers.accept.split(',')[0] == 'text/css') {
        console.log('css file loaded');

        fs.readFile('css/Index.css', (err, data)=>{
            res.writeHeader(200, {'Content-Type': 'text/css'});
            res.write(data);
            res.end();
        });  
   }
   else if (req.headers.accept.split(',')[0] == 'image/webp')
   {
    console.log('image file loaded');

    fs.readFile('img/Dass.jpg', (err, data)=>{
        res.writeHeader(200, {'Content-Type': 'image/jpeg'});
        res.write(data);
        res.end();
    });  
   }
   else if (req.headers.accept.split(',')[0] == 'text/html') {
    // console.log('loaded html', req);

    fs.readFile('Index.html', function(err, data) {
        res.writeHead(200, {'Content-Type': 'text/html'});
        res.end(data);
});
}}).listen(80);
console.log('Server started and it is running on post 80');
