#Listing 4_41: JavaScript function to hide/display <div> tag
function myfunction(id) {
    var x=document.getElementById(id+id);
    if (x.style.display === "none")
    x.style.display = "block";
  else
  x.style.display = "none";
  }
