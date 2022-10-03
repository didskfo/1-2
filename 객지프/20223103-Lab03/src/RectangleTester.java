import java.awt.Rectangle;

public class RectangleTester
{
	public static void main(String[] args)
    {
		Rectangle r1 = new Rectangle(0, 0, 100, 50);
        /* Your code goes here */
		Rectangle r2 = r1;
		r2.grow(10, 20);
		
		System.out.println(r1); // Rectangle 객체 r1 에 대한 정보 출력
        /* and here */
		System.out.println(r2);
    }
	
}