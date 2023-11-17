let textAreas = document.querySelectorAll('textarea');

textAreas.forEach((elem) => 
    elem.addEventListener("input", function() {
        this.style.height = '0px';
        this.style.height = this.scrollHeight + 'px';
    })
);