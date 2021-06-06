//Question 1

let array = [];

let i = 0;

while(i<=100){
    array.push(i);
    i++;
}
console.log(array);
// Question 2

let even_array = [];
i = 0;
while(i<100){
    if(array[i]%2==0){
        even_array.push(array[i]);
    }
   i++;
}
console.log(even_array);


// Function that returns the square of even numbers and throws an error if odd no is passed

async function evenSquare(value){

    return new Promise((resolve,reject)=>{

        if(value % 2 == 0){
            resolve(Math.pow(value,2));
        }
        else{
            reject({message:"Please input an even number"});
        }
    })

}

//Question 3 and 4

let even_squares = [];

console.log("even array is ",even_array);

let even_squares_sum = 0;  // sum of all even squares

even_array.forEach(async(element)=>{

    try{
     const result = await evenSquare(element);
     even_squares.push(result);
     even_squares_sum+=result;
    }
    catch(err){

    }

})

//Question 5

let result = [];

array.forEach( async(element)=>{
    
    try{
     const result = await evenSquare(element);
     even_squares.push(result);
     even_squares_sum+=result;
    }
    catch(err){
     
        result.push(err);

    }

})

// the length of result is the no of errors .



