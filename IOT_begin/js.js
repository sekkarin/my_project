var firebaseConfig = {
    apiKey: "AIzaSyDp0RJtRiIXXTP3X3bDRbpv-Vaq9RsSE_I",
    authDomain: "iot-begin.firebaseapp.com",
    databaseURL: "https://iot-begin-default-rtdb.firebaseio.com",
    projectId: "iot-begin",
    storageBucket: "iot-begin.appspot.com",
    messagingSenderId: "680136782403",
    appId: "1:680136782403:web:40fd21e6560aeaa468daf6",
    measurementId: "G-H067QY76Q1"
};
// Initialize Firebase
firebase.initializeApp(firebaseConfig);
firebase.analytics();

function saveOnclick() {
    var save = document.getElementById('save'); //เก็บ อิลิเมน save ใว้ในตัวแปล seve
    var passwowrd  = document.getElementById('password'); //เก็บ อิลิเมน password ใว้ในตัวแปล password
    var address = document.getElementById('address');    //เก็บ อิลิเมน address ใว้ในตัวแปล address
    insertdata(email.value,passwowrd.value,address.value); //ส่งค่าไปยังฟันชันช์ insertdata
    
}
window.onload = function () {
    showData();
}

function showData(){
    var firebaseRef = firebase.database().ref("user").orderByChild('address');  //เมดฌเธด จัดเรียงตาม key orderByChild("key")
    firebaseRef.once('value').then(function (dateSnapshot) {    
        dateSnapshot.forEach(function(dateSnapshot){
            var childKey = dateSnapshot.key;
            var childdata = dateSnapshot.val();
            console.log(childdata);
        });
    });

}
// ฟังชันช์ เพิ่มข้อมูล มีพารามิสเตอร์ 3 ตัว 
function insertdata(email,password,address){
    var firebaseRef = firebase.database().ref('user'); //อ้างอิงตัวแม่ 
    firebaseRef.push({  //ใช้เมดเธด push(เพิ่มchidlให้เอง และ ค่าที่จะเพิ่มเข้าเป็นออฟเจค {key: value} )
        email:email,
        password:password,
        address:address
    })
    console.log("success");
}
// การลบข้อมุล
function DelOnclick(){
    var firebaseRef = firebase.database().ref("user/user1");  // อ้างอิงตําแหน่งในฐานข้อมูล ที่จะลบ
    firebaseRef.remove().then(function(){    // ใช้คําเมดเธด remove()
        console.log("Remove succeded");
    }).catch(function(error){
        console.log("remove failed"+ error.message);
    })
}
// การอัพเดตข้อมูล
function updateOnclick(){
    var firebaseRef = firebase.database().ref("user/-MPYXi8CEREMMNOttIQb"); 
    firebaseRef.update({address:"kennnnnn",email:"sekkri1234@gmail.com"}); // ใช้เมดเธด  update(ค่าที่จะเปลี่ยน key: value)
    console.log("Update success!!");
}