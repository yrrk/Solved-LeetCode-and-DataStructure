function mergerlist(array1,array2){
    for(let i=0;i<array2.length;i++){
        for(let j=0;j<array1.length;j++){
            if(array2[i]<array1[j]){
                array1.splice(j,0,array2[i])
                break;
            }
        }
    }
    return array1
}
a=[1,3,7,10,12]
b=[4,5,6,8,9]

console.log(mergerlist(a,b))