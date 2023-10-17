function potholePatch(S){
    let count = 0;
    let N = S.length;

    for(let i = 0; i < N; i++ ){
        if(S[i] === "X"){
            count++;
            i += 2;
        }
    }
    return count;
}


console.log(potholePatch("XXXX"));
