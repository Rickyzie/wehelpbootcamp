
const submitLoginBtn = document.querySelector('#submitLogin');
const submitNumBtn = document.querySelector('#submitNum');

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

submitLoginBtn.addEventListener('click', (e) => {
    // prevent the form from submitting
    e.preventDefault();
    // show the form values
    const formData = new FormData(document.getElementById('formLogin'));
    let signinData = {
        account:formData.get("account"),
        password:formData.get("password")
    };
    console.log(signinData)
    postData("/signin", signinData)
});

submitNumBtn.addEventListener('click', (e) => {
    // prevent the form from submitting
    e.preventDefault();
    // show the form values
    const formData = new FormData(document.getElementById('formNum'));
    window.location.href = `/square/${formData.get("naturalNumber").toString()}`
});