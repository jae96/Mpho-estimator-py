##Challenge_1_2_3

import math


def esimator(data):

    reportedCases = data["reportedCases"]

    impact = {"currentlyInfected": reportedCases*10}
    severeImpact = {"currentlyInfected": reportedCases*50}

    # Calculate infectionsByRequestedTime by finding the find the period type and timeToElapse and calculate factor
    timeToElapse = data["timeToElapse"]
    periodType = data["periodType"]
    if periodType == "days":
        finalTimeToElapse = timeToElapse
    if periodType == "weeks":
        finalTimeToElapse = timeToElapse * 7  # There are seven days in a week
    if periodType == "weeks":
        finalTimeToElapse = timeToElapse * 30  # Assuming 30 days in a month

    factor = math.floor(finalTimeToElapse/3)

    impact["infectionsByRequestedTime"] = (reportedCases*10)*(2**factor)
    severeImpact["infectionsByRequestedTime"] = (reportedCases * 50) * (2 ** factor)

    impact["severeCasesByRequestedTime"] = (((reportedCases*10)*(2**factor))*0.15)
    severeImpact["severeCasesByRequestedTime"] = (((reportedCases * 50) * (2 ** factor)) * 0.15)

    totalHospitalBeds = data["totalHospitalBeds"]

    impact["hospitalBedsByRequestedTime"] = math.ceil((0.35*totalHospitalBeds)) - impact[
        "severeCasesByRequestedTime"]
    severeImpact["hospitalBedsByRequestedTime"] = math.ceil((0.35*totalHospitalBeds)) - severeImpact[
        "severeCasesByRequestedTime"]

    impact["casesForICUByRequestedTime"] = (((reportedCases*10)*(2**factor))*0.05)
    severeImpact["casesForICUByRequestedTime"] = (((reportedCases*50)*(2**factor))*0.05)

    impact["casesForVentilatorsByRequestedTime"] = (((reportedCases*10)*(2**factor))*0.02)
    severeImpact["casesForVentilatorsByRequestedTime"] = (((reportedCases*50)*(2**factor))*0.02)

    impact["dollarsInFlight"] = round(((reportedCases*10)*(2**factor)*0.73*4*38), 2)
    severeImpact["dollarsInFlight"] = ((reportedCases*50)*(2**factor)*0.73*4*38)

    estimate = {"impact": impact, "severeImpact": severeImpact}
    return estimate


data = {"region": {
    "name": "Africa",
    "avgAge": 19.7,
    "avgDailyIncomeInUSD": 4,
    "avgDailyIncomePopulation": 0.73
}, "periodType": "days",
    "timeToElapse": 38,
    "reportedCases": 2747,
    "population": 92931687,
    "totalHospitalBeds": 678874}


print(esimator(data))

