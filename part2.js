
//Question 1

var button = "My button";
let buttonhtml = `<button type="button">${button}</button>`

// Question 2


function list(value) {
    return `<li>${value}</li>`
}


//In react or jsx we render in such a format

function renderlist() {


    // Question 2
    let array = []
    for (let i = 0; i < 30; i++) {
        array.push(i);
    }
    // Question 3 even numbers

    for (let i = 0; i < 30; i+=2) {
        array.push(i);
    }


    return array.map((value) => list(value));



}


//Question 4

let promiseArray = [];


function PromiseSettings(){

    for(let i = 1;i<=10;i++){
        let promiseName = `promise${i}`;
         
        promiseName = new Promise((resolve,reject)=>{
            setTimeout(()=>{
             resolve("Promise executed after 3 seconds")
            },3000)
        })
        promiseArray.push(promiseName);
    }
    Promise.all((values)=>{
        console.log("All promise executed with delays")
    })
}




