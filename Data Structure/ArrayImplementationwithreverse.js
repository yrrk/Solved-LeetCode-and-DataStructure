class MyArray{
    constructor(){
        this.length=0;
        this.data={};
    }
    
    get(index){
        return this.data[index]
    }
    
    push(item){
        this.data[this.length]=item
        this.length++
        return this.length
    }
    
    pop(){
        delete this.data[this.length-1]
        this.length--
    }
    delete(index){
        for(let i=index;i<this.length-1;i++){
            this.data[i]=this.data[i+1]
        }
        this.pop()
    }
    reverse(){
        let sampledata=this.data
        let samplelength=this.length
        this.data={}
        this.length=0
        for(let i=samplelength-1;i>=0;i--){
            this.push(sampledata[i])
        }
    }
}


inputstring="Yaksh is a good boy"
splittedstring=inputstring.split("")
A= new MyArray()
for(let i=0;i<splittedstring.length;i++){
    A.push(splittedstring[i])
}
console.log(A)
A.reverse()
console.log(A)



