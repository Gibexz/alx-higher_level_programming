const urll = 'https://swapi-api.hbtn.io/api/films/?format=json';

$.get(urll, data => {
  data.results.forEach(movie => {
    $('UL#list_movies').append(`<li>${movie.title}</li>`);
  });
});
