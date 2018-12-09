'use strict';

const add_film_form = document.querySelector('.film_form');

const name = add_film_form.querySelector('#id_name');

add_film_form.addEventListener('submit', e => {
    e.preventDefault();

    if (name.value.length === 0) {
        const name_error_message = add_film_form.querySelector('#id_name_error');
        if (name_error_message === null) {
            name.insertAdjacentHTML('beforebegin',
              `<div id="id_name_error"><strong>Film name cannot be blank.</strong></div>`);
        } else {
            name_error_message.innerHTML = `<div id="id_name_error"><strong>Film name cannot be blank.</strong></div>`;
        }
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
                                const error_message = add_film_form.querySelector('#id_'+ field + '_error');
                                if (error_message === null) {
                                    field_box.insertAdjacentHTML('beforebegin',
                                      `<div id="id_${field}_error"><strong>${field_error}</strong></div>`);
                                } else {
                                    error_message.innerHTML = `
                                      <div id="id_name_error"><strong>${field_error}</strong></div>`
                                      .trim();
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
