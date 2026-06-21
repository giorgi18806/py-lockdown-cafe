class VaccineError(Exception):
    def __str__(self) -> str:
        return "Visitor should be vaccinated"


class OutdatedVaccineError(VaccineError):
    def __str__(self) -> str:
        return "Vaccination is out of date"


class NotVaccinatedError(VaccineError):
    def __str__(self) -> str:
        return "Visitor should be vaccinated"


class NotWearingMaskError(Exception):
    def __str__(self) -> str:
        return "Visitor should wear a mask"
