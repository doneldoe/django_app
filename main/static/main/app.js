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
    document.querySelectorAll('#div_id_passport_image, #div_id_cam_image, #div_id_password1, #div_id_password2, #passport_wrap, #face_wrap'),
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

passport_camera = document.getElementById('passport_camera')
passport_result = document.getElementById('passport_result')
open_passport = document.getElementById('open_passport_cam');
close_passport = document.getElementById('close_passport_cam');
passport_screenshot = document.getElementById('take_passport_snapshot');
redo_passpport = document.getElementById('retake_passport_snapshot');

face_wrap = document.getElementById('face_wrap')
face_camera = document.getElementById('face_camera')
face_result = document.getElementById('face_result')
open_face = document.getElementById('open_face_cam');
close_face = document.getElementById('close_face_cam');
face_screenshot = document.getElementById('take_face_snapshot');
redo_face = document.getElementById('retake_face_snapshot');

Webcam.set({
    image_format: 'jpeg',
    jpeg_quality: 90,
    fps: 45
});

function open_passport_cam() {
    open_passport.className += "d-none"
    passport_screenshot.classList.remove("d-none")
    passport_camera.classList.remove("d-none")
    Webcam.attach('#passport_camera');
}

function take_passport_snapshot() {
    Webcam.freeze()
    passport_screenshot.className += "d-none"
    redo_passpport.classList.remove("d-none")
    close_passport.classList.remove("d-none")
}

function retake_passport_snapshot() {
    Webcam.unfreeze()
    passport_screenshot.classList.remove("d-none")
    redo_passpport.className += "d-none"
    close_passport.className += "d-none"
}

function save_passport() {
    face_wrap.classList.remove("d-none")
    close_passport.className += "d-none"
    redo_passpport.className += "d-none"
    passport_camera.className += "d-none"
    passport_result.classList.remove("d-none")
    Webcam.snap(function (data_uri) {
        passport_result.innerHTML = '<img src="' + data_uri + '"/>';
    });
    Webcam.reset();
}

function open_face_cam() {
    open_face.className += "d-none"
    face_screenshot.classList.remove("d-none")
    face_camera.classList.remove("d-none")
    Webcam.attach('#face_camera');
}

function take_face_snapshot() {
    Webcam.freeze();
    face_screenshot.className += "d-none"
    redo_face.classList.remove("d-none")
    close_face.classList.remove("d-none")
}

function retake_face_snapshot() {
    Webcam.unfreeze();
    face_screenshot.classList.remove("d-none")
    redo_face.className += "d-none"
    close_face.className += "d-none"
}

function save_face() {
    close_face.className += "d-none"
    redo_face.className += "d-none"
    face_camera.className += "d-none"
    face_result.classList.remove("d-none")
    Webcam.snap(function (data_uri) {
        face_result.innerHTML = '<img src="' + data_uri + '"/>';
    });
    Webcam.reset();
}
