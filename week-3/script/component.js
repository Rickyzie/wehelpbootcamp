export function TopComponent(src, title){
    let divTop = document.createElement("div");
    divTop.setAttribute("class", "Top");
    let divImgWrapper = document.createElement("div");
    divImgWrapper.setAttribute("class", "ImgWrapper");
    divImgWrapper.style.backgroundImage = src;
    let divContext = document.createElement("div");
    divContext.setAttribute("class", "Context");
    let img = new Image();
    img.src = src;
    divTop.appendChild(divImgWrapper);
    divTop.appendChild(divContext).textContent = title;
    divImgWrapper.appendChild(img);
    document.querySelector(".Content").appendChild(divTop);
}