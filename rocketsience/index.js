module.exports = function(a, b) {
	console.log("Starting ");
	var output = starting(a, b);
	return output;
};

function starting(a, b) {
	var fire = "🚀    ";
	for (i = 0; i < b; i++) {
		fire += " 🔥 "
	}
	console.log(fire);
};
