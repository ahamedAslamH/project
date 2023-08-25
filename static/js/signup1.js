const form = document.getElementById("signup-form");
const username = document.getElementById("username");
const lastname = document.getElementById("lastname");
const email = document.getElementById("email");
const address = document.getElementById("address");
const password = document.getElementById("password");
const password2 = document.getElementById("password2");
const phno = document.getElementById("phno");
const ipn = document.getElementById("ipn");

form.addEventListener("submit", (e) => {
  e.preventDefault();

  const flag = checkInputs();
  if (flag) {
    document.getElementById("signup-form").submit();
  }
  // alert("Register Successfully!");
});

function checkInputs() {
  // trim to remove the whitespaces
  var flag = false;
  const usernameValue = username.value.trim();
  const lastValue = lastname.value.trim();
  const emailValue = email.value.trim();
  const addressValue = address.value.trim();
  const passwordValue = password.value.trim();
  const password2Value = password2.value.trim();
  const phnoValue = phno.value.trim();
  const ipnValue = ipn.value.trim();

  if (usernameValue === "") {
    setErrorFor(username, "Firstname cannot be blank");
    flag = false;
  } else {
    setSuccessFor(username);
    flag = true;
  }

  if (ipnValue === "") {
    setErrorFor(ipn, "Identity Proof Number cannot be blank");
    flag = false;
  } else {
    setSuccessFor(ipn);
    flag = true;
  }

  if (phnoValue === "") {
    setErrorFor(phno, "Phone Number cannot be blank");
    flag = false;
  } else if (!phonenumber(phnoValue)) {
    setErrorFor(phno, "Not a valid Phone Number");
    flag = false;
  } else {
    setSuccessFor(phno);
    flag = true;
  }

  if (lastValue === "") {
    setErrorFor(lastname, "Lastname cannot be blank");
    flag = false;
  } else {
    setSuccessFor(lastname);
    flag = true;
  }

  if (emailValue === "") {
    setErrorFor(email, "Email cannot be blank");
    flag = false;
  } else if (!isEmail(emailValue)) {
    setErrorFor(email, "Not a valid email");
    flag = false;
  } else {
    setSuccessFor(email);
    flag = true;
  }

  if (addressValue === "") {
    setErrorFor(address, "Address cannot be blank");
    flag = false;
  } else {
    setSuccessFor(address);
    flag = true;
  }

  if (passwordValue === "") {
    setErrorFor(password, "Password cannot be blank");
    flag = false;
  } else {
    setSuccessFor(password);
    flag = true;
  }

  if (password2Value === "") {
    setErrorFor(password2, "Confirm Password cannot be blank");
    flag = false;
  } else if (passwordValue !== password2Value) {
    setErrorFor(password2, "Confirm Password does not match");
    flag = false;
  } else {
    setSuccessFor(password2);
    var pass = true;
  }

  return flag && pass;
}

function setErrorFor(input, message) {
  const Inputfield = input.parentElement;
  const small = Inputfield.querySelector("small");
  Inputfield.className = "input-field error";
  small.innerText = message;
}

function setSuccessFor(input) {
  const Inputfield = input.parentElement;
  Inputfield.className = "input-field success";
}

function isEmail(email) {
  return /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/.test(
    email
  );
}

function phonenumber(phno) {
  return /^\(?([0-9]{3})\)?[-. ]?([0-9]{3})[-. ]?([0-9]{4})$/.test(phno);
}
