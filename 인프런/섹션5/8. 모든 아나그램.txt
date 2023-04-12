<html>
    <head>
        <meta charset="UTF-8">
        <title>출력결과</title>
    </head>
    <body>
        <script>
            function compareMaps(map1, map2){
                if(map1.size!==map2.size) return false;
                for(let [key, val] of map1){
                    if(!map2.has(key) || map2.get(key)!==val) return false;
                }
                return true;
            }
            function solution(s, t){
                let answer=0;
                let tH = new Map();
                let sH = new Map();
                for(let x of t){
                    if(tH.has(x)) tH.set(x, tH.get(x)+1);
                    else tH.set(x, 1);
                }
                let len=t.length-1;
                for(let i=0; i<len; i++){
                    if(sH.has(s[i])) sH.set(s[i], sH.get(s[i])+1);
                    else sH.set(s[i], 1);
                }
                let lt=0;
                for(let rt=len; rt<s.length; rt++){
                    if(sH.has(s[rt])) sH.set(s[rt], sH.get(s[rt])+1);
                    else sH.set(s[rt], 1);
                    if(compareMaps(sH, tH)) answer++;
                    sH.set(s[lt], sH.get(s[lt])-1);
                    if(sH.get(s[lt])===0) sH.delete(s[lt]);
                    lt++;
                }
                return answer;
            }
            
            let a="bacaAacba";
            let b="abc";
            console.log(solution(a, b));
        </script>
    </body>
</html>