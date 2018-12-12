'use strict';

const add_to_fav_button = document.querySelector('#add_to_fav');

add_to_fav_button.addEventListener('click', e => {
    e.preventDefault();

    const csrf_field = document.querySelector('input[name=csrfmiddlewaretoken]');
    const csrf_token = csrf_field.getAttribute('value');
    const slug = window.location.href.split('/').pop();
    console.log('trying to add to fav this: ', slug);
    fetch('/film/add_to_fav/' + slug, {
        method: 'post',
        headers: new Headers({
            'X-CSRFToken': csrf_token,
        }),
    }).then(response => {
          switch (response.status) {
              case 200:
                  if (add_to_fav_button.classList.contains('delete-button')) {
                      add_to_fav_button.classList.remove('delete-button');
                      add_to_fav_button.textContent = 'Add to favorites';
                      console.log('Removed from favorites: success');
                  } else {
                      add_to_fav_button.classList.add('delete-button');
                      add_to_fav_button.textContent = 'Remove from favorites';
                      console.log('Add to favorites: success');
                  }
                  break;
              case 404:
                  console.log('Film not found.');
                  break;
              default:
                  console.log('Unknown error')
          }
    });
});
