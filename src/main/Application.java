package main;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Scanner;

public class Application {	
	public static void main(String[] args) {
		String output = "#separator:semicolon\n#html:true\n"; 
		
	    try {
	    	File myObj = new File("../input.txt");
	        Scanner myReader = new Scanner(myObj);
			String data = "";
			String question = "";
			String answer = "";
	        while (myReader.hasNextLine()) {
	        	data = myReader.nextLine();
				if(data.startsWith("    - ")){
					if(data.startsWith("    - https")){
						answer += "<li><img src=\"\"" + data.substring(6) + "\"\"></li>";
					} else{
						answer += "<li>" + data.substring(6) + "</li>";
					}
				} else if(data.startsWith("- ")){
					if(question != "" && answer != ""){
						output += question + ";\"" + answer + "\"\n";
					}
					question = data.substring(2);
					answer = "";
				}
	        }
			output += question + ";" + answer + "\n";
			question = data;
			answer = "";
	        myReader.close();
	    } catch (FileNotFoundException e) {
	        System.out.println("An error occurred.");
	        e.printStackTrace();
	    }
	    
	    BufferedWriter writer;
		try {
			writer = new BufferedWriter(new FileWriter("../output.txt"));
			writer.write(output);
			writer.close();
		} catch (IOException e) {
			e.printStackTrace();
		}
	}
}



















