// console.clear();

console.group("%cGood with Computers", "font-weight: bold;");

setInterval(function() {
	console.info("✊");
}, 1000);

console.groupEnd();

console.table([
	{
		first: "René",
		last: "Magritte"
	},
	{
		first: "Chaim",
		last: "Soutine",
		birthday: "18930113"
	},
	{
		first: "Henri",

		last: "Matisse"
	}
]);

console.time();
for (var i = 0; i < 100000; i++) {
	let square = i ** 2;
}
console.timeEnd();
const first = () => {
	second();
};
const second = () => {
	third();
};
const third = () => {
	fourth();
};
const fourth = () => {
	console.trace();
};
first();
