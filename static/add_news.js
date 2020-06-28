document.addEventListener('DOMContentLoaded', () => {
    // 1. hook na formularz na event submit
    // 2. dane z formularza przekazać do REST API
    // 3. ???
    const form = document.querySelector('form');
    form.onsubmit = event => {
        const request = new XMLHttpRequest();
        request.open('POST', '/api/v1/news/create');

        request.onload = () => {
            const data = JSON.parse(request.responseText);
            console.log(data);
            // ??? - @todo :P
        }

        // jak to działa? - @todo :P
        // request.onerror = () => {
        //     console.log(request.responseText);
        // }

        const requestData = new FormData(form);
        request.setRequestHeader('X-CSRFToken', document.querySelector('#news-script').dataset.csrftoken);

        request.send(requestData);

        // nie wysyłaj formularza...
        event.preventDefault();
    }

    document.querySelector('#button-id-cancel').onclick = () => {
        location.href = '/news';
    }
});
