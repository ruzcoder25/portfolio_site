document.addEventListener('DOMContentLoaded', function() {

    const profileInput = document.querySelector('#id_profile_image');
    const profilePreview = document.querySelector('#profilePreview');

    // Profil rasmini tanlaganda darhol preview qilish
    if(profileInput && profilePreview){
        profileInput.addEventListener('change', function(e){
            const file = e.target.files[0];
            if(file){
                const reader = new FileReader();
                reader.onload = function(e){
                    profilePreview.src = e.target.result;
                }
                reader.readAsDataURL(file);
            }
        });
    }

    // Alertlarni avtomatik yopish 5 soniyadan keyin
    const alerts = document.querySelectorAll('.alert');
    alerts.forEach(alert => {
        setTimeout(() => {
            alert.classList.remove('show');
            alert.classList.add('hide');
        }, 5000);
    });
});
