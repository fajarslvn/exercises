"use strict";
const questions = [
    {
        id: 1,
        text: 'What is the full birth name of Boy George?',
        answer: 'George Alan O\'Dowd',
        wrongAnswers: ['George Phillips', 'Johnny Cash', 'Bill Freud'],
    },
    {
        id: 2,
        text: 'According to legend, which plant screams when the root is dug up?',
        answer: 'Mandrake',
        wrongAnswers: ['Daisy', 'Potato', 'Jasmine'],
    },
    {
        id: 3,
        text: 'What fruit appears on the first screen in the original "Pac-Man" arcade game?',
        answer: 'Cherry',
        wrongAnswers: ['Apple', 'Kiwi', 'Banana'],
    }
];
const scoreEl = document.getElementById('score'); // Possibly null
const answersSelectEl = document.getElementById('answersSelect'); // Possibly null
const questionTextEl = document.getElementById('questionText'); // Possibly null
const submitButtonEl = document.getElementById('submitButton'); // Possibly null
const startButtonEl = document.getElementById('startButton'); // Possibly null
let index = 0;
let correct = 0;
if (scoreEl &&
    answersSelectEl &&
    questionTextEl &&
    submitButtonEl &&
    startButtonEl) {
    const getNextQuestion = () => {
        return questions[index++];
    };
    const scrambleAnswers = (answers) => {
        return answers.sort(() => Math.random() - 0.5);
    };
    const displayQuestion = (q) => {
        questionTextEl.innerText = q.text;
        answersSelectEl.innerHTML = '';
        const answers = scrambleAnswers([...q.wrongAnswers, q.answer]);
        answers.forEach(answers => {
            const newAnswer = document.createElement('option');
            newAnswer.value = answers;
            newAnswer.innerText = answers;
            answersSelectEl.appendChild(newAnswer);
        });
    };
    const showScore = () => {
        const score = Math.floor((correct / questions.length) * 100);
        answersSelectEl.style.display = 'none';
        questionTextEl.style.display = 'none';
        submitButtonEl.style.display = 'none';
        scoreEl.style.display = 'block';
        scoreEl.innerText = 'Your score: ' + score + '%';
    };
    submitButtonEl.addEventListener('click', () => {
        if (questions[index - 1].answer === answersSelectEl.value) {
            correct++;
        }
        if (index < questions.length) {
            displayQuestion(getNextQuestion());
        }
        else {
            showScore();
        }
    });
    startButtonEl.addEventListener('click', () => {
        startButtonEl.style.display = 'none';
        submitButtonEl.style.display = 'block';
        questionTextEl.style.display = 'block';
        answersSelectEl.style.display = 'block';
        displayQuestion(getNextQuestion());
    });
}
