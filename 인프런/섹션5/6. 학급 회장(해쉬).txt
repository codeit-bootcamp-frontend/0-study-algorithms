<html>
    <head>
        <meta charset="UTF-8">
        <title>출력결과</title>
    </head>
    <body>
        <script>
            function solution(s){  
                let answer;
                let sH = new Map();
                for(let x of s){
                    if(sH.has(x)) sH.set(x, sH.get(x)+1);
                    else sH.set(x, 1);
                }
                let max=Number.MIN_SAFE_INTEGER;
                for(let [key, val] of sH){
                    if(val>max){
                        max=val;
                        answer=key;
                    }
                }
                return answer;
            }

            let str="BACBACCACCBDEDE";
            console.log(solution(str));
        </script>
    </body>
</html>