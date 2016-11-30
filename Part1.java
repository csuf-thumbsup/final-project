import java.util.Scanner;
import java.io.*;

public class Part1 {
	public static void main(String [] args) {
		String fname = "C:/Users/gsala_000/workspace/CPSC 323 Final Project/src/finalv1.txt";
		
		try {
			readData(fname);
		} catch(IOException ex) {
			System.out.println("Error");
		}
	}
	
	public static void readData(String fname) throws IOException {
		BufferedReader in = new BufferedReader(new FileReader(fname));
		String file = "C:/Users/gsala_000/workspace/CPSC 323 Final Project/src/finalv2.txt";
		BufferedWriter out = new BufferedWriter(new FileWriter(file));
		
		String text = "";
		String [] lines;
		String line;
		while((line = in.readLine()) != null) {
			line = line.trim();
			if (isComment(line) == true) {
				continue;
			}
			text += line;
			text += "\n";
		}
		
	
		String[] token = text.split("//s+");
	
		for (int i = 0; i < token.length; i++) {
			System.out.println(token[i]);
			out.write(token[i]);
		}
		
		out.close();	
		in.close();
	}
	
	public static boolean isComment(String line) {
		if (line.startsWith("/*")) {
			return true;
		}
		if (line.endsWith("*/")) {
			return true;
		}
		
		return false;
	}
	
	
}
