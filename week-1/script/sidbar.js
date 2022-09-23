const toggleBtn = document.querySelector(".HamburgerIcon");
const sidebar = document.querySelector(".NavItem");
toggleBtn.addEventListener("click", function () {
    sidebar.classList.toggle("Show-NavItem");
});
