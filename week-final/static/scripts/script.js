
const submitLoginForm = document.querySelector('.submitLoginForm');

const submitSignupForm = document.querySelector('.submitSignupForm');

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

submitLoginForm.addEventListener('click', (e) => {
    e.preventDefault();
    const formData = new FormData(document.querySelector('loginForm'));
    let json = {
        username:formData.get("username"),
        password:formData.get("password")
    };
    console.log(signinData)
    postData("/login", json)
});

submitNumBtn.addEventListener('click', (e) => {
    e.preventDefault();
    const formData = new FormData(document.getElementById('formNum'));
    window.location.href = `/square/${formData.get("naturalNumber").toString()}`
});