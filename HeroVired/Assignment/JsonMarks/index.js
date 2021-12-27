var http = require('http');
var fs = require('fs');
http.createServer(function (req, res) {
  console.log(req.url)

    if(req.url == '/'){
    fs.readFile('Index.html', function(err, data) {
    res.writeHead(200, {'Content-Type': 'text/html'});
    res.write(data);
    return res.end();
  });
    } else if(req.url == '/jScript.js'){
    fs.readFile('jScript.js', function(err, data) {
        res.writeHead(200, {'Content-Type': 'text/js'});
        res.write(data);
        return res.end();

    });
  } else 
  {
    return res.end();
  }


}).listen(3000); 