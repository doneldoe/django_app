let start = document.createElement('div');
start.className = "start-form";
let start_ref = document.querySelector('.border-bottom');
last_elem = document.querySelector('#div_id_agree');
last_elem_parent = last_elem.parentElement;
last_elem_parent.className = "lep"

Array.prototype.forEach.call(
    document.querySelectorAll('#div_id_last_name, #div_id_first_name, #div_id_patronymic, #div_id_sex, #div_id_email, #div_id_phone_number, .lep'),
    function (c) {
        start.appendChild(c);
    });
start_ref.before(start);


let end = document.createElement('div');
end.className = "end-form d-none";
let end_ref = document.querySelector('.start-form');

Array.prototype.forEach.call(
    document.querySelectorAll('#div_id_passport_image, #div_id_cam_image, #div_id_password1, #div_id_password2'),
    function (c) {
        end.appendChild(c);
    });
end_ref.after(end);

let next = document.querySelector(".next-btn")
let registration = document.querySelector(".registration")


function showForm() {
    start.className += " d-none";
    end.classList.remove("d-none");
    next.className += " d-none";
    registration.classList.remove("d-none");
}