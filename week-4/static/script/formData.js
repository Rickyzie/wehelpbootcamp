const submitLoginBtn = document.querySelector('#submitLogin');

const submitNumBtn = document.querySelector('#submitNum');

async function postData(url = '', data = {}) {
    try{
        const response = await fetch(url, {
            method: 'POST', 
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data) 
            });
            response.redirected?window.location.href = response.url:void 0;  
    }catch(err){
        console.log(err)
    }
}

submitLoginBtn.addEventListener('click', (e) => {
    e.preventDefault();
    const formData = new FormData(document.getElementById('formLogin'));
    let signinData = {
        account:formData.get("account"),
        password:formData.get("password")
    };
    console.log(signinData)
    postData("/signin", signinData)
});

submitNumBtn.addEventListener('click', (e) => {
    e.preventDefault();
    const formData = new FormData(document.getElementById('formNum'));
    window.location.href = `/square/${formData.get("naturalNumber").toString()}`
});