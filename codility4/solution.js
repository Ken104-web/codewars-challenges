// def solution(K, A):
//         N = len(A)
//         count = 0
//         for i in range(N):
//             minimum=A[i]
//             maximum=A[i]
//             for x in range(i, N):
//                maximum = max(maximum, A[x])
//                minimum = min(minimum, A[x])
//                if maximum - minimum <= K:
//                 count += 1
//         return count

function solution(K, A) {
    let N = A.length;
    let count = 0;

    for (let i = 0; i < N; i++) {
        let min = A[i];
        let max = A[i];

        for (let q = i; q < N; q++) {
            max = Math.max(max, A[q]);
            min = Math.min(min, A[q]);

            if (max - min <= K) {
                count += 1;
            }
        }
    }

    return count;
}