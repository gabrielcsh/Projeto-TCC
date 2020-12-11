import java.util.*;

public class Main {
	public static void main(String [] args){
		int i;
		ReadFrequency frq = new ReadFrequency();
		//List<Object> frequencias = (frq.getFrequencia());	

		NoteFrequency audio1 = new NoteFrequency(frq.getFrequencia());
	}
}
