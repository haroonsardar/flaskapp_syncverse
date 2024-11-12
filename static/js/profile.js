function editProfile() {
    document.querySelector('.profile-edit').style.display = 'block';
    document.querySelector('.edit-profile-button').style.display = 'none';
}

function saveProfile() {
    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;
    document.getElementById('user-name').textContent = name;
    document.getElementById('user-email').textContent = email;

    document.querySelector('.profile-edit').style.display = 'none';
    document.querySelector('.edit-profile-button').style.display = 'block';
}
window.onload = function(){
    const sidebar = document.querySelector(".sidebar");
    const closeBtn = document.querySelector("#btn");
    const searchBtn = document.querySelector(".bx-search")

    closeBtn.addEventListener("click",function(){
        sidebar.classList.toggle("open")
        menuBtnChange()
    })

    searchBtn.addEventListener("click",function(){
        sidebar.classList.toggle("open")
        menuBtnChange()
    })

    function menuBtnChange(){
        if(sidebar.classList.contains("open")){
            closeBtn.classList.replace("bx-menu","bx-menu-alt-right")
        }else{
            closeBtn.classList.replace("bx-menu-alt-right","bx-menu")
        }
    }
}
