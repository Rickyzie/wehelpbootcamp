async function postData(url = '', data = {}) {
    try{
        const response = await fetch(url, {
            method: 'POST', 
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data) 
            });
            console.log(response);
    }catch(err){
        console.log(err)
    }
}