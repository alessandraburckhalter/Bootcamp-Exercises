const myButton = document.getElementById('clickMe');
const noun1 = document.getElementById('noun1');
const myButton2 = document.getElementById('clickMe2');
const noun2 = document.getElementById('noun2');
const myButton3 = document.getElementById('clickMe3');
const noun3 = document.getElementById('noun3');
const myButton4 = document.getElementById('clickMe4');
const noun4 = document.getElementById('noun4');
const myButton5 = document.getElementById('clickMe5');
const noun5 = document.getElementById('noun5');
const myButton6 = document.getElementById('clickMe6');
const noun6 = document.getElementById('noun6');

const noun1Input = document.getElementById('noun1Input');
const noun2Input = document.getElementById('noun2Input'); 
const noun3Input = document.getElementById('noun3Input'); 
const noun4Input = document.getElementById('noun4Input');
const noun5Input = document.getElementById('noun5Input');
const noun6Input = document.getElementById('noun6Input');

myButton.addEventListener('click', function (event) {
  event.preventDefault();
  noun1.innerHTML = noun1Input.value;
})
myButton2.addEventListener('click', function (event) {
    event.preventDefault();
  noun2.innerHTML = noun2Input.value;
});
myButton3.addEventListener('click', function (event) {
    event.preventDefault();
  noun3.innerHTML = noun3Input.value;
});
myButton4.addEventListener('click', function (event) {
  event.preventDefault();
noun4.innerHTML = noun4Input.value;
});
myButton5.addEventListener('click', function (event) {
  event.preventDefault();
noun5.innerHTML = noun5Input.value;
});
myButton6.addEventListener('click', function (event) {
  event.preventDefault();
noun6.innerHTML = noun6Input.value;
});