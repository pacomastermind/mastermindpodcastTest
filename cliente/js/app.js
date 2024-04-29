var categoryListDOM = document.getElementById('categorias-selectores');

var categoriesData = [
    {name:"music"},
    {name:"technology"},
    {name:"art"},
    {name:"sports"},
]

var categoryListDOM=""

categoriesData.map((cat,index) => {
  index++;
  categoryListDOM = categoryListDOM + `<input type="radio" class="btn-check" name="vbtn-radio" id="vbtn-radio${index}" autocomplete="off"  ${index==1?"checked":""}>
  <label class="btn btn-outline-danger" for="vbtn-radio${index}">${cat.name}</label>`
});

document.getElementById('categorias-selectores').innerHTML = categoryListDOM

var inputs=document.getElementsByClassName("btn-check"),
    x=inputs.length;
var labels = document.getElementsByTagName('label');
while(x--)
    inputs[x].addEventListener("change",(evt)=>{
        console.log("name: "+evt.target.id);
        for( var i = 0; i < labels.length; i++ ) {
            if (labels[i].htmlFor == evt.target.id)
                return console.log("name: "+labels[i].innerHTML);;
        }
    });

/*
const loginForm = document.getElementById("login")

loginForm.addEventListener("submit", (e) => {
  e.preventDefault()
  console.log("Aprieto")

  const formData = new FormData(loginForm)

  console.log(formData)

  fetch("http://localhost:8000/token", {
    method: "POST",
    body: formData,
  })
  .then((res) => res.json())
  .then((token) => {
    console.log("Token", token)
  })
  .catch((err) => {
    console.log("Error", err)
  })
})*/