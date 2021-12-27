var http = require('http');
var url = require('url');
var path = require('path');
var fs = require('fs');
const { resolve } = require('path');
const { readdir } = require('fs').promises;
var fileList = [];
var rootpath = "/hdd/Backup/Coding/Nodejs/MediaServer/";


var mimeTypes = {
    "html" : "text/html",
    "jpeg" : "image/jpeg",
    "jpg" : "image/jpg",
    "png" : "image/png",
    "js" : "text/javascript",
    "css" : "text/css",
    "mp4" : "video/mp4"
}

async function getFiles(dir) {
    const dirents = await readdir(dir, { withFileTypes: true });
    const files = await Promise.all(dirents.map((dirent) => {
      const res = resolve(dir, dirent.name);
      return dirent.isDirectory() ? getFiles(res) : res;
    }));
    return Array.prototype.concat(...files);
  }


http.createServer(function (req, res){
    var uri = url.parse(req.url).pathname;
    var filename = path.join(process.cwd(), unescape(uri));
    console.log('Loading ' + uri, req.url, filename);
    var stats;

    //console.log("filename", filename, req.url);
            if (uri == "/Videos")
            {
                
                let templist = [];

                fs.readdirSync('Videos/').forEach(file => {
                    templist.push(file.replace(rootpath, ""));
                    res.writeHead(200, {'Content-Type': 'text/plain'});
                    res.write(JSON.stringify(templist));
                    res.end();
                    console.log(templist);
                    });

            }else if (uri != "/Videos" && uri.includes("/Videos"))
            {
                getFiles(filename.replace("/Videos", "/Videos/"))
                .then(files => {
                  files.forEach(file => fileList.push(file.replace(rootpath, "")));
                    
                    
                //   console.log(fileList);
            })
                .catch(e => console.error(e));
    

                    res.writeHead(200, {'Content-Type': 'text/plain'});
                    res.write(JSON.stringify(fileList));
                    res.end();

            }





    try {
        stats = fs.lstatSync(filename);
        } catch (e){
                
            console.log("errror : ", e);
                // res.writeHead(400, {'Content-Type': 'text/plain'});
                // res.write('404 file not found\n');
                // res.end();
            //}
            return;

        }

        // check if file/directory
        if(stats.isFile()){
            var mimeType = mimeTypes[path.extname(filename).split(".").reverse()[0]];
            res.writeHead(200, {'Content-type' : mimeType});

            var fileStream = fs.createReadStream(filename);
            fileStream.pipe(res);
        } else if (stats.isDirectory()){
            res.writeHead(302,{'Location' : 'index.html'});
            res.end();
        } else {
            res.writeHead(500, {'Content-Type': 'text/plain'});
            res.write('504 Internal Error\n');
            res.end();
        }


}).listen(3002);
