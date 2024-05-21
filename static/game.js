const moves = document.getElementById("moves-count");
const timeValue = document.getElementById("time");
const startButton = document.getElementById("start");
const stopButton = document.getElementById("stop");
const gameContainer = document.querySelector(".game-container");
const result = document.getElementById("result");
const controls = document.querySelector(".control-container");
let cards;
let interval;
let firstCard = false;
let secondCard = false;


const items = [
    {name: "color1", image: "../images/1.png"},
    {name: "color2", image: "../images/2.png"},
    {name: "color3", image: "../images/3.png"},
    {name: "color4", image: "../images/4.png"},
    {name: "color5", image: "../images/5.png"},
    {name: "color6", image: "../images/6.png"},
    {name: "color7", image: "../images/7.png"},
    {name: "color8", image: "../images/8.png"},
    {name: "color9", image: "../images/9.png"},
    {name: "color10", image: "../images/10.png"},
    {name: "color11", image: "../images/11.png"},
    {name: "color12", image: "../images/12.png"},
    {name: "color13", image: "../images/13.png"},
    {name: "color14", image: "../images/14.png"},
    {name: "color15", image: "../images/15.png"},
    {name: "color16", image: "../images/16.png"},
    {name: "color17", image: "../images/17.png"},
    {name: "color18", image: "../images/18.png"},
    {name: "color19", image: "../images/19.png"},
    {name: "color20", image: "../images/20.png"},
];

let seconds = 0,
    minutes = 0;

let movesCount = 0,
    winCount = 0;

const timeGenerator = () => {
    seconds += 1;
    if (seconds >= 60) {
        minutes += 1;
        seconds = 0;
    }
    let secondsValues = seconds < 10 ? `0${seconds}` : seconds;
    let minuteValues = minutes < 10 ? `0${minutes}` : minutes;
    timeValue.innerHTML = `<span>Time: </span>${minuteValues}:${secondsValues}`;
};

const movesCounter = () => {
    movesCount += 1;
    moves.innerHTML = `<span>Moves: </span>${movesCount}`;
};

const generateRandom = (size = 4) => {
    let tempArray = [...items];
    let cardValues = [];
    size = (size * size) / 2;
    for (let i = 0; i < size; i++) {
        const randomIndex = Math.floor(Math.random() * tempArray.length);
        cardValues.push(tempArray[randomIndex]);
        tempArray.splice(randomIndex, 1);
    }
    return cardValues;
};


const matrixGenerator = (cardValues, size = 4) => {
    gameContainer.innerHTML = "";
    cardValues = [...cardValues, ...cardValues];

    cardValues.sort(() => Math.random() - 0.5);
    for (let i = 0; i < size * size; i++) {

        gameContainer.innerHTML += `
     <div class="card-container" data-card-value="${cardValues[i].name}">
        <div class="card-before">?</div>
        <div class="card-after">
            <img src="${cardValues[i].image}" alt="cards" class="image"/>
        </div>
     </div>
     `;
    }

    gameContainer.style.gridTemplateColumns = `repeat(${size},auto)`;

    cards = document.querySelectorAll(".card-container");
    cards.forEach((card) => {
        card.addEventListener("click", () => {

            if (!card.classList.contains("matched")) {

                card.classList.add("flipped");

                if (!firstCard) {

                    firstCard = card;

                    firstCardValue = card.getAttribute("data-card-value");
                } else {

                    movesCounter();

                    secondCard = card;
                    let secondCardValue = card.getAttribute("data-card-value");
                    if (firstCardValue === secondCardValue) {

                        firstCard.classList.add("matched");
                        secondCard.classList.add("matched");

                        firstCard = false;

                        winCount += 1;

                        if (winCount === Math.floor(cardValues.length / 2)) {
                            result.innerHTML = `<h2>You Won</h2>
                        <h4>Moves: ${movesCount}</h4>`;
                            stopGame();
                        }
                    } else {

                        let [tempFirst, tempSecond] = [firstCard, secondCard];
                        firstCard = false;
                        secondCard = false;
                        setTimeout(() => {
                            tempFirst.classList.remove("flipped");
                            tempSecond.classList.remove("flipped");
                        }, 500);
                    }
                }
            }
        });
    });
};

startButton.addEventListener("click", () => {
    movesCount = 0;
    seconds = 0;
    minutes = 0;

    controls.classList.add("hide");
    stopButton.classList.remove("hide");
    startButton.classList.add("hide");

    interval = setInterval(timeGenerator, 1000);

    moves.innerHTML = `<span>Moves: </span> ${movesCount}`;
    initializer();
});

stopButton.addEventListener(
    "click",
    (stopGame = () => {
        controls.classList.remove("hide");
        stopButton.classList.add("hide");
        startButton.classList.remove("hide");
        clearInterval(interval);
    })
);

const initializer = () => {
    result.innerText = "";
    winCount = 0;
    let cardValues = generateRandom();
    console.log(cardValues);
    matrixGenerator(cardValues);
}


// // initGame();
// //
// // function initGame() {
// //
// //     // Your game can start here, but define separate functions, don't write everything in here :)
// //
// // }
