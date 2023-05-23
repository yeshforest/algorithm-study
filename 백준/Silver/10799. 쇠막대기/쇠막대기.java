import java.util.*;
class Main {
  public static void main(String[] args) {
   Scanner sc = new Scanner(System.in);
		String s = sc.next();
    Stack <Character>stack=new Stack<>();
    int ans=0;

    for(int i=0;i<s.length();i++){
      if(s.charAt(i)=='('){
        stack.push('(');
       
      }else{
         stack.pop();
        
         if(s.charAt(i-1)=='('){
          ans+=stack.size();
        }else{// ) 이전에 )인경우 
          ans+=1;
        }
       
      }
    }

 System.out.println(ans);
  

    
    
  }
}