package org.jcm.alloyutils;

import java.util.HashMap;
import java.util.Map;


public class GenerateAlloyOutput {
	
	protected static AlloyConnector m_ac = new AlloyConnector();
	private static boolean m_debug = true;
	protected static HashMap<String, String> m_structures = new HashMap<String, String>();
	

	public GenerateAlloyOutput() {
		// TODO Auto-generated constructor stub
				

	}

	

	public static void exportConfigurations(String filepath){
			for (Map.Entry<String, String> e: m_structures.entrySet()){
				TextFileHandler fhdata = new TextFileHandler(filepath+"/"+e.getKey()+".json");
				fhdata.exportFile(e.getValue());
			}
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		if (args.length<3) {
			System.out.println("Usage: GenerateAlloyOutput [input file] [export path] [max solutions]");
			System.exit(0);
		}
		
		//String modelFile =  "models/model.als";
		String modelFile = args[0];  // INPUT FILE
		String exportPath = args[1];
		int maxSols = Integer.parseInt(args[2]); // MAXIMUM NUMBER OF SOLUTIONS
		
		
		
		m_ac.setMaxSolutions(maxSols);  
		m_ac.generateSolutions(modelFile);
		
		for (int i=0; i<m_ac.getSolutions().size();i++){
			String strSolId = AlloyConnector.SOLUTION_STRING+String.valueOf(i);
			String strSol = m_ac.getSolution(strSolId);
			AlloySolution sol = new AlloySolution();
			sol.loadFromString(strSol);
			m_structures.put(strSolId, sol.toJSON(strSolId));
			
			if (m_debug)
				System.out.println("\n\n\n SOLUTION "+String.valueOf(i)+" ----------------------\n\n\n" + m_structures.get(strSolId));
		}
		
		//exportConfigurations("models/ALLOY"); // PATH FOR OUTPUT FILES
		exportConfigurations(exportPath); // PATH FOR OUTPUT FILES
		
		
	}

}
