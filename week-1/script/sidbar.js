const toggleBtn = document.querySelector(".HamburgerIcon");
const toggleBtn1 = document.querySelector(".NavItem");
const sidebar = document.querySelector(".NavItem");
const handleToggle = () => {
    sidebar.classList.toggle("Show-NavItem")
;}
toggleBtn.addEventListener("click", handleToggle);

sidebar.addEventListener("click", handleToggle);
