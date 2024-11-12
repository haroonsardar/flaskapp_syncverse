function startSyncverse() {
    alert('Starting SyncVerse for syncing audio with video...');
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


// Function to open the modal
function openModal() {
    document.getElementById("resourceModal").style.display = "block";
}

// Function to close the modal
function closeModal() {
    document.getElementById("resourceModal").style.display = "none";
}

// Function to handle both GitHub and Colab actions
function openResources() {
    // Open the GitHub link in a new tab
    window.open("https://github.com/your-repo-link", "_blank");
    
    // Open the Colab link in a new tab for download
    window.open("https://colab.research.google.com/drive/your-colab-link", "_blank");
    
    // Close the modal after action
    closeModal();
}

// Close modal when clicking outside of it
window.onclick = function(event) {
    const modal = document.getElementById("resourceModal");
    if (event.target === modal) {
        modal.style.display = "none";
    }
}

