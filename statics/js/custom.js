const uploader = document.getElementById('id_image')
const file_name = document.querySelector('.file-name')
const choose_button = document.querySelector('.profile-image-upload-label')
const profile_image = document.querySelector('.profile-image')
const image_preview = document.querySelector('.image-preview')
const submit_button = document.querySelector('.profile-submit-button')

uploader.addEventListener('change', function(){
    const file = this.files[0];
    if(file){
        const reader = new FileReader();

        reader.addEventListener("load", function(){
            image_preview.setAttribute("src", this.result);
            profile_image.style.display = "none";
            image_preview.style.display = "block";
            choose_button.style.background = "green";
            choose_button.style.color = "white";
            choose_button.innerText = file.name;
            submit_button.removeAttribute("disabled");

        });

        reader.readAsDataURL(file);
    }
    else{
        image_preview.setAttribute("src", "");
        image_preview.style.display = "none";
        profile_image.style.display = "block";
        choose_button.style.background = "white";
        choose_button.style.color = "black";
        choose_button.innerText = "انتخاب تصویر";
        submit_button.setAttribute("disabled", "");
    }
});
