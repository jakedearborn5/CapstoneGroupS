#ifndef NOTAM_H
#define NOTAM_H

#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

/*
    NOTAM class Definition.
 */
class NOTAM {
private:
    string id;
    string series;
    string number;
    string type;
    string issued;
    string affectedFIR;
    string selectionCode;
    string traffic;
    string purpose;
    string scope;
    string minimumFL;
    string maximumFL;
    string location;
    string effectiveStart;
    string effectiveEnd;
    string text;
    string classification;
    string accountId;
    string lastUpdated;
    string icaoLocation;

public:
    // Constructor
    NOTAM(const string& id, const string& series, const string& number, const string& type,
          const string& issued, const string& affectedFIR, const string& selectionCode,
          const string& traffic, const string& purpose, const string& scope, const string& minimumFL,
          const string& maximumFL, const string& location, const string& effectiveStart,
          const string& effectiveEnd, const string& text, const string& classification,
          const string& accountId, const string& lastUpdated, const string& icaoLocation);

    // Getter for ID
    string getId() const;

    // Helper method to get NOTAM info: returns NOTAM id only.
    string getInfo() const;

    // Static method to sort a vector of NOTAMs by ID
    static void sortById(vector<NOTAM>& notams);
};

#endif
