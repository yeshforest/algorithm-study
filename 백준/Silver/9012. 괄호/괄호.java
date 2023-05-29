import java.util.*;
class Main {


 
  public static void main(String[] args) {

    Scanner scanner = new Scanner(System.in);
    int n = scanner.nextInt();
   

    for(int i=0;i<n;i++){
        System.out.println(checkStack(scanner.next()));
       
    }
    

    
    

    
    
  }

  public static String checkStack(String str){
Stack<Character> stack= new Stack<>();
     
    
      for(int j=0;j<str.length();j++){
        char c = str.charAt(j);
        
        if(c=='('){//다음이 왼쪽괄호이면
          stack.push(c);
        }else if(stack.empty()){
           return "NO";
        }else{
          stack.pop();
        }
      }

      if(stack.empty()){
       return "YES";
      }else{
        return "NO";
      }

          
  }

}