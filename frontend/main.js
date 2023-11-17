
/* Make each text area dynamically change height */
let textAreas = document.querySelectorAll('textarea');

textAreas.forEach((elem) => 
    elem.addEventListener("input", function() {
        this.style.height = '0px';
        this.style.height = this.scrollHeight + 'px';
    })
);

/* Typing animation */
let hasStartedTyping = false;

let textElem = document.querySelector(".generatedText");

let textToType = "The phrase “it's just a game” is such a weak mindset. You are ok with what happened, losing, imperfection of a craft. When you stop getting angry after losing, you've lost twice. There's always something to learn, and always room for improvement, never settle.";
let splitText = textToType.split(' ');
let wordIndex = 0;


function typeText() {
    if (wordIndex < splitText.length) {
        textElem.innerHTML = textElem.innerHTML.slice(0, -2) + splitText[wordIndex] + "  •";
        wordIndex++;
    } else if (wordIndex == splitText.length) {
        textElem.innerHTML = textElem.innerHTML.slice(0, -2);
        wordIndex++;
    }
}

function onGenerateText() {
    textElem.innerHTML = "";
    wordIndex = 0;
    if (!hasStartedTyping) {
        setInterval(typeText, 70);
        hasStartedTyping = true;
    }
}

function setTextToEmpty() {
    textElem.innerHTML = "";
}

function setTextToCursor() {
    textElem.innerHTML = " •";
}

/* Copy to clipboard */

function copyToClipboard() {
    let copyText = document.querySelector(".generatedText").innerHTML;

    // Copy the text inside the text field
    navigator.clipboard.writeText(copyText);

    // Alert the copied text
    alert("Copied the text: " + copyText);
}
