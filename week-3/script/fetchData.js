async function getData(){
    await fetch('https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json')
    .then(function(response) {
        return response.json();
    }).then(function(jsonData) {
        let { results } = jsonData.result;
        results.map((val, index)=>{
            if(index>9) return localStorage.setItem(index,  JSON.stringify(val));
            index<2?TopComponent(val.file.match(/http.*?jpg/i), val.stitle):CardComponent(val.file.match(/http.*?jpg/i), val.stitle);
        }).join(" ");
        canScroll = true;
    })
}

getData()




