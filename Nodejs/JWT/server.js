require('dotenv').config();

const express = require('express');
const app = express();

const jwt = require('jsonwebtoken');

app.use(express.json());


const posts = [
    {
        username: 'Dass',
        title: 'Post 1'
    },
    {
        username: 'Dass2',
        title: 'Post 2'
    },
    {
        username: 'Dass3',
        title: 'Post 3'
    }
];

app.get('/posts', authenticateToken, (req, res, next) =>{
    res.json(posts.filter(post => post.username === req.user.name));
});

app.post('/login', (req, res, next) => {
    //Authenticate User
    const username = req.body.username;
    const user = {name : username}

    const accessToken = jwt.sign(user, process.env.ACCESS_TOKEN_SECRET);
    res.json({accessToken: accessToken});

});

function authenticateToken(req, res, next) {
    const authHeader = req.headers['authorization'];
    console.log(authHeader, req.headers);

    const token = authHeader && authHeader.split(" ")[1];
    if(token == null) return res.sendStatus(401);
    
    jwt.verify(token, process.env.ACCESS_TOKEN_SECRET, (err, user) =>{
        if (err) return res.sendStatus(403)
        req.user = user;
        next();
    })

};

app.listen(3000,() => console.log("server is running"));