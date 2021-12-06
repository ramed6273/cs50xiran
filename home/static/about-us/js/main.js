const sections = document.querySelectorAll("section");
const links = document.querySelectorAll("nav .container ul li");

let sectionOne = document.getElementById("fixedBtnCount");

let sticky = sectionOne.offsetTop;

function btnTopFunction() {
  if (window.pageYOffset > sticky) {
    document.getElementById("fixedBtn").style.display = "inline-block";
  } else {
    document.getElementById("fixedBtn").style.display = "none";
  }
}
function changeLinkState() {
  let index = sections.length;

  while (--index && window.scrollY + 50 < sections[index].offsetTop) {}

  links.forEach((link) => link.classList.remove("active"));
  links[index].classList.add("active");
}

changeLinkState();
window.addEventListener("scroll", () => {
  changeLinkState();
  btnTopFunction();
});
