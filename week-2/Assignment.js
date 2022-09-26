function calculate(min, max, step){
    let count = Math.floor((max - min) / step);
    let answer = min*(count + 1) + ((count) * (count + 1) / 2) * step;
    console.log(answer);
    }
    calculate(1, 3, 1); // 你的程式要能夠計算 1+2+3，最後印出 6
    calculate(4, 8, 2); // 你的程式要能夠計算 4+6+8，最後印出 18
    calculate(-1, 2, 2); // 你的程式要能夠計算 -1+1，最後印出 0

function avg(data){
    let total = 0;
    data.employees.map((val)=>{
        val.manager?total+=val.salary:void 0;
    });
    console.log(total);
    }
    avg({
    "employees":[
    {
    "name":"John",
    "salary":30000,
    "manager":false
    },
    {
    "name":"Bob",
    "salary":60000,
    "manager":true
    },
    {
    "name":"Jenny",
    "salary":50000,
    "manager":false
    },
    {
    "name":"Tony",
    "salary":40000,
    "manager":false
    }
    ]
    }); // 呼叫 avg 函式

function func(a){
    return (b , c)=>console.log(a + b*c);
    }
    func(2)(3, 4); // 你補完的函式能印出 2+(3*4) 的結果 14
    func(5)(1, -5); // 你補完的函式能印出 5+(1*-5) 的結果 0
    func(-3)(2, 9); // 你補完的函式能印出 -3+(2*9) 的結果 15
    // 一般形式為 func(a)(b, c) 要印出 a+(b*c) 的結果

function maxProduct(nums){
    let result = [];
    nums.map((i, i_index)=>{
        nums.map((j, j_index)=>{
            if(i_index === j_index) return;
            result.push(i*j);
        });
    });
    console.log(Math.max(...result));
    return Math.max(...result);
    }
    maxProduct([5, 20, 2, 6]) // 得到 120
    maxProduct([10, -20, 0, 3]) // 得到 30
    maxProduct([10, -20, 0, -3]) // 得到 60
    maxProduct([-1, 2]) // 得到 -2
    maxProduct([-1, 0, 2]) // 得到 0 或 -0
    maxProduct([5, -1, -2, 0]) // 得到 2
    maxProduct([-5, -2]) // 得到 10

function twoSum(nums, target){
    let newNums =  nums.map((val)=>val-target);
    let result = [];
    newNums.map((i, i_index)=>{
        if(result.length===2) return;
        nums.map((j, j_index)=>{
            if(i+j===0){
                result.push(i_index);
                result.push(j_index);
            };
        });
    });
    return result;
    }
    let result=twoSum([0, 11, 7, 15], 15);
    console.log(result); // show [0, 2] because nums[0]+nums[2] is 9

function maxZeros(nums){
    // 請用你的程式補完這個函式的區塊
    let array = [];
    let counter = 0;
    nums.map((val)=>{
        array.push(0);
        val===0?array[counter]+=1:counter++;
    });
    return Math.max(...array);
    }
    maxZeros([0, 1, 0, 0]); // 得到 2
    maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0]); // 得到 4
    maxZeros([1, 1, 1, 1, 1]); // 得到 0
    maxZeros([0, 0, 0, 1, 1]) // 得到 3