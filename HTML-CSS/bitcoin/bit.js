
document.querySelector('.investment__btn').addEventListener('click',function(){
const btcusdbought = document.querySelector('.price__input--bought').value;
const btcusdnow = document.querySelector('.price__input--now').value;
const btc = document.querySelector('.investment__btc').value;

const invested=btc* btcusdbought;
const current = btc*btcusdnow;
const profit =current - invested;
const growth = profit/invested*100;
let message=""

if(profit>0)
{
	message="Great! you have made profit of "+profit+"("+growth +"%).";
	document.querySelector('.result').style.color = 'green';
}
else if(profit<0){
message ="oh no you are in loss of "+profit+"("+growth +"% ).";
	document.querySelector('.result').style.color = 'red';
}
else
{
	message="you are breaking even!"
}
console.log(message);

document.querySelector('.result').textContent = message;
});

