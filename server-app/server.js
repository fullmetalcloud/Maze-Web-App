// server.js

    // set up ========================
    const express  = require('express');
    const request = require('request');
    var app      = express();                               // create our app w/ express
    const bodyParser = require('body-parser');    // pull information from HTML POST (express4)
    const redis = require('redis');
    // configuration =================

    app.use(express.static(__dirname + '/public'));                 // set the static files location /public/img will be /img for users
    app.use(bodyParser.urlencoded({'extended':'true'}));            // parse application/x-www-form-urlencoded
    app.use(bodyParser.json());                                     // parse application/json
    app.use(bodyParser.json({ type: 'application/vnd.api+json' })); // parse application/vnd.api+json as json
    
    app.use(function(req, res, next) {
      res.header("Access-Control-Allow-Origin", "*");
      res.header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept");
      next();
    });

    // //redis dbs
    // var redismaster = redis.createClient(6379, 'redis-master');
    // var redisslave = redis.createClient(6379, 'redis-slave');

    // //check connection to redis master and slave
    // redismaster.on('ready', function() {
    //     console.log('master connected');
    // });

    // redisslave.on('ready', function() {
    //     console.log('slave connected');
    // });

    // routes ======================================================================

    // api ---------------------------------------------------------------------
    // request maze and send to client
    app.get('/maze/:size', function(req, res) {
      request('http://localhost:5000/maze/' + req.params.size, function (error, response, body) {
        console.log()
        res.json(body);
      });
    });

    // check maze is doen and record time if best time
    app.post('/maze/:time', function(req, res) {
      res.send('bestest boy time: ' + req.params.time);
    });

    // application -------------------------------------------------------------
    app.get('/', function(req, res) {
        res.sendFile('./public/index.html'); // load the single view file (angular will handle the page changes on the front-end)
    });

    // listen (start app with node server.js) ======================================
    app.listen(8282);
    console.log("App listening on port 8080");