const http = require("http"); // dieses ist dazu da, das der Server über http läuft
const fs = require('fs').promises;
const hoster = "localhost"; // ich brauche hier den Host von Eugen, so lange erstmal local
const port = 8000;
let indexFile;

const jsonReader = function (req,res)
{
    fs.readFile(__dirname + "/darstellung.html")
    .then(contents => {
    res.setHeader("Content-Type", "application/json");
    switch (req.url) {}
    res.writeHead(200);
    res.end("Der Server läuft, hier die Inhalte: "+ contents); })
    case "/müssenWirNochBestimmen":
            res.writeHead(200);
            res.end(authors);
            break
    default:
            res.writeHead(404);
            res.end(JSON.stringify({error:"Resource not found"}));
    .catch(err => {
            res.writeHead(500);
            res.end(err);
            return;
        });
};

const server = http.createServer(jsonReader);
server.listen(port,hoster, () => {
    console.log("Der Server ist gehostet unter http://${hoster}:${port}");
});

