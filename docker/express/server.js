"use strict";

const express = require("express");
const process = require('process')

const PORT = 8080;
const HOST = "0.0.0.0";

const app = express();
app.get("/", (req, res) => {
	res.send("Hello world\n");
	console.log("Request 🙋‍♂️");
});

app.listen(PORT, HOST);
console.log(`Running on http://${HOST}:${PORT}`);


process.on('SIGINT', () => {
  process.exit(0)
})
