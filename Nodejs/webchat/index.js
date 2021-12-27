const http = require('http');

const hostname = '127.0.0.1';
const port = 3000;

var dd = function (req, res) {
    res.statusCode = 200;
    res.setHeader('Content-Type', 'text/plain');
    res.end('Hello, World!\n');
}

var dd2 = (req, res) => {
    res.statusCode = 200;
    res.setHeader('Content-Type', 'text/plain');
    res.end('Hello, World!\n');
}

const server = http.createServer(dd);

server.listen(port, hostname, () => {
  console.log(`Server running at http://${hostname}:${port}/`);
});

console.log(typeof dd, typeof dd2, dd === dd2, dd.global);