import java.util.*;
class Main {

  public static int[][] img;
  public static StringBuilder sb = new StringBuilder();
  
  public static void main(String[] args) {

    Scanner scanner = new Scanner(System.in);
    int n = scanner.nextInt();
    img=new int[n][n];

    for(int i=0;i<n;i++){
      String str=scanner.next();

      for(int j=0;j<n;j++){
        img[i][j]=str.charAt(j)-'0';//숫자로 저장
      }
    }
    QuadTree(0,0,n);
    System.out.println(sb);

    
    

    
    
  }

  public static void QuadTree(int x,int y,int size){
    if(isSame(x,y,size)){
        sb.append(img[x][y]);
        return;
    }

    int newSize=size/2;

    sb.append('(');
    QuadTree(x, y, newSize);
    QuadTree(x, y+newSize, newSize);
    QuadTree(x+newSize, y, newSize);
    QuadTree(x+newSize, y+newSize, newSize);

    sb.append(')');//해당 단계의 순회가 끝나면 ) 추가
    
  
  }

  public static boolean isSame(int x, int y, int size) {
		int value = img[x][y];
		
		for(int i = x; i < x + size; i++) {
			for(int j = y; j < y + size; j++) {
				if(value != img[i][j]) {
					return false;
				}
			}
		}
		return true;
	}
}