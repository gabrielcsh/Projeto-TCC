import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.*;
 
public class ReadFrequency {
	
    public List<String[]> getFrequencia() {
        
        List<String[]> texto = new ArrayList();    
        List<Double> frequencias = new ArrayList();    
        String arquivoCSV = "frequencias.csv";
        BufferedReader br = null;
        String linha = " ";
        String csvDivisor = ",";
        int i;
        
        try {
            br = new BufferedReader(new FileReader(arquivoCSV));
            while ((linha = br.readLine()) != null) {
                texto.add(linha.split(csvDivisor));
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
        }
        return texto;
    }
}
