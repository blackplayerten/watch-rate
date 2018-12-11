'use strict';

const add_film_form = document.querySelector('.film_form');

const name = add_film_form.querySelector('#id_name');
const year = add_film_form.querySelector('#id_year');
const age = add_film_form.querySelector('#id_age');
const time_input = add_film_form.querySelector('#id_time');

add_film_form.addEventListener('submit', e => {
    e.preventDefault();

    let form_is_wrong = false;

    if (name.value.length === 0) {
        const name_error_message = add_film_form.querySelector('#id_name_error');
        if (name_error_message === null) {
            name.insertAdjacentHTML('beforebegin',
              `<div class="errors" id="id_name_error"><strong>Film name cannot be blank</strong></div>`);
        } else {
            name_error_message.innerHTML = `<strong>Film name cannot be blank</strong>`;
        }
        form_is_wrong = true;
    }

    const year_error_message = add_film_form.querySelector('#id_year_error');
    if (year.value.length === 0) {
        if (year_error_message === null) {
            year.insertAdjacentHTML('beforebegin',
              `<div class='errors' id="id_year_error"><strong>Year cannot be blank</strong></div>`);
        } else {
            year_error_message.innerHTML = `<strong>Year cannot be blank</strong>`;
        }
        form_is_wrong = true;
    } else {
        const year_value = parseInt(year.value);
        const today = new Date();
        if (year_value <= 1800 || year_value >= today.getFullYear() + 10) {
            if (year_error_message === null) {
                year.insertAdjacentHTML('beforebegin',
                  `<div class='errors' id="id_year_error"><strong>Year should be real</strong></div>`);
            } else {
                year_error_message.innerHTML = `<strong>Year should be real</strong>`;
            }
            form_is_wrong = true;
        }
    }

    if (age.value.length !== 0) {
        const age_value = parseInt(age.value);
        if (age_value < 0 || age_value > 21) {
            const age_error_message = add_film_form.querySelector('#id_age_error');
            if (age_error_message === null) {
                age.insertAdjacentHTML('beforebegin',
                  `<div class='errors' id="id_age_error"><strong>Age can't be negative or more than 21</strong></div>`);
            } else {
                age_error_message.innerHTML = `<strong>Age can't be negative or more than 21</strong>`;
            }
            form_is_wrong = true;
        }
    }

    if (time_input.value.length === 0) {
        const time_error_message = add_film_form.querySelector('#id_time_error');
        if (time_error_message === null) {
            time_input.insertAdjacentHTML('beforebegin',
              `<div class="errors" id="id_time_error"><strong>Time cannot be blank</strong></div>`);
        } else {
            time_error_message.innerHTML = `<strong>Time cannot be blank</strong>`;
        }
        form_is_wrong = true;
    }

    if (form_is_wrong) {
        return
    }

    const formData = new FormData(add_film_form);
    fetch("/films", {
        method: "post",
        body: formData,
    }).then(response => {
        switch (response.status) {
            case 200:
                response.json().then(message => {
                    window.location.href = message.href;
                });
                break;
            case 400:
                console.log('Bad request, field (-s) is (are) invalid.');
                response.json().then(message => {
                    console.log(message);
                    const wrong_fields = message.errors;
                    for (let field in wrong_fields) {
                        if (wrong_fields.hasOwnProperty(field)) {
                            const field_errors = wrong_fields[field];
                            const field_box = add_film_form.querySelector('#id_' + field);
                            field_errors.forEach(field_error => {
                                const error_message = add_film_form.querySelector('#id_' + field + '_error');
                                if (error_message === null) {
                                    field_box.insertAdjacentHTML('beforebegin',
                                      `<div class="errors" id="id_${field}_error"><strong>${field_error}</strong></div>`);
                                } else {
                                    error_message.innerHTML = `<strong>${field_error}</strong>`;
                                }
                            })
                        }
                    }
                });
                break;
            default:
                console.log('Looks like there was a problem. Status Code: ' + response.status);
        }
    }).catch(error => {
        console.log('cannot send film data: ' + error.message);
    });
});
