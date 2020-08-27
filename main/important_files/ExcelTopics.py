from enum import Enum


class Topics(Enum):
    ScouterName = "Scouter Name"
    TeamNumber = "Team Number"
    MatchNumber = "Match Number (pr02/q01/p04)"
    MovedFromSectorLine = "Moved from Sector Line?"
    A_PowerCellsScoredInlow = "(A) Power Cells scored in low"
    A_PowerCellsMissedInLow = "(A) Power Cells missed in low"
    A_PowerCellsScoredInHigh_2_Hexagon = "(A) Power Cells scored in High - 2 (Hexagon)"
    A_PowerCellsScoredInHigh_3_Circle = "(A) Power Cells scored in High - 3 (Circle)"
    A_PowerCellsMissedInHigh = "(A) Power Cells missed in High"
