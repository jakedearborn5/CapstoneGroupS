import com.fasterxml.jackson.annotation.JsonProperty;
public class NOTAM {
	
	private String id;
	private String series;
	private String number;
	private String type;
	private String issued;
	private String affectedFIR;
	private String selectionCode;
	private String traffic;
	private String purpose;
	private String scope;
	private String minimumFL;
	private String maximumFL;
	private String location;
	private String effectiveStart;
	private String effectiveEnd;
	private String text;
	private String classification;
	private String accountId;
	private String lastUpdated;
	private String icaoLocation;
	private String coordinates;
	private String radius;
	
	// Constructors: 
	public NOTAM(
	        @JsonProperty("id") String id,
	        @JsonProperty("series") String series,
	        @JsonProperty("number") String number,
	        @JsonProperty("type") String type,
	        @JsonProperty("issued") String issued,
	        @JsonProperty("affectedFIR") String affectedFIR,
	        @JsonProperty("selectionCode") String selectionCode,
	        @JsonProperty("traffic") String traffic,
	        @JsonProperty("purpose") String purpose,
	        @JsonProperty("scope") String scope,
	        @JsonProperty("minimumFL") String minimumFL,
	        @JsonProperty("maximumFL") String maximumFL,
	        @JsonProperty("location") String location,
	        @JsonProperty("effectiveStart") String effectiveStart,
	        @JsonProperty("effectiveEnd") String effectiveEnd,
	        @JsonProperty("text") String text,
	        @JsonProperty("classification") String classification,
	        @JsonProperty("accountId") String accountId,
	        @JsonProperty("lastUpdated") String lastUpdated,
	        @JsonProperty("icaoLocation") String icaoLocation,
	        @JsonProperty("coordinates") String coordinates,
	        @JsonProperty("radius") String radius
	    ) {
	        this.id = id;
	        this.series = series;
	        this.number = number;
	        this.type = type;
	        this.issued = issued;
	        this.affectedFIR = affectedFIR;
	        this.selectionCode = selectionCode;
	        this.traffic = traffic;
	        this.purpose = purpose;
	        this.scope = scope;
	        this.minimumFL = minimumFL;
	        this.maximumFL = maximumFL;
	        this.location = location;
	        this.effectiveStart = effectiveStart;
	        this.effectiveEnd = effectiveEnd;
	        this.text = text;
	        this.classification = classification;
	        this.accountId = accountId;
	        this.lastUpdated = lastUpdated;
	        this.icaoLocation = icaoLocation;
	        this.coordinates = coordinates;
	        this.radius = radius;
	    }
	
	// Getters for testing purposes:
	public String getId() {
		return id;
	}
	
	public String getType() {
		return type;
	}
	
	public String getLocation() {
		return location;
	}
	
	// toString for necessary testing:
	public String toString() {
		return "ID: " + id + "; Type: " + type + "; Location: " + location;
	}
	
}
