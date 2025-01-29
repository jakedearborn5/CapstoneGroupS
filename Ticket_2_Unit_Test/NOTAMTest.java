import static org.junit.jupiter.api.Assertions.*;
import com.fasterxml.jackson.databind.ObjectMapper;
import org.junit.jupiter.api.Test;

class NOTAMTest2 {

	@Test
	void testNOTAM() {
		
		// JSON format for NotAM Objects
		
		String testNotAM1str = "{\r\n"
				+ "    \"id\": \"NOTAM_1_67308205\",\r\n"
				+ "    \"series\": \"A\",\r\n"
				+ "    \"number\": \"A0639/23\",\r\n"
				+ "    \"type\": \"N\",\r\n"
				+ "    \"issued\": \"2023-02-03T17:25:00.000Z\",\r\n"
				+ "    \"affectedFIR\": \"KZLA\",\r\n"
				+ "    \"selectionCode\": \"QPICH\",\r\n"
				+ "    \"traffic\": \"I\",\r\n"
				+ "    \"purpose\": \"NBO\",\r\n"
				+ "    \"scope\": \"A\",\r\n"
				+ "    \"minimumFL\": \"000\",\r\n"
				+ "    \"maximumFL\": \"999\",\r\n"
				+ "    \"location\": \"LAX\",\r\n"
				+ "    \"effectiveStart\": \"2023-02-03T17:24:00.000Z\",\r\n"
				+ "    \"effectiveEnd\": \"2023-05-10T17:24:00.000Z\",\r\n"
				+ "    \"text\": \"LAX IAP LOS ANGELES INTL, LOS ANGELES, CA.\\\\nRNAV (RNP) Z RWY 24R, AMDT 1D...\\\\nRNP 0.15 DA 531/ HAT 409 ALL CATS, VISIBILITY ALL CATS RVR 5000.\\\\nRNP 0.30 DA 593/HAT 471 ALL CATS. TEMPORARY CRANE 248 MSL 5792FT E\\\\nOF RWY 24R (2021-AWP-523-OE), TEMPORARY CRANES UP TO 302 MSL\\\\nBEGINNING 1.2NM E OF RWY 24R (2022-AWP-15384/15385/15386/15387-OE).\",\r\n"
				+ "    \"classification\": \"INTL\",\r\n"
				+ "    \"accountId\": \"KLAX\",\r\n"
				+ "    \"lastUpdated\": \"2023-02-03T17:26:00.000Z\",\r\n"
				+ "    \"icaoLocation\": \"KLAX\"\r\n"
				+ "  }";
		
		String testNotAM2str = " {\r\n"
				+ "    \"id\": \"NOTAM_1_67308206\",\r\n"
				+ "    \"series\": \"A\",\r\n"
				+ "    \"number\": \"A0640/23\",\r\n"
				+ "    \"type\": \"N\",\r\n"
				+ "    \"issued\": \"2023-02-03T17:25:00.000Z\",\r\n"
				+ "    \"affectedFIR\": \"KZLA\",\r\n"
				+ "    \"selectionCode\": \"QPICH\",\r\n"
				+ "    \"traffic\": \"I\",\r\n"
				+ "    \"purpose\": \"NBO\",\r\n"
				+ "    \"scope\": \"A\",\r\n"
				+ "    \"minimumFL\": \"000\",\r\n"
				+ "    \"maximumFL\": \"999\",\r\n"
				+ "    \"location\": \"LAX\",\r\n"
				+ "    \"effectiveStart\": \"2023-02-03T17:24:00.000Z\",\r\n"
				+ "    \"effectiveEnd\": \"2023-05-10T17:24:00.000Z\",\r\n"
				+ "    \"text\": \"LAX IAP LOS ANGELES INTL, LOS ANGELES, CA.\\\\nRNAV (RNP) Z RWY 24L, AMDT 2B...\\\\nRNP 0.30 DA 620/ HAT 497 ALL CATS. TEMPORARY CRANES UP TO 250 MSL\\\\nBEGINNING 1.1NM E OF RWY 24L (2022-AWP-299/300/301-NRA), TEMPORARY\\\\nCRANES UP TO 302 MSL BEGINNING 1.1NM E OF RWY 24L\\\\n(2022-AWP-15384/15385/15386/15387-OE).\",\r\n"
				+ "    \"classification\": \"INTL\",\r\n"
				+ "    \"accountId\": \"KLAX\",\r\n"
				+ "    \"lastUpdated\": \"2023-02-03T17:26:00.000Z\",\r\n"
				+ "    \"icaoLocation\": \"KLAX\"\r\n"
				+ "  }";
		
		String testNotAM3str = "{\r\n"
				+ "    \"id\": \"NOTAM_1_68010722\",\r\n"
				+ "    \"series\": \"A\",\r\n"
				+ "    \"number\": \"A1677/23\",\r\n"
				+ "    \"type\": \"N\",\r\n"
				+ "    \"issued\": \"2023-03-30T08:14:00.000Z\",\r\n"
				+ "    \"affectedFIR\": \"KZLA\",\r\n"
				+ "    \"selectionCode\": \"QLXAS\",\r\n"
				+ "    \"minimumFL\": \"000\",\r\n"
				+ "    \"maximumFL\": \"999\",\r\n"
				+ "    \"location\": \"LAX\",\r\n"
				+ "    \"effectiveStart\": \"2023-03-30T08:07:00.000Z\",\r\n"
				+ "    \"effectiveEnd\": \"2023-03-30T09:00:00.000Z\",\r\n"
				+ "    \"text\": \"LAX TWY D CL LGT BTN TWY P AND TWY D10 U/S\",\r\n"
				+ "    \"classification\": \"INTL\",\r\n"
				+ "    \"accountId\": \"KLAX\",\r\n"
				+ "    \"lastUpdated\": \"2023-03-30T08:15:00.000Z\",\r\n"
				+ "    \"icaoLocation\": \"KLAX\",\r\n"
				+ "    \"coordinates\": \"3357N11824W\",\r\n"
				+ "    \"radius\": \"005\"\r\n"
				+ "  }";
		
		// ObjectMapper to handle declaring NotAMs
		ObjectMapper objectMapper = new ObjectMapper();
		
		NOTAM notAM1 = null; 
		NOTAM notAM2 = null; 
		NOTAM notAM3 = null;
		
		// Declare NotAMs
		try{
			notAM1 = objectMapper.readValue(testNotAM1str, NOTAM.class);
		}
		catch (Exception e) {
			e.printStackTrace();
		}
		
		try{
			notAM2 = objectMapper.readValue(testNotAM2str, NOTAM.class);
		}
		catch (Exception e) {
			e.printStackTrace();
		}
		
		try{
			notAM3 = objectMapper.readValue(testNotAM3str, NOTAM.class);
		}
		catch (Exception e) {
			e.printStackTrace();
		}
		
		// Testing correctness using NotAM ID, type, and location for all 3.
		assertEquals("NOTAM_1_67308205", notAM1.getId());
		assertEquals("N", notAM1.getType());
		assertEquals("LAX", notAM1.getLocation());
		
		assertEquals("NOTAM_1_67308206", notAM2.getId());
		assertEquals("N", notAM2.getType());
		assertEquals("LAX", notAM2.getLocation());
		
		assertEquals("NOTAM_1_68010722", notAM3.getId());
		assertEquals("N", notAM3.getType());
		assertEquals("LAX", notAM3.getLocation());
	}

}
