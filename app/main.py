from __future__ import annotations
from app.cafe import Cafe
from app.errors import VaccineError, NotWearingMaskError, NotVaccinatedError, OutdatedVaccineError


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    masks_to_buy = 0

    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except NotVaccinatedError as e:
            return f"✗ NotVaccinatedError: {e}"
        except OutdatedVaccineError as e:
            return f"✗ OutdatedVaccineError: {e}"
        except NotWearingMaskError as e:
            masks_to_buy += 1
            return f"✗ NotWearingMaskError: {e}"

    if masks_to_buy > 0:
        return f"Friends should buy {masks_to_buy} masks"

    return f"Friends can go to {cafe.name}"
