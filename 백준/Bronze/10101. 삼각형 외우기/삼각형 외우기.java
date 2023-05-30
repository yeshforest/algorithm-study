import java.util.*;
class Main {
  public static void main(String[] args) {

    int sum=0;
    int[] arr=new int[3];
   Scanner scanner=new Scanner(System.in);
    for(int i=0;i<3;i++){
      arr[i]=scanner.nextInt();
      sum+=arr[i];
    }
    if(sum!=180){System.out.println("Error");
                return;}
    if(arr[0]==60&&arr[1]==60&&arr[2]==60){System.out.println("Equilateral");return;}
    else if(arr[0]==arr[1]||arr[1]==arr[2]||arr[0]==arr[2]){
      System.out.println("Isosceles");
    }else{
      System.out.println("Scalene");
    }
    
    

    
    

    
    
  }
}
  