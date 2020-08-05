let humanScore = 0;
let computerScore = 0;
let currentRoundNumber = 1;

//generating the secret number
const generateTarget = () => Math.floor(Math.random() * 9) + 1;

//getting the absolute distance between the guesses and the secret number (used in the compareGusses function that comes next)
const getAbsoluteDistance = (guessNumber , secretNumber) => Math.abs(guessNumber - secretNumber);

//comparing the computer and the human guesses
function compareGuesses(humanGuess , computerGuess , secretNumber) {
    //validating human guess
    if(humanGuess < 0 || humanGuess > 9){
        alert('Round lost due to Invalid Guess, please ensure guess is between 0-9');
        return false;
    }
    //getting the absolute distance
    const humanGuessDifference = getAbsoluteDistance(humanGuess , secretNumber);
    const computerGuessDifference = getAbsoluteDistance(computerGuess , secretNumber);
    
    //figuring out if the human guess or the computer guess were closer to the target
    if (humanGuessDifference === computerGuessDifference) {
        return true;
    } else if (humanGuessDifference > computerGuessDifference) {
        return false;
    } else {
        return true;
    }
}

//updating the score
function updateScore(winner) {
    if (winner === 'human') {
        humanScore++;
    } else {
        computerScore++;
    }
}

// advancing the round
const advanceRound = () => currentRoundNumber++;