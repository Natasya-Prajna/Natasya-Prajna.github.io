const button = document.getElementById('btn1');
button.addEventListener('click',function(){
   const y = document.getElementById('info1');
   if (y.style.display == 'none'){
        y.style.display = 'block';
   } else if (y.style.display == 'block') {
    y.style.display = 'none';
   }
   
})

const kunci2 = document.getElementById('btn2');
kunci2.addEventListener('click',function(){
   const u = document.getElementById('info2');
   if (u.style.display == 'none'){
        u.style.display = 'block';
   } else if (u.style.display == 'block') {
    u.style.display = 'none';
   }
   
})

const peng3 = document.getElementById('btn3');
peng3.addEventListener('click',function(){
   const i = document.getElementById('info3');
   if (i.style.display == 'none'){
        i.style.display = 'block';
   } else if (i.style.display == 'block') {
    i.style.display = 'none';
   }
   
})

const buk4 = document.getElementById('btn4');
buk4.addEventListener('click',function(){
   const i = document.getElementById('info4');
   if (i.style.display == 'none'){
        i.style.display = 'block';
   } else if (i.style.display == 'block') {
    i.style.display = 'none';
   }
   
})

const discon1 = document.getElementById('Disc1');
const harga1= document.getElementById('info1');
discon1.addEventListener('click',function(){
    harga1.innerHTML = "Rp. 12.750";
    harga1.style.color = "red";
    harga1.style.fontFamily = "Consolas";
})

const discon2 = document.getElementById('Disc2');
const harga2= document.getElementById('info2');
discon2.addEventListener('click',function(){
    harga2.innerHTML = "Rp. 3.400";
    harga2.style.color = "red";
    harga2.style.fontFamily = "Consolas";
})

const discon3 = document.getElementById('Disc3');
const harga3= document.getElementById('info3');
discon3.addEventListener('click',function(){
    harga3.innerHTML = "Rp. 4.250";
    harga3.style.color = "red";
    harga3.style.fontFamily = "Consolas";
})

const discon4 = document.getElementById('Disc4');
const harga4= document.getElementById('info4');
discon4.addEventListener('click',function(){
    harga4.innerHTML = "Rp. 34.000";
    harga4.style.color = "red";
    harga4.style.fontFamily = "Consolas";
})

function myFunction() {
    alert("Mode Has Been Changed");
    var element = document.body;
    element.classList.toggle("dark-mode");
}

