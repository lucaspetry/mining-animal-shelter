import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;

public class PreProcess {
	
	/**
	 * @param args
	 */
	public static void main(String[] args) {

		String trainIN = "/home/lucas/git/mining-animal-shelter/data/train.csv";
		String trainOUT = "/home/lucas/git/mining-animal-shelter/data/trainProcessed_1.csv";
		
		String testIN = "/home/lucas/git/mining-animal-shelter/data/test.csv";
		String testOUT = "/home/lucas/git/mining-animal-shelter/data/testProcessed_1.csv";
		
		preProcessTrainSet(trainIN, trainOUT);
		preProcessTestSet(testIN, testOUT);
	}

	public static void preProcessTrainSet(String fileIN, String fileOUT) {		
        BufferedReader br = null;
        BufferedWriter bw = null;
        String line = "";
        String cvsSplitBy = ",";

        try {

            br = new BufferedReader(new FileReader(fileIN));
            bw = new BufferedWriter(new FileWriter(fileOUT));
            
            br.readLine(); // Header
            bw.write("hasName,animalType,sex,isIntact," +
            		"monthsOld,breed1,breed2,isMix,color1,color2,outcome\n"); // Write Header
            
            while ((line = br.readLine()) != null) {
            	// AnimalID,Name,DateTime,OutcomeType,OutcomeSubtype,AnimalType,
            	// SexuponOutcome,AgeuponOutcome,Breed,Color
            	
            	/**
            	 * Novos Dados:
            	 * boolean hasName
            	 * String animalType
            	 * char sex
            	 * boolean isIntact 
            	 * int ageInMonths
            	 * String breed1
            	 * String breed2
            	 * boolean isMix
            	 * String color1
            	 * String color2
            	 * String outcome
            	 * String outcome2
            	 */
            	
                String[] fields = line.split(cvsSplitBy);
                String outLine = "";
                
                // Transformar essas 5 semanas em 1 mês
                if(fields[7].equals("5 weeks"))
                	fields[7] = "1 month";
                
                if(fields[1].equals("")) // Nome vazio
                	outLine += "false,";
                else
                	outLine += "true,";
                
                outLine += fields[5] + ",";
                String sex = "";
                String isIntact = "";
                
                if(!fields[6].equals("Unknown") && fields[6] != null
                	&& !fields[6].equals("")) {
                	sex = fields[6].split(" ")[1].equals("Female") ? "F," : "M,";
                	isIntact = fields[6].split(" ")[0].equals("Intact") ? "true," : "false,";
                } else {
                	sex = ",";
                	isIntact = ",";
                }
                
                outLine += sex + isIntact;
                
                try {
                	int age = Integer.parseInt(fields[7].split(" ")[0]);

                    String sufAge = fields[7].split(" ")[1];
                    
                    if(sufAge.contains("day"))
                    	age = 0;
                    else if(sufAge.contains("week"))
                    	age = 0;
                    else if(sufAge.contains("year"))
                    	age *= 12;
                    
                    outLine += age + ",";
                } catch(Exception e) {
                	outLine += ",";
                }
                
                String[] breeds = fields[8].split("/");
                String[] colors = fields[9].split("/");
                
                String isMix = "false";
                
                if(breeds[0].contains(" Mix")) {
                	isMix = "true";
                	breeds[0] = breeds[0].substring(0, breeds[0].indexOf(" Mix"));
                }
                
                if(breeds.length > 1 && breeds[1].contains(" Mix")) {
                	isMix = "true";
                	breeds[1] = breeds[1].substring(0, breeds[1].indexOf(" Mix"));
                }
                
                outLine += breeds[0] + "," + (breeds.length > 1 ? breeds[1] : "") + "," + isMix + ",";
                outLine += colors[0] + "," + (colors.length > 1 ? colors[1] : "") + ",";
                outLine += fields[3]; // + "," + fields[4];
                
                bw.write(outLine + "\n");
            }

        } catch (FileNotFoundException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        } finally {
            if (br != null) {
                try {
                    br.close();
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }

            if (bw != null) {
                try {
                    bw.close();
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
        }
	}

	public static void preProcessTestSet(String fileIN, String fileOUT) {		
        BufferedReader br = null;
        BufferedWriter bw = null;
        String line = "";
        String cvsSplitBy = ",";

        try {

            br = new BufferedReader(new FileReader(fileIN));
            bw = new BufferedWriter(new FileWriter(fileOUT));
            
            br.readLine(); // Header
            bw.write("hasName,animalType,sex,isIntact," +
            		"monthsOld,breed1,breed2,isMix,color1,color2\n"); // Write Header
            
            while ((line = br.readLine()) != null) {
            	// AnimalID,Name,DateTime,AnimalType,
            	// SexuponOutcome,AgeuponOutcome,Breed,Color
            	
            	/**
            	 * Novos Dados:
            	 * boolean hasName
            	 * String animalType
            	 * char sex
            	 * boolean isIntact 
            	 * int ageInMonths
            	 * String breed1
            	 * String breed2
            	 * boolean isMix
            	 * String color1
            	 * String color2
            	 */
            	
                String[] fields = line.split(cvsSplitBy);
                String outLine = "";
                
                // Transformar essas 5 semanas em 1 mês
                if(fields[5].equals("5 weeks"))
                	fields[5] = "1 month";
                
                if(fields[1].equals("")) // Nome vazio
                	outLine += "false,";
                else
                	outLine += "true,";
                
                outLine += fields[3] + ",";
                String sex = "";
                String isIntact = "";
                
                if(!fields[4].equals("Unknown") && fields[4] != null
                	&& !fields[4].equals("")) {
                	sex = fields[4].split(" ")[1].equals("Female") ? "F," : "M,";
                	isIntact = fields[4].split(" ")[0].equals("Intact") ? "true," : "false,";
                } else {
                	sex = ",";
                	isIntact = ",";
                }
                
                outLine += sex + isIntact;
                
                try {
                	int age = Integer.parseInt(fields[5].split(" ")[0]);

                    String sufAge = fields[5].split(" ")[1];
                    
                    if(sufAge.contains("day"))
                    	age = 0;
                    else if(sufAge.contains("week"))
                    	age = 0;
                    else if(sufAge.contains("year"))
                    	age *= 12;
                    
                    outLine += age + ",";
                } catch(Exception e) {
                	outLine += ",";
                }
                
                String[] breeds = fields[6].split("/");
                String[] colors = fields[7].split("/");
                
                String isMix = "false";
                
                if(breeds[0].contains(" Mix")) {
                	isMix = "true";
                	breeds[0] = breeds[0].substring(0, breeds[0].indexOf(" Mix"));
                }
                
                if(breeds.length > 1 && breeds[1].contains(" Mix")) {
                	isMix = "true";
                	breeds[1] = breeds[1].substring(0, breeds[1].indexOf(" Mix"));
                }
                
                outLine += breeds[0] + "," + (breeds.length > 1 ? breeds[1] : "") + "," + isMix + ",";
                outLine += colors[0] + (colors.length > 1 ? "," + colors[1] : "");
                
                bw.write(outLine + "\n");
            }

        } catch (FileNotFoundException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        } finally {
            if (br != null) {
                try {
                    br.close();
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
            
            if (bw != null) {
                try {
                    bw.close();
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
        }
	}

}
