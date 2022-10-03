import { TopComponent } from "./component.js";

import (TopComponent)
async function getData(){
    await fetch('https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json')
    .then(function(response) {
        return response.json();
    }).then(function(jsonData) {
        let { results } = jsonData.result;
        results.map((val, index)=>{
            if(index>9) return
            index<2?TopComponent(val.file.match(/http.*?jpg/i), val.stitle):CardComponent(val.file.match(/http.*?jpg/i), val.stitle);
        }).join(" ");
    })
}

getData()

function CardComponent(src, title){
    let divTop = document.createElement("div");
    divTop.setAttribute("class", "Card");
    let divImgWrapper = document.createElement("div");
    divImgWrapper.setAttribute("class", "ImgWrapper"); 
    divImgWrapper.style.backgroundImage = `url(${src})`; 
    let divContext = document.createElement("div");
    divContext.setAttribute("class", "Title");
    divTop.appendChild(divImgWrapper);
    divTop.appendChild(divContext).textContent = title;
    document.querySelector(".Content").appendChild(divTop);
}


