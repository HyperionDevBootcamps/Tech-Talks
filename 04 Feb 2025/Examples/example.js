// (A + B).(A + C) = A + (B.C)

let A = false;
let B = true;
let C = false;

if ((A || B) && (A || C)) {
  console.log("It worked");
} else {
  console.log("It didn't work");
}

// A + (B.C)
// let A = false;
// let B = true;
// let C = false;
// if (A || (B && C)) {
//   console.log("It worked");
// } else {
//   console.log("It didn't work");
// }

// let name = "John";
// let bootcamp = "WD";
// if (bootcamp != "DS" && bootcamp == "DS") {
//   console.log("It worked");
// } else {
//   console.log("It didn't work");
// }
