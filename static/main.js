document.addEventListener('DOMContentLoaded', () => {
    loadNews();
});

const loadNews = url => {

    // Tworzymy obiekt request, który będzie umiał pytać backend o dane
    const request = new XMLHttpRequest();

    // Jeżeli url nie został ustawiony, tworzymy domyślny
    if (typeof url === 'undefined') {
        url = '/api/v1/news';
    }

    // otwieramy połączenie z backendem po URL metodą GET
    request.open('GET', url);

    // opisujemy jak ma zachować się aplikacja po otrzymaniu danych z backendu.
    request.onload = () => {
        // zamieniamy otrzymany string na obiekt JSON
        const data = JSON.parse(request.responseText);

        // wywołujemy funkcję do wyświetlenia listy newsów
        showNews(data);
    }

    // poniższe tylko, jeżeli przekazujemy FORM przez AJAX metodą POST / PUT
    // const requestData = new FormData(document.querySelector('#extras-form'));
    // requestData.append('fooid', 'dweweffef')
    // request.setRequestHeader('X-CSRFToken', document.querySelector('#news-script').dataset.csrftoken);
    // request.send(requestData);

    // wysyłamy request do backendu
    request.send()
}

const showNews = data => {
    // mówimy systemowi szablonów, jakiego HTMLa będziemy używać (w tym przypadku HTML zawarty jest w bloku script)
    let newsTemplate = Handlebars.compile(document.querySelector('#news-item').innerHTML);

    // Czyścimy artefakty z listy newsów
    document.querySelector('#news_list').innerHTML = '';

    // uzupełniamy listę newsów
    for (let i = 0; i < data.results.length; i++) {

        // tworzymy JSONa, który pozwoli systemowi szablonów zamienić nazwy zmiennych na wartości
        let news = {
            'news_id': data.results[i]['id'],
            'news_url': `/news/${data.results[i]['id']}`,
            'news_title': data.results[i]['title']
        }

        // dodajemy wyrenderowany rekord do bloku <UL>
        document.querySelector('#news_list').innerHTML += newsTemplate(news);
    }
}