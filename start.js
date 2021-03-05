const http = require("http"); // dieses ist dazu da, das der Server über http läuft
const hoster = "localhost"; // ich brauche hier den Host von Eugen, so lange erstmal local
const port = 8000;

const jsonReader = function (req,res)
{
    res.writeHead(200);
    res.end("Der Server läuft");
};

const server = http.createServer(jsonReader);
server.listen(port,hoster, () => {
    console.log("Der Server ist gehostet unter http://${hoster}:${port}");
});

