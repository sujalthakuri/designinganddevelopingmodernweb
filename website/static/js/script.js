function upload_image(){
  var sess = document.getElementById("upload_image");

  if (sess.style.display =="none")
  {
    sess.style.display = "block"
  }

  else{
    sess.style.display = "none"
  }
}

function update_bio(){

  var bio = document.getElementById("bio")

  if(bio.style.display == "none")
  {
    bio.style.display = "block"
  }

  else
  {
    bio.style.display = "none"
  }

}

function admin_form(){
  var form = document.getElementById("admin_form")

  if(form.style.display == "none")
  {
    form.style.display = "block"
  }

  else
  {
    form.style.display = "none"
  }
}


function isFollowed(request)
{
  var followed = document.getElementById("followed")
  var notFollowed = document.getElementById("notFollowed")

  if(request != null)
  {
    followed.style.display == "none"
    notFollowed.style.display == "block"
  }

  else
  {
    notFollowed.style.display == "block"
    followed.style.display == "none"
  }
}

function sureDelete(request)
{
  var sure;
  var r = confirm("Are you Sure you want to Delete?");
  return r;
  document.getElementById("demo").innerHTML = sure;

}

function login_validation()
{
    var username = document.forms["loginForm"]["username"].value;
    var password = document.forms["loginForm"]["password"].value;

  if(username == ""){
    alert("Please Enter Username");
    return false;
  }

  if(password == ""){
    alert("Please Enter Password");
    return false;
  }

  if(password.length <5 || username.length >32 )
  {
    alert("Please enter password with the range 6-32");
    return false;
  }

  return true;

}

function admin_validation()
{
    var adminname = document.forms["AdminForm"]["adminname"].value;
    var password = document.forms["AdminForm"]["password"].value;

  if(adminname == ""){
    alert("Please Enter adminname");
    return false;
  }

  if(password == ""){
    alert("Please Enter Password");
    return false;
  }

  if(password.length <5 || adminname.length >32 )
  {
    alert("Please enter password with the range 5-32");
    return false;
  }

  return true;

}



function signup_validation()
{
  var fname = document.forms["signupForm"]["fname"].value;
  var lname = document.forms["signupForm"]["lname"].value;
  var username = document.forms["signupForm"]["username"].value;
  var email = document.forms["signupForm"]["email"].value;
  var password = document.forms["signupForm"]["password"].value;

  if(fname =="")
  {
      alert("Please Enter a First Name");
      return false;
  }

  if(lname == "")
  {
    alert("Please enter a Last Name");
    return false;
  }

  if(username =="")
  {
      alert("Please Enter a Username");
      return false;
  }

  if(email == "")
  {
    alert("Please enter a Email");
    return false;
  }
   if(password =="")
  {
      alert("Please Enter a Password");
      return false;
  }
  return true;
}

function pimage_validation()
{
  var pimage = document.forms["u_i"]["myfile"].value;
  if(pimage == "")
  {
    alert("Please Select an Image");
    return false;
  }

  return true;

}

function image_validation()
{
  var image = document.forms["upload_photo"]["myfile"].value;
  if(image == "")
  {
    alert("Please Select an Image");
    return false;
  }

  return true;
}


