var http = require('http');                                      // This is core module
var fs = require('fs');                                         //This is core module
var url = require('url');                                     

http.createServer(function (req, res) {
var qs = url.parse(req.url, true);


console.log("ssss", req.url, res.data);

if(req.url === '/postdata')                // can also check this using if (qs.pathname === '/about')
{


var body = "";
  req.on('data', function (chunk) {
    body += chunk;
  });
  req.on('end', function () {
    console.log('POSTed: ' + body);
    fs.writeFile('Data.txt', body, function (err) {
        if (err) return console.log(err);
        console.log('Got result');
      });

    res.writeHead(200);
    res.write("Data was successfully written to text file");
    res.end();
  });

}

if(req.url === '/')                // can also check this using if (qs.pathname === '/about')
{
  //console.log(qs.query);
  fs.readFile('Page1.html', function(err,data){
  res.writeHead(200, {'Content-Type': 'text/html'});
  res.write(data);        // This line writes 'Arun'
  res.end();
})
}


if(req.url === '/css/main.css')                // can also check this using if (qs.pathname === '/about')
{
        fs.readFile('css/main.css', function(err,data){
        res.writeHead(200, {'Content-Type': 'text/css'});
        res.write(data);        // This line writes 'Arun'
        res.end();
    })
}

if(req.url === '/Data.txt')                // can also check this using if (qs.pathname === '/about')
{
        fs.readFile('Data.txt', function(err,data){
        res.writeHead(200, {'Content-Type': 'text/json'});
        res.write(data);        // This line writes 'Arun'
        res.end();
    })
}


}).listen(3002);