#include <gtest/gtest.h>
#include "NOTAM.h"
using namespace std;

// Testing Function
TEST(NOTAMTest, SortById) {
    vector<NOTAM> notams = {
        NOTAM("NOTAM_1_68010722", "A", "A1677/23", "N", "2023-03-30T08:14:00.000Z", "KZLA", "QLXAS", "I", "NBO", "A", "000", "999", "LAX", "2023-03-30T08:07:00.000Z", "2023-03-30T09:00:00.000Z", "LAX TWY D CL LGT BTN TWY P AND TWY D10 U/S", "INTL", "KLAX", "2023-03-30T08:15:00.000Z", "KLAX"),
        NOTAM("NOTAM_1_67308205", "A", "A0639/23", "N", "2023-02-03T17:25:00.000Z", "KZLA", "QPICH", "I", "NBO", "A", "000", "999", "LAX", "2023-02-03T17:24:00.000Z", "2023-05-10T17:24:00.000Z", "LAX IAP LOS ANGELES INTL, LOS ANGELES, CA...", "INTL", "KLAX", "2023-02-03T17:26:00.000Z", "KLAX"),
        NOTAM("NOTAM_1_67308206", "A", "A0640/23", "N", "2023-02-03T17:25:00.000Z", "KZLA", "QPICH", "I", "NBO", "A", "000", "999", "LAX", "2023-02-03T17:24:00.000Z", "2023-05-10T17:24:00.000Z", "LAX IAP LOS ANGELES INTL, LOS ANGELES, CA...", "INTL", "KLAX", "2023-02-03T17:26:00.000Z", "KLAX")
    };

    // class the sortBYID function on the NOTAM class
    NOTAM::sortById(notams);

    // Expected output to be compared against next
    vector<string> expectedIds = {
        "NOTAM_1_67308205",
        "NOTAM_1_67308206",
        "NOTAM_1_68010722"
    };
    // checks for the matching ids in order.
    for (size_t i = 0; i < notams.size(); ++i) {
        EXPECT_EQ(expectedIds[i], notams[i].getId());
    }
}

int main(int argc, char **argv) {
    // Script to run the test function
    ::testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}