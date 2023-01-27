// Write a JavaScript script that fetches and lists the title for all movies by using this
// URL: https://swapi-api.alx-tools.com/api/films/?format=json

const url = "https://swapi-api.alx-tools.com/api/films/?format=json";
$.get(url, function (data, status) {
    if (status === 'success') {
        films = data.results
        films.forEach(film => {
            $("#list_movies").append("<li>" + film.title + "</li>");
        });
    }
});