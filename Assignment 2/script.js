// function myFunction() {
//   var x = document.getElementById("navDemo");
//   if (x.className.indexOf("w3-show") == -1) {
//     x.className += " w3-show";
//   } else {
//     x.className = x.className.replace(" w3-show", "");
//   }
// }

// $("a").click(function(e) {
//   e.preventDefault(); //stop the browser from following
//   window.location.href = "uploads/file.doc";
// });

// setInterval(function(){

//     $('.blink').fadeOut(1000);
//     $('.blink').fadeIn(1000);

// }, 1000);

const name = document.getElementById("name");
const email = document.getElementById("email");
const form = document.getElementById("form");
const errorElement = document.getElementById("error");

form.addEventListener("submit", e => {
  let messages = [];

  if (name.value == "" || name.value == null) {
    messages.push("Name is required");
  }

  if (email.value.length < 1) {
    messages.push("email cant be blank");
  }

  if (messages.length > 0) {
    e.preventDefault();
    errorElement.innerText = messages.join(",");
  }
});

// function dosomething() {
//   alert("Your message was sent!");
//   window.location.reload("contact.htnl");
// }

function validateForm() {
  var x = document.forms["myForm"]["name"].value;
  if (x == "") {
    alert("Name must be filled out");
    return false;
  }
}

function myFunction() {
  var x, text;

  // Get the value of the input field with id="numb"
  x = document.getElementById("numb").value;

  // If x is Not a Number or less than one or greater than 10
  if (isNaN(x) || x < 1 || x > 10) {
    text = "Input not valid";
  } else {
    text = "Input OK";
  }
  document.getElementById("demo").innerHTML = text;
}