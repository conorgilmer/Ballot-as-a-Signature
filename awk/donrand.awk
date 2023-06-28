function shuf(arr,      i, j, n, tmp) {
    n = length(arr)
    for (i=n; i>1; i--) {
        j = int( 1 + rand()*i )
        tmp = arr[i]
        arr[i] = arr[j]
        arr[j] = tmp
    }
}

BEGIN {
    srand()
    for (i=1; i<=n; i++) { arr[i] = i }
    for (k=1; k<=o; k++){
        shuf(arr)
        for (i=1; i<=m; i++) { printf("%d,",arr[i]) }
        printf("\n")
    }
}
