function Solution(A){
    let maxInValue = A[0]
    let minInValue = A[0]

    for(let i=0; i.arrayLength; i++){
        if (i > maxInValue){
            maxInValue = i;
        } else if(i < minInValue){
            minInValue = i;
        } else if(length(A) === 0){
            return 0
        }
    amplitude = maxInValue - minInValue

    }
    return amplitude
}

A = [10, 2, 44, 15, 39, 20]
// console.log(A);