var process = require("process");
var express = require("express");
var auth = require("basic-auth");
var app = express();
var bodyParser = require("body-parser");
var morgan = require("morgan");
var jwt = require("jsonwebtoken");
var config = require("./config");
var port = process.env.PORT || 80;

process.on("SIGINT", () => {
	process.exit(0);
});

app.set("secret", config.secret);
app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());
app.use(morgan("dev"));

var routes = express.Router();
var user = new Object({
	name: "foobar",
	password: "password",
	admin: true
});

console.log(user);

routes.get("/", function(req, res) {
	res.json({ message: "Welcome to the coolest API on earth!" });
});

routes.post("/auth", function(req, res) {
	var credentials = auth.parse(req.headers.authorization);
	if (
		user === undefined ||
		(credentials.name == user.name && credentials.pass == user.password)
	) {
		var payload = { user: user.name };
		var token = jwt.sign(payload, app.get("secret"));
		res.json({ token: token });
		res.end("Access granted");
	} else {
		res.writeHead(401, "Access invalid", { "Content-Type": "text/plain" });
		res.end("Invalid credentials");
	}
});

routes.use(function(req, res, next) {
	var token = req.headers["x-access-token"];
	if (token) {
		jwt.verify(token, app.get("secret"), function(err, decoded) {
			if (err) {
				res.writeHead(401, "Access invalid", {
					"Content-Type": "text/plain"
				});
				res.end("Access invalid");
			} else {
				next();
			}
		});
	} else {
		return res.status(403).send({
			success: false,
			message: "No token provided."
		});
	}
});

routes.get("/user", function(req, res) {
	res.status(200).json({ message: "token valid" });
});

app.use("/api", routes);
app.listen(port);

console.log("✨ Now the magic happens.");
