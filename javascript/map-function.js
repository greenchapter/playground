
//
let cars = ["Saab", "Volvo", "BMW"];
cars.map(function (element) {
  console.log('👉🏻 ', element);
});

//
let car = {type:"Fiat", model:"500", color:"white"};
Object.keys(car).map(function(key) {
	console.log('👉🏻 ', car[key]);
});
