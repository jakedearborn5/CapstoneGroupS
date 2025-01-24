#include "NOTAM.h"
using namespace std;

/*
    Imports the NOTAM Class. Implementations of the NOTAM class methods.
*/
// Constructor
NOTAM::NOTAM(const string& id, const string& series, const string& number, const string& type,
             const string& issued, const string& affectedFIR, const string& selectionCode,
             const string& traffic, const string& purpose, const string& scope, const string& minimumFL,
             const string& maximumFL, const string& location, const string& effectiveStart,
             const string& effectiveEnd, const string& text, const string& classification,
             const string& accountId, const string& lastUpdated, const string& icaoLocation)
    : id(id), series(series), number(number), type(type), issued(issued), affectedFIR(affectedFIR),
      selectionCode(selectionCode), traffic(traffic), purpose(purpose), scope(scope), minimumFL(minimumFL),
      maximumFL(maximumFL), location(location), effectiveStart(effectiveStart), effectiveEnd(effectiveEnd),
      text(text), classification(classification), accountId(accountId), lastUpdated(lastUpdated),
      icaoLocation(icaoLocation) {}

// returns id
string NOTAM::getId() const {
    return id;
}

// print Notam Information (for now it is just ID)
string NOTAM::getInfo() const {
    return "ID: " + id;
}

// Sort a vector of NOTAMS by ID
void NOTAM::sortById(std::vector<NOTAM>& notams) {
    sort(notams.begin(), notams.end(), [](const NOTAM& a, const NOTAM& b) {
        return a.getId() < b.getId();
    });
}
