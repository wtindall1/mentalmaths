const url = 'http://127.0.0.1:8000';

async function getHighScores() {

    const response = await fetch(url + '/get_scores');
    const data = await response.json();

    return data;

}

async function displayInitialHighScores() {

    data = await getHighScores();

    for (const [key, value] of Object.entries(data)) {
        highScores[key] = value.score;
        //update the displayed value
        document.querySelector(`.highscore #scorehigh_${key} span`).textContent = value.score;
    }
}

async function getProblem() {

    //call backend to get problem
    const request = new Request(url, {
        method: 'POST',
        body: `{"level": "${level}"}`,
        headers: {'Content-Type' : 'application/json'}
    });

    console.log(request);

    const response = await fetch(request);
    const data = await response.json();

    // console.log(data);
    return data;
};


async function setProblem() {
    
    const problem = await getProblem();

    const num1 = problem.num1;
    const num2 = problem.num2;


    //set question on the page
    const question = document.querySelector('.question')
    //set answer on page - will be invisible
    const answer = document.querySelector('.answer');

    question.textContent = `${num1} * ${num2} =`;
    answer.textContent = problem.answer;

    problemDisplayed = problem
};

function setLevel() {

    const displayLevel = document.querySelector(".displaylevel_value");

    //change level to the value of the clicked button
    switch (this.value) {
        case 'easy': {
            level = 'easy';
            displayLevel.style.backgroundColor = 'springgreen';
            break;
        }
        case 'medium': {
            level = 'medium';
            displayLevel.style.backgroundColor = 'yellow';
            break;
        } 
        case 'hard': {
            level = 'hard';
            displayLevel.style.backgroundColor = 'red';
            break;
        }
    };

    displayLevel.textContent = level;

    //reset the current streak
    currentScore = 0;
    document.querySelector('.highscore .scorecurrent span').textContent = currentScore;

    //new problem
    setProblem();

}

function updateHighScore() {

    //set high score for current level
    Object.keys(highScores).forEach(key => {
        if (level === key && currentScore > highScores[key]) {

            highScores[key] = currentScore;
            document.querySelector(`.highscore #scorehigh_${key} span`).textContent = currentScore;
            
            saveScoresToDB(level, currentScore);
        }
    });

    currentScore = 0
    document.querySelector('.highscore .scorecurrent span').textContent = currentScore;
}


function checkAnswer(problem) {
    
    
    //get user answer from text input box
    userAnswer = document.getElementById('user_answer').value;
    //convert to number
    userAnswer = +userAnswer

    //check against problem answer
    userAnswer === problem.answer ? console.log('correct') : console.log('incorrect');

    //if incorrect, apply red effect and update high score
    if (userAnswer !== problem.answer) {
        document.querySelector('.problem').classList.add('incorrect');
        document.querySelector('.answer').classList.add('visible');

        updateHighScore();

    } else {
        //if correct, apply green effect and add to streak counter
        document.querySelector('.problem').classList.add('correct');
        
        //update streak counter
        currentScore++;
        document.querySelector('.highscore .scorecurrent span').textContent = currentScore;
    }
    
    //clear the input box
    document.getElementById('user_answer').value = "";
}


async function enterHandler(event) {

    if (event.key === 'Enter') {

        //check answer & do transition effect
        checkAnswer(problemDisplayed);

        //reset problem
        // await setProblem();
        setTimeout(setProblem, 800)
    }
}

function removeTransition(event) {
    if (event.propertyName !== 'transform') return;
    document.querySelector('.problem').classList.remove('incorrect', 'correct');
    document.querySelector('.answer').classList.remove('visible');
}


async function saveScoresToDB(level, score) {

    const request = new Request(url + '/save_scores', {
        method: 'POST',
        headers: {'Content-Type' : 'application/json'},
        body: `{
            "user_name": "Will",
            "level": "${level}",
            "score": ${score}
        }`
    });

    const response = await fetch(request);
    const data = await response.json();

    return data;
}




let problemDisplayed;

//high score & streak counter 
let currentScore = 0;

//set high scores
let highScores = {};
displayInitialHighScores();

//initial problem difficulty
let level = 'easy';
setLevel(level);


//update problem difficulty
document.getElementById("easy").addEventListener("click", setLevel);
document.getElementById("medium").addEventListener("click", setLevel);
document.getElementById("hard").addEventListener("click", setLevel);


//listener for removing green/red effect
document.addEventListener("transitionend", removeTransition)
//check answer and reset problem
document.addEventListener("keydown", enterHandler);




























