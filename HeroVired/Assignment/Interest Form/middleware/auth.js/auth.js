const jwt = require("jsonwebtoken");

const config = process.env;

const verifyToken = (req, res, next) => {
    console.log(req.url);
    var infostr = "";
    var infourl = "";
    if (req.url == "/interestform")
    {
      infostr = "User must logon to submit interest form";
      infourl = "/interestform";

    } else if (req.url == "/adminpage")
    {
      infostr = "User must logon to view adminpage ";
      infourl = "/adminpage";
    }

    global.urlinfo = infourl;

  const token =
    req.body.token || req.query.token || req.headers["x-access-token"] || req.cookies['token'];

  if (!token) {
    // return res.status(403).send("A token is required for authentication");
    

    return res.status(200).render('../views/login', {"info" : infostr, "infourl" : infourl});
  }
  try {
    const decoded = jwt.verify(token, "HeroSerectKey");
    req.user = decoded;
  } catch (err) {
    return res.status(401).send("Invalid Token");
  }
  return next();
};

module.exports = verifyToken;