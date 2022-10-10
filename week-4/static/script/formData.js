
const btn = document.querySelector('#submit');

async function postData(url = '', data = {}) {
    // Default options are marked with *
    try{
        const response = await fetch(url, {
            method: 'POST', // *GET, POST, PUT, DELETE, etc.
            mode: 'cors', // no-cors, *cors, same-origin
            cache: 'no-cache', // *default, no-cache, reload, force-cache, only-if-cached
            credentials: 'same-origin', // include, *same-origin, omit
            headers: {
                'Content-Type': 'application/json'
                // 'Content-Type': 'application/x-www-form-urlencoded',
            },
            redirect: 'follow', // manual, *follow, error
            referrerPolicy: 'no-referrer', // no-referrer, *no-referrer-when-downgrade, origin, origin-when-cross-origin, same-origin, strict-origin, strict-origin-when-cross-origin, unsafe-url
            body: JSON.stringify(data) // body data type must match "Content-Type" header
            });
            response.redirected?window.location.href = response.url:void 0;  // parses JSON response into native JavaScript objects
    }catch(err){
        console.log(err)
    }
}

btn.addEventListener('click', (e) => {
    // prevent the form from submitting
    e.preventDefault();
    let signinData = {};
    // show the form values
    const formData = new FormData(document.getElementById('form'));
    for(let [key, value] of formData.entries()) {
        value?signinData[key] = value:void 0;
    }
    postData("/signin", signinData)
});