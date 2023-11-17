// let hasStartedTyping = false;

// let textElem = document.querySelector(".backgroundText");

// let textToType = "Salt air, and the rust on your door I never needed anything more Whispers of \"Are you sure?\" \"Never have I ever before\" But I can see us lost in the memory August slipped away into a moment in time 'Cause it was never mine And I can see us twisted in bedsheets August sipped away like a bottle of wine 'Cause you were never mine Your back beneath the sun Wishin' I could write my name on it Will you call when you're back at school? I remember thinkin' I had you But I can see us lost in the memory August slipped away into a moment in time 'Cause it was never mine And I can see us twisted in bedsheets August sipped away like a bottle of wine 'Cause you were never mine Back when we were still changin' for the better Wanting was enough For me, it was enough To live for the hope of it all Cancel plans just in case you'd call And say, \"Meet me behind the mall\" So much for summer love and saying \"us\" 'Cause you weren't mine to lose You weren't mine to lose, no But I can see us lost in the memory August slipped away into a moment in time 'Cause it was never mine And I can see us twisted in bedsheets August sipped away like a bottle of wine 'Cause you were never mine 'Cause you were never mine, never mine But do you remember? Remember when I pulled up and said, \"Get in the car\" And then canceled my plans just in case you'd call? Back when I was livin' for the hope of it all, for the hope of it all \"Meet me behind the mall\" Remember when I pulled up and said, \"Get in the car\" And then canceled my plans just in case you'd call? Back when I was livin' for the hope of it all (for the hope of it all) For the hope of it all For the hope of it all (For the hope of it all) (For the hope of it all)";
// let splitText = textToType.split(' ');
// let wordIndex = 0;
// /* Typing animation */

// function typeText() {
//     if (wordIndex < splitText.length) {
//         textElem.innerHTML = textElem.innerHTML.slice(0, -2) + splitText[wordIndex] + "  •";
//         wordIndex++;
//     } else if (wordIndex == splitText.length) {
//         textElem.innerHTML = textElem.innerHTML.slice(0, -2);
//         wordIndex++;
//     }
// }

// setInterval(typeText, 40);


const textArray = [
    "Biology",
    "Computer Science",
    "Music",
    "Engineering",
    "Mathematics",
    "Quantum Mechanics",
    "Harry Potter Studies",
    "Eating",
    "Pop Culture",
    "Elvin Filmic Studies"
  ];
  
  // Initialize variables
  let typeJsText = document.querySelector(".animatedText");
  let stringIndex = 0;
  let charIndex = 0;
  let isTyping = true;
  
  function typeJs() {
    if (stringIndex < textArray.length) {

      const currentString = textArray[stringIndex];
  
      if (isTyping) {
        // Typing animation
        if (charIndex < currentString.length) {
          typeJsText.innerHTML += currentString.charAt(charIndex);
          charIndex++;
        } else {
          isTyping = false;
        }
      } else {
        // Erasing animation
        if (charIndex > 0) {
          typeJsText.innerHTML = currentString.substring(0, charIndex - 1);
          charIndex--;
        } else {
          isTyping = true;
          stringIndex++;
  
          if (stringIndex >= textArray.length) {
            stringIndex = 0;
          }
  
          charIndex = 0;
        }
      }
    }
  }

  setInterval(typeJs, 90);