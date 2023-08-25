const form = document.getElementById("signup-form1");
const orgname = document.getElementById("orgname");
const comname = document.getElementById("comname");
const cemail = document.getElementById("cemail");
const cphno = document.getElementById("cphno");
const caddress = document.getElementById("caddress");
const regcertnumber = document.getElementById("regcertnumber");
const password = document.getElementById("password");
const password2 = document.getElementById("password2");

form.addEventListener("submit", (e) => {
  e.preventDefault();

  const flag = checkInputs();
  if (flag) {
    document.getElementById("signup-form1").submit();
  }
});

function checkInputs() {
  // trim to remove the whitespaces
  var flag = false;
  const orgnameValue = orgname.value.trim();
  const comnameValue = comname.value.trim();
  const cemailValue = cemail.value.trim();
  const cphnoValue = cphno.value.trim();
  const caddressValue = caddress.value.trim();
  const regcertnumberValue = regcertnumber.value.trim();
  const passwordValue = password.value.trim();
  const password2Value = password2.value.trim();

  if (orgnameValue === "") {
    setErrorFor(orgname, "Organizer Name cannot be blank");
    flag = false;
  } else {
    setSuccessFor(orgname);
    flag = true;
  }

  if (comnameValue === "") {
    setErrorFor(comname, "Community Name cannot be blank");
    flag = false;
  } else {
    setSuccessFor(comname);
    flag = true;
  }

  if (cemailValue === "") {
    setErrorFor(cemail, "Email cannot be blank");
    flag = false;
  } else if (!isEmail(cemailValue)) {
    setErrorFor(cemail, "Not a valid email");
    flag = false;
  } else {
    setSuccessFor(cemail);
    flag = true;
  }

  if (cphnoValue === "") {
    setErrorFor(cphno, "Phone Number cannot be blank");
    flag = false;
  } else if (!phonenumber(cphnoValue)) {
    setErrorFor(cphno, "Not a valid Phone Number");
    flag = false;
  } else {
    setSuccessFor(cphno);
    flag = true;
  }

  if (caddressValue === "") {
    setErrorFor(caddress, "Address cannot be blank");
    flag = false;
  } else {
    setSuccessFor(caddress);
    flag = true;
  }

  if (regcertnumberValue === "") {
    setErrorFor(regcertnumber, "Register Certificate Number cannot be blank");
    flag = false;
  } else {
    setSuccessFor(regcertnumber);
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

function isEmail(cemail) {
  return /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/.test(
    cemail
  );
}

function phonenumber(cphno) {
  return /^\(?([0-9]{3})\)?[-. ]?([0-9]{3})[-. ]?([0-9]{4})$/.test(cphno);
}
