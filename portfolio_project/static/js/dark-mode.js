//darkmode
const chk = document.getElementById('niwax');
chk.checked?document.body.classList.add("active-dark"):document.body.classList.remove("active-dark");
chk.addEventListener('click', () => {
  localStorage.setItem('darkModeStatus',!chk.checked);
});
window.addEventListener('load', (event) => {
  if(localStorage.getItem('darkModeStatus')=="true"){
    document.body.classList.add("active-dark"); 
    document.getElementById('niwax').checked = true;
  }
});
