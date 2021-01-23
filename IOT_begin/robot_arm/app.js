var database = firebase.database();

var slider = document.getElementById("myRange");
var output = document.getElementById("demo");
output.innerHTML = slider.value; // Display the default slider value

// Update the current slider value (each time you drag the slider handle)
slider.oninput = function () {
    var database = firebase.database().ref("robotA/"); 
    console.log(this.value);
    database.update({join1:slider.value}); // ใช้เมดเธด  update(ค่าที่จะเปลี่ยน key: value)

    output.innerHTML = this.value;
}
