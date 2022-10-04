function TopComponent(src, title){
    const divTop = document.createElement("div");
    divTop.setAttribute("class", "Top");
    const divImgWrapper = document.createElement("div");
    divImgWrapper.setAttribute("class", "ImgWrapper");
    divImgWrapper.style.backgroundImage = src;
    const divContext = document.createElement("div");
    divContext.setAttribute("class", "Context");
    const img = new Image();
    img.src = src;
    divTop.appendChild(divImgWrapper);
    divTop.appendChild(divContext).textContent = title;
    divImgWrapper.appendChild(img);
    document.querySelector(".Content").appendChild(divTop);
}

function CardComponent(src, title){
    const divTop = document.createElement("div");
    divTop.setAttribute("class", "Card");
    const divImgWrapper = document.createElement("div");
    divImgWrapper.setAttribute("class", "ImgWrapper"); 
    divImgWrapper.style.backgroundImage = `url(${src})`; 
    const divContext = document.createElement("div");
    divContext.setAttribute("class", "Title");
    divTop.appendChild(divImgWrapper);
    divTop.appendChild(divContext).textContent = title;
    document.querySelector(".Content").appendChild(divTop);
}
