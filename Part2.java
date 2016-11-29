import java.util.Scanner;
import java.io.*;

public class Part2 {
	public static void main(String [] args) {
		String file = "C:/Users/gsala_000/workspace/CPSC 323 Final Project/src/finalv2.txt";
		
		try {
			readData(file);
		} catch(IOException ex) {
			System.out.println("Error");
		}
	}
	
	public static void readData(String fname) throws IOException {
		BufferedReader in = new BufferedReader(new FileReader(fname));
		String text = "", line;
		
		while((line = in.readLine()) != null) {
			System.out.println(line);
			text += line;
			text += "\n";
		}
		
		System.out.println();
		
		if (text.contains("program") && text.contains("var") && text.contains("begin") && text.contains("end.") && text.contains("integer") && text.contains("print") && checkForTerms(text) == true) {
			System.out.println("No errors");
		}
		else if (!text.contains("program")) {
			System.out.println("program is expected");
		}
		else if (!text.contains("var")) {
			System.out.println("var is expected");
		}
		else if (!text.contains("begin")) {
			System.out.println("begin is expected");
		}
		else if (!text.contains("end.")) {
			System.out.println("end. is expected");
		}
		else if (!text.contains("integer")) {
			System.out.println("integer is expected");
		}
		else if (!text.contains("print")) {
			System.out.println("print is expected");
		}
		else if (!text.contains(";")) {
			System.out.println("; is missing");
		}
		
		System.out.println();
		
		in.close();
	}
	
	public boolean isReserved(String word) {
		if (word.equals("program") || word.equals("var") || word.equals("begin") || word.equals("end.") || word.equals("integer") || word.equals("print")) {
			return true;
		}
		else {
			return false;
		}
	}
	
	public static boolean checkForTerms(String text) {
		if (!text.contains("/*") && text.contains("*/")) {
			System.out.println("/* is missing");
			return false;
		}
		else if (text.contains("/*") && !text.contains("*/")) {
			System.out.println("*/ is missing");
			return false;
		}
		else if (!text.contains(",")) {
			System.out.println(", is missing");
			return false;
		}
		else if (!text.contains(".")) {
			System.out.println(". is missing");
			return false;
		}
		else if (!text.contains(")")) {
			System.out.println(") is missing");
			return false;
		}
		else if (!text.contains("(")) {
			System.out.println("( is missing");
			return false;
		}
		else {
			return true;
		}
	}
	public boolean isIdentifier(String text) {
		if (text.contains("var")) {
			return true;
		}
		return false;
	}
}

/*
output:
if there are no errors:
program a2016;
var
a1 , b2a , c , ba12 : integer ;
begin
a1 = 3 ;
b2a = 4 ;
c = 5 ;
print ( c ) ;
ba12 = a1 * ( b2a + 2 * c ) ;
print ( ba12 ) ;
end.

No errors

Example error:
program a2016;
var
a1 , b2a , c , ba12 : integer ;

a1 = 3 ;
b2a = 4 ;
c = 5 ;
print ( c ) ;
ba12 = a1 * ( b2a + 2 * c ) ;
print ( ba12 ) ;
end.

begin is expected

program a2016;
var
a1 , b2a , c , ba12 : integer ;
begin*/
a1 = 3 ;
b2a = 4 ;
c = 5 ;
print ( c ) ;
ba12 = a1 * ( b2a + 2 * c ) ;
print ( ba12 ) ;
end.

'/*' is missing

*/
