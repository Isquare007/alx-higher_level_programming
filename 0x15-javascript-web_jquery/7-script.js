// Write a JavaScript script that fetches the character name from this URL
// URL: https://swapi-api.alx-tools.com/api/people/5/?format=json

const url = 'https://fourtonfish.com/hellosalut/?lang=fr';
$.get(url, function (data, textStatus) {
    if (textStatus === 'success'){
        $('#character').text(data.name);
    }
})