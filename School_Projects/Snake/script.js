let coords = "3x7";
let length = 1;
let rcoords = "8x7";
var score = 0;
var result = "ArrowRight";
const allCells = document.querySelectorAll('.cells');

document.getElementById(coords).style.background = "limeGreen";
document.getElementById(rcoords).style.background = "red";
document.getElementById("start_game").addEventListener("click",start);
function start(){
document.getElementById("start_game").style.display = "none";
pleaseWork("ArrowRight");
}
function pleaseWork(e){
  runningFunction = false;
  console.log(e)
  if (e!="ArrowRight"&&e!="ArrowLeft"&&e!="ArrowUp"&&e!="ArrowDown"){
  e=e.key;
  }
  if (e=="ArrowRight"||e=="ArrowLeft"||e=="ArrowUp"||e=="ArrowDown"){
  returnArray = funct(e,coords);
  coords = returnArray[0];
  prevEvent = returnArray[1];
  if (coords==rcoords){
    score+=1;
    length+=1;
  document.getElementById("score").innerHTML="Score: "+score;  
    rcoordsx = Math.floor(Math.random()*11)+1;
    rcoordsy = Math.floor(Math.random()*13)+1;
    rcoords = rcoordsx+"x"+rcoordsy;
    while (rcoords==coords){
      rcoordsx = Math.floor(Math.random()*11)+1;
      rcoordsy = Math.floor(Math.random()*13)+1;
      rcoords = rcoordsx+"x"+rcoordsy;
    }
    document.getElementById(rcoords).style.background = "red";
  }
  window.addEventListener("keydown",function (edo){
    result = edo.key
  }); 
  let timer = 500-(25*score);
  if (timer<100){
    timer=100;
  }
  setTimeout(pleaseWork,timer,result)
  }

function funct(event,coords){
  var switchState = event;
  if (switchState=="ArrowRight"){
    coords = moveRight(event,coords);
    return [coords, switchState]
  }else if(switchState=="ArrowLeft"){
    coords = moveLeft(event,coords);
    return [coords, switchState]
  }else if(switchState=="ArrowUp"){
    coords = moveUp(event,coords);
    return [coords, switchState]
  }else if(switchState=="ArrowDown"){
    coords = moveDown(event,coords);
    return [coords, switchState]
  }
}
function moveRight(event,coords){
  let coords2 = coords;
  let coordssplit = coords2.split("x");
  let newx = parseInt(coordssplit[0],10) + 1;
  if (newx>11){
    gameOver();
  }
  let coords3 = String(newx)+"x"+coordssplit[1]
    document.getElementById(coords3).style.background="limeGreen";
  document.getElementById(coords).style.background="darkGray";
  return coords3
}
function moveLeft(event,coords){
  let coords2 = coords;
  let coordssplit = coords2.split("x");
  let newx = parseInt(coordssplit[0],10) - 1;
  if (newx<1){
    gameOver();
  }
  let coords3 = String(newx)+"x"+coordssplit[1]
  document.getElementById(coords).style.background="darkGray";
  document.getElementById(coords3).style.background="limeGreen";
  return coords3
}
function moveUp(event,coords){
  let coords2 = coords;
  let coordssplit = coords2.split("x");
  let newy = parseInt(coordssplit[1],10) - 1;
  if (newy<1){
    gameOver();
  }
  let coords3 = coordssplit[0]+"x"+String(newy);
  document.getElementById(coords).style.background="darkGray";
  document.getElementById(coords3).style.background="limeGreen";
  return coords3
}
function moveDown(event,coords){
  let coords2 = coords;
  let coordssplit = coords2.split("x");
  let newy = parseInt(coordssplit[1],10) + 1;
  if (newy>13){
    gameOver();
  }
  let coords3 = coordssplit[0]+"x"+String(newy);

  document.getElementById(coords).style.background="darkGray";
  document.getElementById(coords3).style.background="limeGreen";
  return coords3
}
function gameOver(){
  allCells.forEach(cell => {
    cell.style.display="none";
});
    document.getElementById("game_over").innerHTML="GAME OVER";
document.getElementById("new_game").style.display="inline-block";
document.getElementById("new_game").addEventListener("click",newGame);
return
}
return}
function newGame(){
  location.reload();
}