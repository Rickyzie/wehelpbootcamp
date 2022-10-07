let counter = 10;
let canScroll = false;
let data
const ScrollLoader = document.querySelector('.ScrollLoader')

const option = {
    root: null,
    rootMargin: "20px",
    threshold: 0
};
const handleObserver = (entries) => {
    const target = entries[0];
    if (target.isIntersecting && canScroll) {
        for(let i = 0;i < 4; i++){
            counter++;
            if(!localStorage.getItem(counter)) return
            CardComponent(JSON.parse(
                localStorage.getItem(counter)).file.match(/http.*?jpg/i), 
                JSON.parse(localStorage.getItem(counter)).stitle)
            console.log(data)
        }
    }
};

const observer = new IntersectionObserver(handleObserver, option);
if (ScrollLoader) observer.observe(ScrollLoader);


